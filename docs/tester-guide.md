# Trying the wake-word notebooks

This guide is for a person who does not program. Three notebooks build and
train a wake-word model, the small model that makes a voice assistant start
listening when it hears a phrase such as "hey jarvis". You open a notebook
in your browser, press one button, wait, and read the result at the bottom.
You do not install anything on your own computer.

The times below are rough: "a few minutes on a machine without a GPU". They
were not timed on Kaggle or Colab, and nothing was timed on a GPU.

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

**synthetic_ww_dataset** builds a small folder of spoken examples. A free
online text-to-speech service says the phrase "hey mycroft" twenty times in
five voices, and says ten similar-sounding phrases that must not wake an
assistant. It needs internet and no GPU, and it takes a few minutes. You
set nothing. At the end the last cell lists the folder `synth_ww_output` and
prints `Dataset ready`. If you want another phrase, change `WAKE_WORD` in the
Settings cell before you press Run All.

**kaggle_quickstart_ww** trains a wake-word model. By default it runs a quick
demo for the phrase "hey jarvis": it makes its own spoken examples, trains
for five short rounds, saves two model files, and checks them. The demo needs
internet and no GPU, and it takes a few minutes. You set nothing. At the
end you see scores for sample clips and a line called Margin. The Margin is
the line to look at: it should be clearly above zero. A message such as
"LOW - needs more data" next to the demo's confidence score is expected for
a model trained this briefly, and is not a failure. You also get the two model files `best_f1.onnx` and
`best_f1_featurizer.onnx`, and a block of settings to paste into an OVOS
configuration. The demo model proves the pipeline works; it is not good enough
to use. For a model worth using, change `SMOKE = True` to `SMOKE = False` in
the second cell and switch the Accelerator to a GPU; that run takes much
longer and was not timed. Advanced users can chain the notebooks so that one
feeds the next; that is not needed for a first try.

**tts2ww_full_pipeline** builds a larger practice set. It uses several online
text-to-speech voices to say your phrase, adds similar-sounding phrases that
must not wake the assistant, and can add noise and room echo when you give it
folders of sounds. By default it runs a quick demo with 32 examples; it
needs internet, no GPU, and a few minutes. You set nothing. At the end a summary
table lists how many files each stage wrote, and a final line names the
folder it wrote. Stages that need folders you did not
provide say they were skipped; that is normal. The full set, 900 examples per
phrase, is chosen by changing `SMOKE = True` to `SMOKE = False` in the second
cell; it took more than 45 minutes on a machine without a GPU.

## At a glance

| Notebook | Runs as is | Time without a GPU | GPU | Must set |
|---|---|---|---|---|
| synthetic_ww_dataset | yes | a few minutes | no | nothing (internet on) |
| kaggle_quickstart_ww | yes, quick demo | a few minutes | no for the demo | nothing (internet on) |
| tts2ww_full_pipeline | yes, quick demo | a few minutes | no | nothing (internet on) |

## If something goes wrong

A red error box means a cell stopped. Read the last line: the notebooks
explain the common causes in plain words. The most frequent one is internet
being off; switch it on in the side panel and press Run All again. If a
session times out, press Run All again; nothing needs to be repaired by hand.

If `kaggle_quickstart_ww` stops with a red error that says the median positive
score exceeds the median negative score "by only" a small amount, "at or below
the 0.1 margin this check requires", the demo did not get enough examples to
learn from. You did nothing wrong. Change `N_SAMPLES` to 64 in the second cell
(the one that says `SMOKE = True`) and press Run All; the notebook makes new
examples by itself.

If it stops with a message that the disk is almost full, get a fresh disk. On
Colab choose Runtime, then Disconnect and delete runtime, and open the
notebook again. On Kaggle, stop the session and start it again. Then press
Run All.
