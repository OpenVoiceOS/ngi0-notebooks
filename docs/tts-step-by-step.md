<!-- For AI agents: read AGENTS.md at the root of this repository. Each step reads the manifest of the step before it. -->

# The TTS notebooks step by step

[Train a TTS voice](pipeline.md) gives the overview of the TTS notebooks and two tutorials. Read it first. This page
explains each separate notebook.

The separate notebooks do the same work as `asr2tts`, but each step is its own notebook. Use them when you want to see
the scores, change the rules and run a step again without running everything again.

The notebooks pass a list of clips from one step to the next. This list is a file called a manifest. It has one line
for each clip, with the text, the path to the audio file and, after measurement, the scores.
[manifest.md](manifest.md) describes the format. A step never changes its input file. It writes a new file, so you can
always go back.

## Step 1-2a or 2b: make the clips

[`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb) makes the clips with a speech model, as in Tutorial 1.
Besides its training folder, it writes a manifest, `manifest.jsonl`.

[`tts_corpus_ingest.ipynb`](../notebooks/tts_corpus_ingest.ipynb) reads recordings that already exist. Set
`CORPUS_KIND` to the kind of source:

- `hf`: a dataset on Hugging Face. Set `HF_DATASET` to its name, and `TEXT_FIELD` and `AUDIO_FIELD` to its columns.
- `ljspeech`: a folder with `metadata.csv` and `wavs/`. Set `LJSPEECH_DIR` to the folder.
- `csv`: a CSV file with a text column and an audio path column. Set `CSV_PATH`, `CSV_TEXT_COL` and `CSV_AUDIO_COL`.

Set `CORPUS_LANG` to the language, for example `pt-PT`. To keep only some speakers, set `SPEAKERS` to their names, or
`TOP_SPEAKERS` to keep the speakers with the most audio. `MAX_HOURS` limits the hours of audio. The notebook writes
`manifest.jsonl` and the clips to its output folder.

## Step 3: clean the audio

[`tts_enhance.ipynb`](../notebooks/tts_enhance.ipynb) is optional. It restores the sound of each clip, and it can also
remove noise. Set `ENH_MANIFEST` to the manifest from step 1-2a or 2b. Set `DENOISE_ENGINE`, for example to `gtcrn`, to
remove noise as well. The notebook writes `<name>.enhanced.jsonl` and the new clips, in `enhanced/`, beside the
input. On Kaggle, set `ENH_OUTPUT_DIR` to a folder under `/kaggle/working/`, for example `/kaggle/working/enhanced`.
The original clips stay.

## Step 4: measure

[`tts_measure.ipynb`](../notebooks/tts_measure.ipynb) gives each clip quality scores. Set `MANIFEST_PATH` to the
manifest. The notebook writes `<name>.scored.jsonl` beside the input. On Kaggle, set `OUTPUT_DIR` to a folder under
`/kaggle/working/`, for example `/kaggle/working/measured`. The notebook then copies the audio there too, so the
scored manifest and its clips stay in one folder.

Every clip gets naturalness scores (UTMOS and DNSMOS). A speech recognition check also runs when you set
`STT_MODULE` to the name of an OVOS speech-to-text plugin, for example `ovos-stt-plugin-vosk`. The check writes the
character error rate, `cer`: the part of the characters that the recogniser got wrong. Without `STT_MODULE`, the
notebook does not compute `cer`.

## Step 5: select

[`tts_select.ipynb`](../notebooks/tts_select.ipynb) is optional. It keeps the clips that pass your rules, and writes
the list of kept clips to a selection file. It never deletes audio, so you can try other rules without measuring again.

Set `MANIFEST_PATH` to the scored manifest, and `RULES` to a list of rules. On Kaggle, also set `SELECTION_PATH` to a
file under `/kaggle/working/`, for example `/kaggle/working/selection.jsonl`. Each rule reads one score and compares it
with a value. For example, this rule keeps clips where the speech recogniser got at most 10 percent of the characters
wrong:

```
[{"score": "cer", "op": "<=", "value": 0.10}]
```

## Step 6: change the voice

[`tts_voice_convert.ipynb`](../notebooks/tts_voice_convert.ipynb) changes every clip to one or more target voices. Set
`VC_MANIFEST` to the manifest, and `VC_SELECTION` to the selection file from step 5, if you made one. Set
`IDENTITIES` to a name for each target voice, separated by commas, for example `miro,dii`. For each name, set
`REFERENCE_<NAME>` to a WAV recording of that voice, for example `REFERENCE_MIRO`.

The notebook writes one manifest for each voice, `<voice>/<voice>.jsonl`, with the clips in `<voice>/wavs/`.

## Steps 7 and 8: measure and select again

Run `tts_measure` again on the manifest of one voice. Set `REFERENCE_<NAME>` there too. The notebook then also
measures how close each clip is to the target voice (`spk_cos`), and with `PARENT_MANIFEST` set to the manifest before
the voice change, how much the length of each clip changed (`len_diff_s`). Then run `tts_select` again, to keep the clips for training. The `tts_select`
notebook shows a set of rules for this step.

## Step 9: publish

[`tts_publish.ipynb`](../notebooks/tts_publish.ipynb) puts one voice on Hugging Face. Set `MANIFEST_PATH` to the
manifest of that voice, and `SELECTION_PATH` to the selection file from step 8. Without a selection file, it publishes
every clip. Set `HF_REPO`, `OWNER`, `LICENSE` and `HF_PUSH = True`, and give the notebook a token, as in Tutorial 2.

## Step 10: train

Train with [`train_vits.ipynb`](../notebooks/train_vits.ipynb) as in Tutorial 1, with `HF_DATASET` set to the
published dataset.

## The target voices

The OpenVoiceOS datasets on Hugging Face use two target voices: miro, a male voice, and dii, a female voice. The voice
change removes the sound of the original speaker. The pronunciation, the accent and the rhythm of the original speech
stay. So choose the source speech for correct pronunciation in your language and dialect.
[Where the speech comes from](tts-approaches.md) explains how to choose it.

## Software and hardware

OmniVoice speaks the sentences. [audiosronnx](https://github.com/TigreGotico/audiosronnx) removes noise and restores
the audio. [speechonnxmetrics](https://pypi.org/project/speechonnxmetrics/) scores the naturalness, and
[speakeronnx](https://pypi.org/project/speakeronnx/) compares each clip with the target voice.
[voiceclonnx](https://pypi.org/project/voiceclonnx/) changes the voice. [phoonnx](https://github.com/TigreGotico/phoonnx)
trains the voice and exports it.

`tts_dataset_gen` and `train_vits` need a GPU. The other notebooks work on a CPU, and a GPU makes them faster. When
you give them no input, some of them run a short demo with OmniVoice, and that demo needs a GPU.

`asr2tts`, `tts_enhance`, `tts_measure` and `tts_voice_convert` run their models with onnxruntime, and install the
CPU build by default. For an NVIDIA graphics card, set `ONNX_RUNTIME = "cuda"`. For an AMD graphics card, set
`ONNX_RUNTIME = "rocm"`. `ONNX_PROVIDERS = "auto"` then uses the fastest hardware that the install supports.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
