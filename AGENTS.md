# Instructions for AI coding agents

This repository holds Jupyter notebooks that make wake words and text-to-speech (TTS) voices for OpenVoiceOS. They
run on Kaggle or Google Colab. A person asks you to run them; this file tells you how. Read
[docs/index.md](docs/index.md) for the guides that a person reads, and [docs/ai-agents.md](docs/ai-agents.md) for
what the person prepared before you started.

## Rules

- Never change the files in `notebooks/` to do a run. For Kaggle, copy the notebook to a work folder outside the
  repository, and change the copy. Change `notebooks/` only when the person asks for a change to the notebook itself, and follow
  [CONTRIBUTING.md](CONTRIBUTING.md).
- Never write a Hugging Face token, a Kaggle token or another secret into a notebook, a cell or a file that you push.
  Kaggle keeps the source of every version. To publish to Hugging Face, run `tts_publish` on the person's computer
  with the token in the environment variable `HF_TOKEN`.
- Keep every Kaggle notebook private: leave `is_private` out of `kernel-metadata.json`, or set it to `true`.
- Ask the person before you start a run that uses more than one hour of GPU time, and tell them how many GPU hours
  the whole task needs. Kaggle gives a limited number of GPU hours each week.
- Ask the person before you publish anything.
- Report what each run did from its own output: the files it wrote, the counts it printed, and the errors. A run
  that ended is not a run that worked.

## Start from nothing

The person may have nothing prepared, and may ask for the whole task in one sentence, for example "make me a voice in
Galician". Then guide them through it, in this order.

1. **Check what exists.** Check for the Kaggle command-line tool and its token (`kaggle kernels list --mine`). If it is
   missing, give the person the steps of "Prepare once" in [docs/ai-agents.md](docs/ai-agents.md). Only the person
   can make accounts, confirm a phone number, create tokens and accept the terms of a dataset. Wait until they are
   done.
2. **Ask what they want.** Ask the questions below that the request does not answer. Ask them together, in one
   message. Give each question two to four options, mark the option you recommend, and say why in one sentence.
3. **Gather the data.** Find the sources for the language in [docs/tts-data-sources.md](docs/tts-data-sources.md) and
   [docs/mozilla-data-collective.md](docs/mozilla-data-collective.md). Show the person the candidates with their
   size and licence, and let them choose. A download from Mozilla Data Collective needs the person's account: ask
   them to accept the terms of the dataset on its page, and to create an API key, or to download the file and give
   you its path.
4. **Plan the runs.** Before you start, show the list of runs, which notebook each run uses, and the GPU hours of
   each. Start when the person agrees.
5. **Run, check and report** each step as this file explains. Stop and ask when a run fails in a way that the
   notebook output does not explain, or when the result is not what the plan said.

The questions for a TTS voice:

- **Language and dialect.** Which language, and which country or dialect? This sets `TTS_LANG`.
- **Where the speech comes from.** Explain the three approaches of [docs/tts-approaches.md](docs/tts-approaches.md),
  and recommend one for the language. OmniVoice is the default. When OmniVoice does not speak the language or the
  dialect well, show the TTS voices and the recordings that exist for it.
- **The voice.** The default voice, a copy of a recording that the person gives (3 to 10 seconds, with its exact
  words), or a voice from a description.
- **Licences.** Will the voice be used in a product that is sold? If yes, leave out the sources with "NC" in their
  licence.
- **GPU hours.** How many hours can the task use this week? One dataset run takes about 40 minutes, and two training
  rounds take about 22 hours.
- **Publish.** Keep the result private, or publish the dataset and the voice on Hugging Face under the person's
  account.

The questions for a wake word: the phrase, its language, and whether to make a quick model (one notebook, about one
and a half hours) or a better model (several dataset runs first).

When a request is not clear, ask. Do not choose for the person between options that change the result, the cost or
the licence.

## Change the settings of a notebook

Each notebook has all its settings in one cell, the Settings cell: the first code cell that a person sees. Each line
reads one setting, for example `TTS_LANG = setting("TTS_LANG", "en")`, and its comment explains it. The guides in
`docs/` explain the settings in more detail.

A setting comes from the environment variable with the same name. When that variable is not set, it comes from a line
`NAME=value` in a file `.env` in the folder where the notebook runs. When neither exists, the value in the cell is
used. So you never need to change the notebook to change a setting.

- **On the person's computer**, set the environment variables before you run the notebook, or write a `.env` file in
  its working folder.
- **On Kaggle**, a notebook gets no environment variables and no `.env` file from you. Add one code cell at the top
  of your copy, and leave the other cells as they are:

  ```python
  import os
  os.environ.update({"TTS_LANG": "pt-PT", "N_PROMPTS": "2000", "SMOKE": "False"})
  ```

