<!-- For AI agents: read AGENTS.md at the root of this repository. The wake-word notebooks are kaggle_quickstart_ww, synthetic_ww_dataset, ww_train_streaming and tts2ww_full_pipeline. -->

# Train a wake word

A wake word is the phrase that makes a voice assistant start to listen, for example "hey mycroft". These notebooks
make a small model that hears your phrase. You need no recordings: a speech model called
[OmniVoice](https://github.com/k2-fsa/OmniVoice) speaks your phrase in many different voices, and the model learns from
them.

If you have never used a notebook, read [Getting started](getting-started.md) first.

## The notebooks

| Notebook | What it does | Hardware | Time |
|---|---|---|---|
| [`kaggle_quickstart_ww`](../notebooks/kaggle_quickstart_ww.ipynb) | Makes the voices, trains the model and tests it, from start to end | GPU | 1 to 1.5 hours |
| [`synthetic_ww_dataset`](../notebooks/synthetic_ww_dataset.ipynb) | Makes about 2,000 examples of your phrase, and examples of speech and sounds that must not wake the assistant | GPU | about 30 minutes |
| [`ww_train_streaming`](../notebooks/ww_train_streaming.ipynb) | Trains a streaming model from `synthetic_ww_dataset` runs | CPU | about 50 minutes |
| [`tts2ww_full_pipeline`](../notebooks/tts2ww_full_pipeline.ipynb) | Makes a larger set of examples of your phrase, with noise and room echo | GPU | depends on the size |

The times are for a Kaggle T4 GPU.

## A quick model

1. Open [`kaggle_quickstart_ww`](../notebooks/kaggle_quickstart_ww.ipynb) with its "Open in Kaggle" button.
2. In the Settings panel, set Internet to on and Accelerator to GPU T4.
3. In the Settings cell, set `WAKE_WORD` to your phrase, and `WW_LANGUAGE` to its language.
4. Click Save Version, select Save & Run All, and wait until the version is complete.

The notebook makes the voices, trains the model, and tests it on speech, sounds and music that must not wake the
assistant. The model is the file `wakehubert_output/best_f1.onnx`, in the Output tab of the version. The settings for
OpenVoiceOS are in `wakehubert_output/ovos_config.json`.

## A better model

A model hears its phrase better when it learns from more voices. Make the examples first, in several runs, and then
train on all of them.

1. Open [`synthetic_ww_dataset`](../notebooks/synthetic_ww_dataset.ipynb), and set your phrase and language as above.
2. Set `RUN_ID` to `1`, and run the notebook with Save & Run All.
3. Run it again with `RUN_ID` set to `2`, then `3`, and so on. The run name chooses the random numbers of the run,
   so each run makes different voices. The runs can go at the same time.
4. Open `kaggle_quickstart_ww`. Click Add Input, select Notebook output, and add every run.
5. Set `DATASET_DIRS = "/kaggle/input"`, and run the notebook with Save & Run All.

[`ww_train_streaming`](../notebooks/ww_train_streaming.ipynb) trains a streaming model from the same runs. A streaming
model uses less computing power on the device, because it processes each new piece of sound only once. It needs no
GPU.

[`tts2ww_full_pipeline`](../notebooks/tts2ww_full_pipeline.ipynb) makes a larger set of examples of your phrase, and
can add noise and room echo to them. It makes no examples that must not wake the assistant. By default, it makes a
short demo of 32 examples. For the full set of 900 examples for each phrase, set `SMOKE = False`.

## Use the model in OpenVoiceOS

1. Download `best_f1.onnx` from the Output tab, and copy it to `~/.local/share/mycroft/` on your device.
2. On the device, install the plugin with `pip install --pre ovos-ww-plugin-wakeforge`.
3. Add the settings from `ovos_config.json` to `~/.config/mycroft/mycroft.conf`.

A streaming model of `ww_train_streaming` is the file `ww_streaming_output/<phrase>_streaming.onnx`, with its own
`ovos_config.json`. Use it in the same way.

The last section of `kaggle_quickstart_ww` prints these settings, and explains the test numbers. The numbers describe
one run with voices made by a computer, so they do not tell how the model behaves in your home. Test the model with
your own voice and in your own room.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
