# Trying the wake-word notebooks

This guide is for a person who does not program. Three notebooks build and
train a wake-word model, the small model that makes a voice assistant start
listening when it hears a phrase such as "hey jarvis". You open a notebook
in your browser, press one button, wait, and read the result at the bottom.
You do not install anything on your own computer.

Most times below are rough. The times of synthetic_ww_dataset and of the
tts2ww_full_pipeline quick demo were measured on a Kaggle T4 GPU; the others
were not timed on Kaggle or Colab.

## Opening a notebook on Kaggle

Sign in at kaggle.com. Kaggle usually asks you to verify your phone number once
before it lets you switch on internet access or a GPU. Choose Create, then
New Notebook. In the notebook, open the File menu, choose Import Notebook,
and upload the `.ipynb` file you were sent. If the repository is public, the
"Open in Kaggle" badge at the top of each notebook does the same in one click.

Open the side panel on the right (Notebook options, or Session options) and
switch Internet on. Leave the Accelerator on None unless the notebook below
says you need a GPU. Then choose Run in the top menu and Run All. Kaggle
starts a session, runs the cells from top to bottom, and writes the results
under the Output tab on the right.

## Opening a notebook on Google Colab

Sign in at colab.research.google.com, choose File, then Upload notebook, and
pick the `.ipynb` file. Internet is always on. Colab opens notebooks with a
CPU unless you choose Runtime, Change runtime type, and pick a GPU. Then choose
Runtime and Run all. Files written by a Colab notebook disappear when the
session ends, so download the ones you want from the file panel on the left
before you close the tab.

## What each notebook does

**synthetic_ww_dataset** builds a folder of training examples. A speech
generator, OmniVoice, says the phrase "hey mycroft" about two thousand times,
and the notebook adds ordinary speech, sounds and music that must not wake an
assistant. Most voices are invented from a short description; the rest copy a
real person from a single spoken word. Voices are distinct as far as the
notebook can tell: the split cannot exclude that two descriptions sound alike,
and copied voices are kept apart by their speaker ids. Run it with the
Accelerator set to a GPU and internet on; it took 21 minutes on a Kaggle T4.
You set nothing.
At the end it prints how many clips and voices it made and from which sources,
then `Dataset ready`; the folder is `synth_ww_output/run_1`, under the Output
tab on Kaggle. If you want another phrase, change `WAKE_WORD` in the Settings
cell before you press Run All. To make more data, run it again with a
different `RUN_ID` in the second cell, and give all the folders to
kaggle_quickstart_ww through its `DATASET_DIRS`.

**kaggle_quickstart_ww** trains a wake-word model for the phrase "hey mycroft" (or
any phrase you type). A speech generator, OmniVoice, speaks the phrase in about
two thousand voices; the notebook adds ordinary speech, sound and music from
public datasets, trains a small model, retrains it on the speech and sound it
wrongly likes, chooses a detection threshold on a separate two-hour stream, and
loads the model through the OVOS wake-word plugin. Run it with the Accelerator
set to a GPU and internet on; it takes about 45 minutes to an hour and a half.
You set nothing. At the end it prints what it measured: how many held-out
synthetic voices were detected, how many held-out speech, noise and silence
clips fired by mistake, and how many false wake-ups per hour an unseen two-hour
stream of speech, sound and music caused, with a 95 % interval. The notebook
does not judge these numbers, and they are not a claim about how the model
performs in a home. You also get the model file `best_f1.onnx` and
`ovos_config.json`. The threshold is chosen on a held-out stream, not calibrated
in the wakeforge sense. `SMOKE = True` in the second cell runs a few-minute
check that only proves the steps run.

**tts2ww_full_pipeline** builds a larger practice set of your phrase. The
OmniVoice speech generator says it in a new voice for every clip, each voice
designed from a short description such as "female, young adult, moderate
pitch", and the notebook can add noise and room echo when you give it folders
of sounds. Every clip says the phrase: the notebook makes no examples that
must not wake the assistant. By default it runs a quick demo with 32 examples;
it needs internet and a GPU, and took under three minutes on a Kaggle T4. You set nothing. At the end a
summary table lists how many files each stage wrote, and a final line names
the folder it wrote. Stages that need folders you did not provide say they
were skipped; that is normal. The full set, 900 examples per phrase, is chosen
by changing `SMOKE = True` to `SMOKE = False` in the second cell.

## At a glance

| Notebook | Runs as is | Time without a GPU | GPU | Must set |
|---|---|---|---|---|
| synthetic_ww_dataset | yes | needs a GPU (21 minutes on a Kaggle T4); the smoke check takes a minute | yes | nothing (internet on) |
| kaggle_quickstart_ww | yes | needs a GPU for the full run (about an hour); the smoke check takes a few minutes | yes, for the full run | nothing (internet on) |
| tts2ww_full_pipeline | yes, quick demo | needs a GPU (under three minutes on a Kaggle T4) | yes | nothing (internet on) |

## If something goes wrong

A red error box means a cell stopped. Read the last line: the notebooks
explain the common causes in plain words. The most frequent one is internet
being off; switch it on in the side panel and press Run All again. If a
session times out, press Run All again; nothing needs to be repaired by hand.

If `kaggle_quickstart_ww` stops with a red error that begins with "The real run needs a GPU" or
mentions the Accelerator, switch the Accelerator to a GPU in the Kaggle settings
and press Run All again.

If it stops with a message that the disk is almost full, get a fresh disk. On
Colab choose Runtime, then Disconnect and delete runtime, and open the
notebook again. On Kaggle, stop the session and start it again. Then press
Run All.