Give every value as text. The notebook converts it to the type of the setting: `True` or `False` for a yes or no
setting, digits for a number, and JSON for a list, for example `'["pt-PT", "pt-BR"]'`. A value that does not fit
stops the notebook with an error that names the setting.

`SMOKE = True` runs a short test on a CPU with a few clips. It checks that the notebook runs, and its output is not a
dataset or a model. Set `SMOKE` to `False` for real work.

## Run a notebook on Kaggle

Install the Kaggle command-line tool with `uv tool install kaggle`. The person gave it a token; check it with
`kaggle kernels list --mine`.

1. Make a folder that holds the changed copy of the notebook and a file `kernel-metadata.json`:

   ```json
   {
     "id": "<kaggle-user>/<slug>",
     "title": "<title>",
     "code_file": "<notebook>.ipynb",
     "language": "python",
     "kernel_type": "notebook",
     "is_private": true,
     "enable_gpu": true,
     "enable_internet": true,
     "dataset_sources": [],
     "kernel_sources": []
   }
   ```

   The slug is the title in lower case, with dashes in place of spaces. Set `enable_gpu` to `false` for a notebook
   that runs on a CPU. Every notebook needs Internet.
2. Run `kaggle kernels push -p <folder>`. This sends the notebook and starts it.
3. Run `kaggle kernels status <kaggle-user>/<slug>` until the status is complete or error. A long run takes hours;
   check every few minutes, not every second.
4. Run `kaggle kernels output <kaggle-user>/<slug> -p <folder>/output` to download the files.

To give the files of one run to the next notebook, add the first run to `kernel_sources` of the next, as
`"<kaggle-user>/<slug>"`. To give it files from the person's computer, such as a WAV recording or a Common Voice
download, make a Kaggle dataset with `kaggle datasets init -p <folder>` and `kaggle datasets create -p <folder>`, and
add it to `dataset_sources`. Both kinds of input appear under `/kaggle/input/`. Find the exact path from the first
lines of the notebook output, or list `/kaggle/input/` in a short test run.

`/kaggle/input/` is read-only. A notebook writes to `/kaggle/working/`. `tts_measure`, `tts_enhance` and `tts_select`
write beside their input by default, so set `OUTPUT_DIR`, `ENH_OUTPUT_DIR` and `SELECTION_PATH` to a folder under
`/kaggle/working/`.

A Kaggle session stops after 12 hours, and a session that Kaggle stops keeps no output. Set every limit so that the
run ends before that. For `train_vits`, use two rounds of `MAX_TRAIN_HOURS = 11`. The second round has the first round
in `kernel_sources`, and sets `BASE_CKPT_URL` to the newest `.ckpt` file in `train_vits_out/checkpoints/` of the first
round, and `BASE_CONFIG_URL` to the `.json` file beside its `.onnx` file. Use full paths under `/kaggle/input/`.

## Run a notebook on the person's computer

A notebook that needs no GPU can run on the person's computer. Make a virtual environment with uv, install
`papermill` and `ipykernel` in it, set the environment variables or write a `.env` file in the working folder, and
run the notebook:

```
MANIFEST_PATH=<work folder>/measured/manifest.jsonl papermill notebooks/tts_select.ipynb <work folder>/tts_select.out.ipynb --cwd <work folder>
```

Each notebook installs its own packages in its first cells. Give the run a working folder outside the repository.

## Which notebook to run

- A wake word: `kaggle_quickstart_ww`, after one or more runs of `synthetic_ww_dataset` for a better model. See
  [docs/wake-words.md](docs/wake-words.md).
- A TTS voice with no recordings: `tts_dataset_gen`, then `train_vits`. See [docs/pipeline.md](docs/pipeline.md).
- A TTS voice from recordings of many speakers, such as Common Voice: `asr2tts`, then `tts_publish`, then
  `train_vits`. See [docs/pipeline.md](docs/pipeline.md).
- Where the speech for a language comes from: [docs/tts-approaches.md](docs/tts-approaches.md),
  [docs/tts-data-sources.md](docs/tts-data-sources.md) and
  [docs/mozilla-data-collective.md](docs/mozilla-data-collective.md).
- Each step on its own, with quality scores and rules: [docs/tts-step-by-step.md](docs/tts-step-by-step.md). The
  file format between steps is in [docs/manifest.md](docs/manifest.md).

## Check the result

Read the counts that each notebook prints at its end, and compare them with what you expected. A dataset has a
`manifest.jsonl` or a `metadata.csv`: count its lines. `train_vits` writes sample sentences spoken by the new voice.
Ask the person to listen to some clips and to the samples. You cannot hear whether a voice speaks a language well.
