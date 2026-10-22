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

Each notebook has a settings cell near the top. Most notebooks work with no changes. A setting looks like
`WAKE_WORD = "hey mycroft"` or like `os.environ.setdefault("TTS_LANG", "en")`. To change a setting, change the last
value on its line, and keep the quotes around it. Some notebooks also have an "Advanced settings" cell, with settings
that most people do not change.

To run the notebook, there are two ways:

- Click Run All. The notebook runs while the page is open. Use this for a short run.
- Click Save Version, and select Save & Run All. Kaggle runs the notebook in the background, and you can close the
  page. When the version is complete, its files are in the Output tab of the version. Use this for a run of more than
  a few minutes.

A Kaggle session stops after 12 hours. If Kaggle stops a session, the files of that session are lost. So a single run
must end within 12 hours.

## Open a notebook on Google Colab

Make a Google account. Some notebooks have an "Open in Colab" button at the top: click it. For a notebook with no
such button, open [Colab](https://colab.research.google.com), select File > Open notebook > GitHub, and paste the
link of the notebook on GitHub. Internet is always on in Colab.
For a GPU, open the Runtime menu, select Change runtime type, select T4 GPU and click Save. Then open the Runtime menu
and select Run all.

Colab deletes all files when the session ends. Before you close the page, download the files you want to keep from the
file panel on the left.

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
