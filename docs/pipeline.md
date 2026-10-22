# TTS dataset pipeline

These notebooks make a speech dataset in one voice, and then train a text-to-speech (TTS) voice from that dataset. A
TTS voice turns written text into speech. Every notebook runs on [Kaggle](https://www.kaggle.com) or
[Colab](https://colab.research.google.com) for free, so you do not need to install anything on your computer.

This page starts with an overview of the notebooks. Then two tutorials take you from nothing to a trained voice. The
last part explains each of the separate notebooks, for people who want to check and control each step.

## Overview

| Notebook | What it does | Hardware | Step |
|---|---|---|---|
| [`tts_dataset_gen`](../notebooks/tts_dataset_gen.ipynb) | Makes a dataset: a speech model reads about 2,000 sentences in your language in one voice | GPU | 1-2a |
| [`asr2tts`](../notebooks/asr2tts.ipynb) | Makes a dataset from recordings and their text, such as Common Voice: cleans them, changes them to one voice and removes bad clips | CPU | |
| [`tts_corpus_ingest`](../notebooks/tts_corpus_ingest.ipynb) | Reads existing recordings into a list of clips | CPU | 2b |
| [`tts_enhance`](../notebooks/tts_enhance.ipynb) | Removes noise and restores the sound of each clip | CPU | 3 |
| [`tts_measure`](../notebooks/tts_measure.ipynb) | Gives each clip quality scores | CPU | 4 and 7 |
| [`tts_select`](../notebooks/tts_select.ipynb) | Keeps the clips whose scores pass your rules | CPU | 5 and 8 |
| [`tts_voice_convert`](../notebooks/tts_voice_convert.ipynb) | Changes every clip to one or more target voices | CPU | 6 |
| [`tts_publish`](../notebooks/tts_publish.ipynb) | Puts a finished dataset on Hugging Face | CPU | 9 |
| [`train_vits`](../notebooks/train_vits.ipynb) | Trains the voice and exports it as an `.onnx` file | GPU | 10 |

The step numbers give the order of the separate notebooks. Most of these notebooks name their step number at the top.

## Before you start

On Kaggle, open a notebook with its "Open in Kaggle" button. Open the Settings panel on the right, set Internet to
on, and for a GPU notebook set Accelerator to GPU T4. On Colab, open the Runtime menu, select Change runtime type,
select T4 GPU and click Save.

Each notebook has a settings cell near the top. You change a setting there, by changing the value after its equals sign.
Every setting has a default value. When you give them no input, the separate notebooks run a short demo, so you can
see that they work.

The output of one notebook is the input of the next. On Kaggle, run the first notebook with Save Version, Save & Run
All. When the version is complete, open the next notebook, click Add Input, select Notebook output, and add the first
notebook. Its files are then under `/kaggle/input/`, and a notebook cannot write there. Three notebooks write their
result beside their input by default, so on Kaggle set their output to a folder under `/kaggle/working/`:
`OUTPUT_DIR` in `tts_measure`, `ENH_OUTPUT_DIR` in `tts_enhance`, and `SELECTION_PATH` in `tts_select`. If you
forget, the notebook stops at once and tells you which setting to change.

## Tutorial 1: a voice from a language only

Use this tutorial when you have no recordings. A speech model makes the recordings for you.

### Make the dataset

1. Open [`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb) and turn on Internet and a GPU.
2. For a language other than English, type its code into `TTS_LANG`, for example `pt-PT`, `de` or `es-ES`.
3. Choose the voice, or keep the default voice of a young woman:
   - To copy a voice, set `REF_AUDIO` to a recording of 3 to 10 seconds, and set `REF_TEXT` to the exact words in it.
   - To invent a voice, set `VOICE_PROMPT` to a description, for example `male, middle-aged, low pitch`.
4. Click Save Version, select Save & Run All, and wait until the version is complete.

The run takes about 40 minutes on a Kaggle T4 GPU and makes about 75 minutes of speech. The result is the folder
`tts_dataset_run_1`. It holds the clips in `wavs/`, their text in `metadata.csv`, and a description of the run in
`dataset.json`.

The speech model is [OmniVoice](https://github.com/k2-fsa/OmniVoice), which speaks more than 600 languages. The
sentences come from [Tatoeba](https://tatoeba.org), a free collection of example sentences. Tatoeba does not filter
its sentences, so some of them contain swearing or violence. If OmniVoice does not speak your language, the notebook
stops and tells you what to do. In that case, set `DONOR_MODEL` to another voice that speaks the language: a voice of
the [phoonnx](https://github.com/TigreGotico/phoonnx) catalog or an OVOS TTS plugin.

### Train the voice

[`train_vits.ipynb`](../notebooks/train_vits.ipynb) does not train a voice from zero. It downloads a finished voice in
your language from the [phoonnx voices](https://huggingface.co/collections/TigreGotico/phoonnx-tts-models), and it
trains that voice further on your clips. This needs much less time and data than a voice from zero.

The setting `BASE` chooses the voice to start from. The default, `auto`, takes a phoonnx voice in your language, or a
[Piper](https://huggingface.co/datasets/rhasspy/piper-checkpoints) voice when there is no phoonnx voice. You can also
set `BASE` to a Piper folder yourself, for example `rhasspy/piper-checkpoints/en/en_US/lessac/medium`. If no voice
exists in your language, `auto` stops and lists your choices. Then start from a voice in another language,
preferably a related one. A voice in any language is a better start than a voice from zero, because it already knows
how to make speech sounds. The new voice can use only the speech sounds that the start voice knows. If more than 2
percent of the sounds in your text are missing from it, the notebook stops and says so. Then choose a voice of a
closer language. `BASE = "none"` trains from zero, and needs much more data and time.

1. Open `train_vits.ipynb` and turn on Internet and a GPU.
2. Click Add Input, select Notebook output, and add your finished `tts_dataset_gen` run.
3. Set `DATASET_DIRS = "/kaggle/input"`.
4. Set `MAX_TRAIN_HOURS = 11`. The section below explains why.
5. Click Save Version, select Save & Run All, and wait until the version is complete.

The output is in `train_vits_out/`. The voice is an `.onnx` file with a `.json` settings file. The notebook also
writes a few sentences spoken by the new voice, so you can listen to the result. Every 10 minutes it saves the state of
the training as a checkpoint file in `train_vits_out/checkpoints/`. A later run can continue the training from a
checkpoint.

### Train a second round

The training stops when the time in `MAX_TRAIN_HOURS` ends. The default is one hour. One hour shows that everything
works, but the voice is not ready.

Kaggle stops a session after 12 hours, and a session that Kaggle stops does not keep its output. So train in two
rounds of 11 hours each. The remaining hour of each round is for the install, the downloads and the export. The second
round continues from the last checkpoint of the first round.

1. Make a copy of your `train_vits` notebook.
2. Click Add Input, select Notebook output, and add the first round. Keep the `tts_dataset_gen` input as well.
3. Find the newest `.ckpt` file in `/kaggle/input/<first round>/train_vits_out/checkpoints/`. Set `BASE_CKPT_URL` to
   its full path.
4. Find the `.json` file that the first round wrote beside its `.onnx` file. Set `BASE_CONFIG_URL` to its full path.
5. Keep `DATASET_DIRS` and `MAX_TRAIN_HOURS = 11` as in the first round.
6. Click Save Version, select Save & Run All, and wait until the version is complete.

The two rounds use 22 hours of GPU time. Kaggle gives about 30 GPU hours each week, so both rounds fit in one week.

On your own computer there is no session limit. Set `MAX_TRAIN_HOURS` to the full time and run once. If the run
stops, run the notebook again with the same settings, and it continues from the newest checkpoint.

## Tutorial 2: a voice from transcribed recordings

Use this tutorial when you have recordings of people reading text aloud, together with the text they read. Such
recordings come from many speakers. A TTS voice needs one speaker, so the notebook changes every recording to one
target voice. [Common Voice](https://commonvoice.mozilla.org) is a free source of such recordings in many languages.

### Make the dataset

1. Open [`asr2tts.ipynb`](../notebooks/asr2tts.ipynb). It runs on a CPU, so you do not need a GPU.
2. Give it the recordings, in one of two ways:
   - For Common Voice, download the language from the Common Voice website, and add it as a Kaggle dataset. Set
     `COMMON_VOICE_DIR` to the folder that holds `clips/` and `validated.tsv`.
   - For other recordings, set `RAW_AUDIO_SOURCE` to the folder of audio files, and `METADATA_CSV` to the file that
     holds the text of each file.
3. Make a folder with one short, clean recording of the target voice, as a WAV file. Set `REF_VOICES_DIR` to
   that folder. Each WAV file in the folder is one target voice. For one voice, put one file in the folder.
4. Set `TTS_LANG` to the language of the recordings, for example `pt-PT`.
5. Click Save Version, select Save & Run All, and wait until the version is complete.

The notebook removes noise, cuts silence, makes the loudness equal, and removes clips that are too fast or too slow. It
then changes each clip to the target voice. Three quality checks remove bad clips:

- After the noise removal, a clip with a sound quality score (DNSMOS) under 2.5 is removed.
- A speech recogniser listens to each clip and compares what it hears with the text. A clip with more than 25 percent
  of its characters wrong is removed.
- After the voice change, a clip that does not sound like the target voice, or that sounds unnatural, is removed.

The result is in `asr2tts_workspace/`. `manifest.jsonl` lists the kept clips with their scores. `quality_scores.csv`
lists the scores of every clip, and `gate_summary.json` tells how many clips each check removed.

### Publish and train

`train_vits` reads a dataset from Hugging Face. So publish the result first:

1. Open [`tts_publish.ipynb`](../notebooks/tts_publish.ipynb) and add your `asr2tts` run as input.
2. Set `MANIFEST_PATH` to the `manifest.jsonl` of the run.
3. Set `HF_REPO` to the name of a new dataset on your Hugging Face account, for example `yourname/my-voice-pt-PT`.
4. Set `HF_TOKEN` to a Hugging Face token with write access, and set `HF_PUSH = "1"`.
5. Run the notebook.

Then train as in Tutorial 1, with one change: set `HF_DATASET` to the name of your published dataset, instead of
`DATASET_DIRS`.

## The separate notebooks

The separate notebooks do the same work as `asr2tts`, but each step is its own notebook. Use them when you want to see
the scores, change the rules and run a step again without running everything again.

The notebooks pass a list of clips from one step to the next. This list is a file called a manifest. It has one line
for each clip, with the text, the path to the audio file and, after measurement, the scores.
[manifest.md](manifest.md) describes the format. A step never changes its input file. It writes a new file, so you can
always go back.

### Step 1-2a or 2b: make the clips

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

### Step 3: clean the audio

[`tts_enhance.ipynb`](../notebooks/tts_enhance.ipynb) is optional. It restores the sound of each clip, and it can also
remove noise. Set `ENH_MANIFEST` to the manifest from step 1-2a or 2b. Set `DENOISE_ENGINE`, for example to `gtcrn`, to
remove noise as well. The notebook writes `<name>.enhanced.jsonl` and the new clips, in `enhanced/`, beside the
input. On Kaggle, set `ENH_OUTPUT_DIR` to a folder under `/kaggle/working/`, for example `/kaggle/working/enhanced`.
The original clips stay.

### Step 4: measure

[`tts_measure.ipynb`](../notebooks/tts_measure.ipynb) gives each clip quality scores. Set `MANIFEST_PATH` to the
manifest. The notebook writes `<name>.scored.jsonl` beside the input. On Kaggle, set `OUTPUT_DIR` to a folder under
`/kaggle/working/`, for example `/kaggle/working/measured`. The notebook then copies the audio there too, so the
scored manifest and its clips stay in one folder.

Every clip gets naturalness scores (UTMOS and DNSMOS). A speech recognition check also runs when you set
`STT_MODULE` to the name of an OVOS speech-to-text plugin, for example `ovos-stt-plugin-vosk`. The check writes the
character error rate, `cer`: the part of the characters that the recogniser got wrong. Without `STT_MODULE`, the
notebook does not compute `cer`.

### Step 5: select

[`tts_select.ipynb`](../notebooks/tts_select.ipynb) is optional. It keeps the clips that pass your rules, and writes
the list of kept clips to a selection file. It never deletes audio, so you can try other rules without measuring again.

Set `MANIFEST_PATH` to the scored manifest, and `RULES` to a list of rules. On Kaggle, also set `SELECTION_PATH` to a
file under `/kaggle/working/`, for example `/kaggle/working/selection.jsonl`. Each rule reads one score and compares it
with a value. For example, this rule keeps clips where the speech recogniser got at most 10 percent of the characters
wrong:

```
[{"score": "cer", "op": "<=", "value": 0.10}]
```

### Step 6: change the voice

[`tts_voice_convert.ipynb`](../notebooks/tts_voice_convert.ipynb) changes every clip to one or more target voices. Set
`VC_MANIFEST` to the manifest, and `VC_SELECTION` to the selection file from step 5, if you made one. Set
`IDENTITIES` to a name for each target voice, separated by commas, for example `miro,dii`. For each name, set
`REFERENCE_<NAME>` to a WAV recording of that voice, for example `REFERENCE_MIRO`.

The notebook writes one manifest for each voice, `<voice>/<voice>.jsonl`, with the clips in `<voice>/wavs/`.

### Steps 7 and 8: measure and select again

Run `tts_measure` again on the manifest of one voice. Set `REFERENCE_<NAME>` there too. The notebook then also
measures how close each clip is to the target voice (`spk_cos`), and with `PARENT_MANIFEST` set to the manifest before
the voice change, how much the length of each clip changed (`len_diff_s`). Then run `tts_select` again, to keep the clips for training. The `tts_select`
notebook shows a set of rules for this step.

### Step 9: publish

[`tts_publish.ipynb`](../notebooks/tts_publish.ipynb) puts one voice on Hugging Face. Set `MANIFEST_PATH` to the
manifest of that voice, and `SELECTION_PATH` to the selection file from step 8. Without a selection file, it publishes
every clip. Set `HF_REPO`, `HF_TOKEN` and `HF_PUSH = "1"` as in Tutorial 2.

### Step 10: train

Train with [`train_vits.ipynb`](../notebooks/train_vits.ipynb) as in Tutorial 1, with `HF_DATASET` set to the
published dataset.

## Choose the source speech

The OpenVoiceOS datasets on Hugging Face use two target voices: miro, a male voice, and dii, a female voice. The voice
change removes the sound of the original speaker. The pronunciation, the accent and the rhythm of the original speech
stay. So choose the source speech for correct pronunciation in your language and dialect.
[tts-data-sources.md](tts-data-sources.md) lists sources of speech for each language.

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
