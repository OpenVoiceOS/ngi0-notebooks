<!-- For AI agents: read AGENTS.md at the root of this repository. Before you run anything, ask the person which approach of docs/tts-approaches.md to use. -->

# Train a TTS voice

These notebooks make a speech dataset in one voice, and then train a text-to-speech (TTS) voice from that dataset. A
TTS voice turns written text into speech. Every notebook runs on [Kaggle](https://www.kaggle.com) or
[Colab](https://colab.research.google.com) for free, so you do not need to install anything on your computer.

This page starts with an overview of the notebooks. Then two tutorials take you from nothing to a trained voice.
If you have never used a notebook, read [Getting started](getting-started.md) first.

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

The step numbers give the order of the separate notebooks, which
[The TTS notebooks step by step](tts-step-by-step.md) explains. Most of these notebooks name their step number at
the top.

## Choose where the speech comes from

Tutorial 1 makes the speech with a speech model, and Tutorial 2 starts from recordings of real people.
[Where the speech comes from](tts-approaches.md) explains when to use each, and
[TTS voice data sources](tts-data-sources.md) lists the sources for each language.

## Before you start

On Kaggle, open a notebook with its "Open in Kaggle" button. Open the Settings panel on the right, set Internet to
on, and for a GPU notebook set Accelerator to GPU T4. On Colab, open the Runtime menu, select Change runtime type,
select T4 GPU and click Save.

Each notebook has all its settings in one cell, the Settings cell, at the top. A setting looks like
`TTS_LANG = setting("TTS_LANG", "en")`. To change it, change the last value on its line, and keep the quotes.
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
[Where the speech comes from](tts-approaches.md) explains the choices.

### Train the voice

[`train_vits.ipynb`](../notebooks/train_vits.ipynb) does not train a voice from zero. It downloads a finished voice in
your language from the [phoonnx voices](https://huggingface.co/collections/TigreGotico/phoonnx-tts-models), and it
trains that voice further on your clips. This needs much less time and data than a voice from zero.

The setting `BASE` chooses the voice to start from. The default, `auto`, takes a phoonnx voice in your language, or a
[Piper](https://huggingface.co/datasets/rhasspy/piper-checkpoints) voice when there is no phoonnx voice. You can also
set `BASE` to a Piper folder yourself, for example `rhasspy/piper-checkpoints/en/en_US/lessac/medium`. If no voice
exists in your language, `auto` stops and lists your choices. Then start from a voice in another language,
preferably a related one. A voice in any language is a better start than a voice from zero, because it already knows
how to make speech sounds. `BASE = "none"` trains from zero, and needs much more data and time.

A voice reads the sounds of a word, not its letters. A phonemizer turns the text into these sounds, and the setting
`PHONEMIZER` in the Advanced part of the Settings cell chooses it. We recommend
[orthography2ipa](https://github.com/TigreGotico/orthography2ipa) (o2i). The notebook uses `espeak` by default, because
Piper voices are trained with espeak. Note that espeak is under the GPL licence: a voice trained with espeak needs
espeak to speak, so it brings a GPL dependency into the software that uses it.

The phonemizer does not limit the choice of the base voice. The part of a voice that reads the sounds is its encoder.
When the base voice was trained with the same phonemizer, the training keeps its encoder, and the new voice learns
faster. With another phonemizer, the training discards the encoder, learns a new one, and keeps the rest of the voice.

The training also discards the encoder when more than 2 percent of the sounds in your text are missing from the base
voice. `auto` prefers a voice trained with your phonemizer, when one exists in your language.

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
3. Find the line `Checkpoint to continue from later` at the end of the output of the first round. It names a `.ckpt`
   file under `/kaggle/working/train_vits_out/checkpoints/`. In the second round, the same file is under
   `/kaggle/input/notebooks/<your Kaggle user>/<first round>/train_vits_out/checkpoints/`. Set `BASE_CKPT_URL` to
   that full path.
4. Find the `.json` file that the first round wrote beside its `.onnx` file, in `train_vits_out/exported/`. Set
   `BASE_CONFIG_URL` to its full path under `/kaggle/input/` in the same way.
5. Keep `DATASET_DIRS` and `MAX_TRAIN_HOURS = 11` as in the first round.
6. Click Save Version, select Save & Run All, and wait until the version is complete.

The two rounds use 22 hours of GPU time. Kaggle gives a limited number of GPU hours each week, and shows how many you
have left on your account page. Check that both rounds fit.

On your own computer there is no session limit. Set `MAX_TRAIN_HOURS` to the full time and run once. If the run
stops, run the notebook again with the same settings, and it continues from the newest checkpoint.

## Tutorial 2: a voice from transcribed recordings

Use this tutorial when you have recordings of people reading text aloud, together with the text they read. Such
recordings come from many speakers. A TTS voice needs one speaker, so the notebook changes every recording to one
target voice. [Common Voice](https://commonvoice.mozilla.org) is a free source of such recordings in many languages,
and [Speech datasets on Mozilla Data Collective](mozilla-data-collective.md) lists it with other sources.

### Make the dataset

1. Open [`asr2tts.ipynb`](../notebooks/asr2tts.ipynb). It runs on a CPU, so you do not need a GPU.
2. Give it the recordings, in one of two ways:
   - For Common Voice, find the Scripted Speech dataset of your language on
     [Mozilla Data Collective](https://mozilladatacollective.com), and accept its terms on its page. Set `MDC_DATASET`
     to the ID of the dataset, the last part of the address of its page. Give the notebook your Mozilla Data Collective
     API key as the secret `MDC_API_KEY`, as [Accounts and tokens](getting-started.md#accounts-and-tokens) explains.
     The notebook then downloads the dataset. You can also download and extract the dataset yourself, add it as a
     Kaggle dataset, and set `COMMON_VOICE_DIR` to the folder that holds `clips/`.
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
4. Get a Hugging Face token with write access, and give it to the notebook as a secret.
   [Accounts and tokens](getting-started.md#accounts-and-tokens) explains both steps. Do not type the token into the
   Settings cell.
5. Set `LICENSE` to the licence of your dataset, for example `cc-by-4.0`. Your licence cannot give more rights than
   the licence of your recordings, so read that licence on the page of the source dataset. To name the owner of the
   dataset on its page, set `OWNER` to your name. When `OWNER` is empty, the page names no owner.
6. Set `HF_PUSH = True`.
7. Run the notebook.

Then train as in Tutorial 1, with one change: set `HF_DATASET` to the name of your published dataset, instead of
`DATASET_DIRS`. If the dataset is private, give `train_vits` your token as a secret, in the same way as for
`tts_publish`.

## Every step on its own

The tutorials use a few notebooks that do many steps at once. Each step also has its own notebook, so you can see the
scores of each clip, change the rules, and run one step again. [The TTS notebooks step by step](tts-step-by-step.md)
explains them, the scores, and the hardware that each notebook needs.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
