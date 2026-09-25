# Manifest format

A manifest is a JSON Lines file: one JSON object per line, and one line per clip. A sidecar file
with the same name and the suffix `.meta.json` records the notebooks that wrote the manifest, each
by its plain stem (for example `asr2tts`, not `asr2tts.ipynb` or `tts_measure (demo)`).

Audio paths are relative to the manifest's directory. So you can move or upload a dataset as one
directory.

## Row fields

| Field | Type | Written by | Meaning |
|---|---|---|---|
| `id` | string | the step that creates the row | Unique in the manifest. It does not change in later steps. |
| `text` | string | prompts, corpus ingest | The text of record for the clip. |
| `lang` | string | prompts, corpus ingest | BCP-47 tag with the variety, for example `pt-PT` or `ca-ES-valencia`. |
| `audio` | string | synthesis, ingest, enhancement, conversion | Path to a WAV file, relative to the manifest. |
| `duration_s` | number | the step that writes `audio` | Audio duration in seconds. |
| `sample_rate` | integer | the step that writes `audio` | Sample rate of the WAV file. |
| `source` | object | synthesis, ingest | Where the speech comes from: `{"kind": "tts", "plugin": ..., "voice": ..., "version": ...}` or `{"kind": "corpus", "name": ..., "url": ..., "item": ...}`. |
| `speaker` | string | ingest | The source speaker, where the corpus names one. |
| `parent_id` | string | enhancement, conversion | The `id` of the row that this audio was made from. |
| `identity` | string | conversion | The target voice name: any value in `IDENTITIES` (`miro` and `dii` for the published TTS voice datasets), a notebook's own reference-voice names (`asr2tts` writes its `REF_VOICES_DIR` file stems, for example `ref_a`), or `demo` for a notebook's built-in demo. |
| `provenance` | object | enhancement | The engine and options behind each enhancement stage applied: `{"denoise": {"engine": ..., "options": ...} or null, "enhance": {"engine": ..., "options": ...} or null}`. |
| `selected` | boolean | publish | Whether the row passed selection and was copied into the published dataset. |
| `scores` | object | measure | One key for each measurement (see below). |

A step adds fields. It does not change a field that an earlier step wrote. A step that makes new
audio (enhancement, conversion) writes new rows, and each new row points to its parent row with
`parent_id`.

## Scores

Each key in `scores` names one measurement:

| Key | Meaning |
|---|---|
| `utmos`, `dnsmos_sig`, `dnsmos_bak`, `dnsmos_ovrl`, `nisqa_mos` | Naturalness estimates from speechonnxmetrics |
| `spk_cos` | Cosine similarity between the clip's speaker embedding and the identity reference |
| `echo_cos` | Cosine similarity between the clip's loudness envelope and the reference's envelope. A high value means that the clip is the reference itself. |
| `len_diff_s` | Converted duration minus parent duration, in seconds |
| `hyp` | The transcript from the recogniser named in `STT_MODULE` |
| `cer` | Character error rate of `hyp` against `text`, after text normalisation |
| `read_wer` | Word error rate between the readings of the clip and of its parent |

The `.meta.json` sidecar records the instrument behind each key: the package, its version and the
model. A measurement that a step could not make is absent, not zero.

## Selection files

A selection file is a JSON Lines file of kept `id` values. Its `.meta.json` sidecar records each
rule and the number of rows that the rule removed. A trainer reads a manifest and a selection
together.
