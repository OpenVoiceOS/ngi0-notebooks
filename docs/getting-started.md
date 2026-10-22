<!-- For AI agents: read AGENTS.md at the root of this repository. -->

# Getting started with the notebooks

This guide is for people who have never used a notebook. A notebook is a web page with small blocks of code, called
cells. You open it in your browser, press one button, and the cells run one after the other. The results appear below
each cell. You do not need to install anything on your computer, and you do not need to know how to program.

The notebooks run for free on [Kaggle](https://www.kaggle.com) or on [Google Colab](https://colab.research.google.com).
Both lend you a computer for some hours. Many notebooks need a GPU, a graphics card that makes the work much faster.
Both sites give you a GPU for free, for a limited number of hours each week.

## Open a notebook on Kaggle

Make an account at kaggle.com. Before Kaggle lets you use the internet or a GPU, it asks you to confirm your phone
number once.

Open the notebook list in the [README](../README.md), and click the "Open in Kaggle" button of a notebook. Kaggle
opens a copy of the notebook in your account. Open the Settings panel on the right. Set Internet to on. If the
notebook needs a GPU, set Accelerator to GPU T4.

Each notebook has all its settings in one cell, the Settings cell. It is the first code cell that you see. Most
notebooks work with no changes. A setting looks like this:

```python
WAKE_WORD = setting("WAKE_WORD", "hey mycroft")   # the phrase that wakes the assistant
```

To change a setting, change the last value on its line, here `"hey mycroft"`, and keep the quotes around it. The text
after `#` explains the setting. The settings that most people do not change are at the end of the cell, after the line
`# ── Advanced ──`.

When you run a notebook on your own computer, you can also keep your settings outside the notebook. Write them in a
file called `.env` in the folder where the notebook runs, one setting on each line, for example
`WAKE_WORD=hey computer`. A value in `.env` replaces the value in the Settings cell.

## Accounts and tokens

Most notebooks need only a Kaggle account or a Google account for Colab. Some steps need more:

| You want to | You need | Where to get it |
|---|---|---|
| Put a dataset on Hugging Face (`tts_publish`) | A Hugging Face token with write access | [Hugging Face tokens](https://huggingface.co/settings/tokens), see below |
| Train from a private dataset on Hugging Face (`train_vits`) | A Hugging Face token with read access | [Hugging Face tokens](https://huggingface.co/settings/tokens), see below |
| Use Common Voice recordings (`asr2tts`) | A free Mozilla Data Collective account, and an API key to let the notebook download them | See below |
| Let an AI coding agent run notebooks on Kaggle | A Kaggle API token | [Use an AI coding agent](ai-agents.md) |

To get a Hugging Face token:

1. Make a free account at [huggingface.co](https://huggingface.co/join).
2. Open the [Access Tokens](https://huggingface.co/settings/tokens) page of your account settings.
3. Click Create new token. Select Write to put datasets on Hugging Face, or Read to only download them.
4. Type a name for the token, for example `notebooks`, and click Create token.
5. Copy the token. It starts with `hf_`. Hugging Face shows it only once, so keep it in a safe place.

To get a Mozilla Data Collective API key:

1. Make a free account at [mozilladatacollective.com](https://mozilladatacollective.com).
2. Open your Profile, and select API.
3. Create an API key, and copy it. Keep it in a safe place.

Before you download a dataset, with the key or on the website, open the page of the dataset and accept its terms. You
do this once for each dataset. Without it, the download stops with the message "Terms must be accepted before
downloading".

### Keep a token secret

Do not type a token or a key into the Settings cell. A saved notebook keeps it, and other people who open the notebook
can read it. Give it to the notebook as a secret instead. The examples below are for the Hugging Face token
`HF_TOKEN`. For the Mozilla Data Collective key, do the same with the name `MDC_API_KEY`.

- On Kaggle, open the Add-ons menu and select Secrets. Add a secret with the label `HF_TOKEN` and your token as its
  value, and turn it on for this notebook.
- On Colab, click the key icon on the left. Add a secret with the name `HF_TOKEN` and your token as its value, and turn
  on Notebook access.
- On your own computer, write the line `HF_TOKEN=` followed by your token in the `.env` file.

## Run a notebook on your own computer

You need Python 3.11 or 3.12 and the program [uv](https://docs.astral.sh/uv/). Download this repository, and open a
terminal in its folder. Each notebook has a list of the programs it needs in the folder `requirements`. Install them
for the notebook that you want to run, here `asr2tts`:

```bash
uv venv .venv --python 3.12
uv pip install -p .venv --prerelease=allow pip jupyter papermill -r requirements/asr2tts.txt
```

Then start Jupyter with `.venv/bin/jupyter lab`, open the notebook, and click Run All. To run all cells without
opening the notebook, write your settings in a `.env` file in a folder of your choice, and type:

```bash
.venv/bin/papermill notebooks/asr2tts.ipynb asr2tts-result.ipynb --cwd <your folder>
```

The results go into that folder, and `asr2tts-result.ipynb` holds the notebook with the output of each cell. A
notebook that needs a GPU needs an NVIDIA graphics card in your computer.

## Use the result of one notebook in the next

Some notebooks read the result of another notebook. On Kaggle, run the first notebook with Save & Run All. Then open
the second notebook, click Add Input, select Notebook output, and add the first notebook. Its files are then in the
folder `/kaggle/input/`. A notebook can read this folder, but it cannot write to it. Each notebook tells you which
setting to change when it needs a folder to write to.

To give a notebook a file from your computer, such as a recording of a voice, click Add Input and then Upload. Kaggle
makes a dataset from the file, and the notebook finds it in a folder under `/kaggle/input/`. The Input panel on the
right shows the full path of each file.

On Colab, put the result of the first notebook into a zip file and download it. In the second notebook, upload the zip
file with the file panel on the left. The notebooks that read such a file tell you how to unzip it and which setting
to change.

## If something goes wrong

A red box below a cell means that the cell stopped. Read the last line of the box. The notebooks explain the usual
causes in plain words, and tell you what to change.

The most usual cause is that Internet is off. Turn it on in the Settings panel, and press Run All again. If a notebook
says that it needs a GPU, set Accelerator to GPU T4 on Kaggle. On Colab, open the Runtime menu, select Change runtime
type, select T4 GPU and click Save. Then run the notebook again.

If a notebook says that the disk is almost full, start with an empty disk. On Kaggle, stop the session and start it
again. On Colab, open the Runtime menu and select Disconnect and delete runtime. Then open the notebook again.

## What to read next

- [Train a wake word](wake-words.md): a model that hears your phrase.
- [Train a TTS voice](pipeline.md): a voice that reads text aloud in your language.
- [Use an AI coding agent](ai-agents.md): let an agent run the notebooks for you.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
