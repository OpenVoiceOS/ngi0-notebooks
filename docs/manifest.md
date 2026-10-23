<!-- For AI agents: read AGENTS.md at the root of this repository. -->

# Manifest format

The TTS dataset notebooks pass a list of audio clips from one notebook to the next. This list is a file called a
manifest. You need this page only if you want to read a manifest yourself, or write one with your own tools. To use the
notebooks, read [Train a TTS voice](pipeline.md) instead.

A manifest is a JSON Lines file: each line is one JSON object, and each object describes one clip. Next to the manifest
there is a second file with the same name and the extension `.meta.json`. Its `notebooks` key lists the notebooks
that wrote the manifest, by their names without `.ipynb`, for example `["asr2tts"]`.

The path to each audio file is relative to the folder of the manifest. So you can move or upload a dataset as one
folder, and the paths still work.

## Fields of a clip

| Field | Type | Written by | Meaning |
|---|---|---|---|
| `id` | string | the notebook that makes the clip | A name for the clip. It is unique in the manifest, and no later notebook changes it. |
| `text` | string | `tts_dataset_gen`, `tts_corpus_ingest`, `asr2tts` | The words spoken in the clip. |
| `lang` | string | `tts_dataset_gen`, `tts_corpus_ingest`, `asr2tts` | The language code, with the country or dialect when there is one, for example `pt-PT` or `ca-ES-valencia`. The format is BCP-47. |
| `audio` | string | every notebook that makes audio | The path to the WAV file, relative to the manifest. |
| `duration_s` | number | every notebook that makes audio | The length of the audio, in seconds. |
| `sample_rate` | integer | every notebook that makes audio | The sample rate of the WAV file. |
| `source` | object | `tts_dataset_gen`, `tts_corpus_ingest`, `asr2tts` | Where the speech comes from. For a speech model: `{"kind": "tts", "plugin": ..., "voice": ..., "version": ...}`. For recordings: `{"kind": "corpus", "name": ..., "url": ..., "item": ...}`. |
| `speaker` | string | `tts_corpus_ingest` | The original speaker, when the recordings name one. |
| `parent_id` | string | `tts_enhance`, `tts_voice_convert`, `asr2tts` | The `id` of the clip that this clip was made from. |
| `identity` | string | `tts_voice_convert`, `asr2tts` | The name of the target voice. `tts_voice_convert` uses the names in `IDENTITIES`: `identity_a` and `identity_b` by default, or names you choose, such as `miro` and `dii`. `asr2tts` uses the file names of its reference recordings, for example `ref_a`. A built-in demo uses `demo`. |
| `provenance` | object | `tts_enhance` | Which tool cleaned the clip, and with which options: `{"denoise": {"engine": ..., "options": ...} or null, "enhance": {"engine": ..., "options": ...} or null}`. |
| `selected` | boolean | `tts_publish` | True when the clip passed the selection and went into the published dataset. |
| `scores` | object | `tts_measure`, `asr2tts` | The quality measurements of the clip. The next section lists them. |

A notebook adds fields, but it does not change a field that an earlier notebook wrote. A notebook that makes new
audio, such as `tts_enhance` or `tts_voice_convert`, writes new clips. Each new clip names the clip it was made from in
`parent_id`.

## Scores

Each key in `scores` is one measurement. The naturalness scores (UTMOS, DNSMOS and NISQA) each estimate the mark that
human listeners would give the clip, from 1 to 5. A key that ends in `cos` is a cosine similarity: a number that
compares two sets of measurements, where 1 means the same and 0 means not related.

| Key | Meaning |
|---|---|
| `utmos`, `nisqa_mos` | How natural the whole clip sounds, from [speechonnxmetrics](https://pypi.org/project/speechonnxmetrics/). Higher is better. |
| `dnsmos_sig`, `dnsmos_bak`, `dnsmos_ovrl` | DNSMOS marks for the voice, for the background noise, and for the clip overall. Higher is better. |
| `spk_cos` | How close the voice of the clip is to the reference recording of the target voice. Higher is closer. |
| `spk_cos_source` | How close the original recording is to the target voice, before the voice change. Compare it with `spk_cos` to see how much the voice change helped. |
| `echo_cos` | How close the loudness pattern of the clip is to that of the reference recording. A value near 1 means that the clip is a copy of the reference recording, not new speech. The example rules in `tts_select` remove a clip at 0.85 or more. |
| `len_diff_s` | The length of the clip minus the length of the clip it was made from, in seconds. |
| `hyp` | The words that the speech recogniser heard. `tts_measure` uses the recogniser in `STT_MODULE`. `asr2tts` uses `ASR_MODEL` or `ASR_STT_MODULE`. |
| `cer` | The character error rate: the part of the characters in `hyp` that differ from `text`. Case and punctuation are ignored. Lower is better. |
| `read_wer` | The part of the words that differ between two transcripts: of this clip, and of the clip it was made from. Lower is better. |

The `.meta.json` file records the tool behind each score: the package, its version and the model. When a notebook
cannot make a measurement, the key is absent. It is never written as zero.

`asr2tts` writes scores at two points. On each original recording, it writes `dnsmos_sig`, `dnsmos_bak`, `dnsmos_ovrl`,
and `nisqa_mos` when you select it, together with `hyp` and `cer`. These DNSMOS and NISQA values describe the recording
after noise removal. `asr2tts` measures them before it cuts the silence and makes the loudness equal. On each clip in the target voice, it
writes `spk_cos_source`, `spk_cos`, `utmos`, `hyp` and `cer`. Its `.meta.json` file also has two more keys. `gates`
gives, for each quality check, its limit, the number of clips before and after the check, the number of clips
that failed, and the hours before and after. `distributions`
gives, for each score, the number of clips and the 10th, 50th and 90th percentiles.

## Selection files

`tts_select` writes a selection file. It is a JSON Lines file with one kept `id` on each line. Its `.meta.json` file
records each rule and the number of clips that the rule removed. `tts_voice_convert` and `tts_publish` read a manifest
and a selection file together.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
