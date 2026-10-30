# OpenVoiceOS Notebooks

These notebooks make and measure wake words and text-to-speech voices for [OpenVoiceOS](https://openvoiceos.org), an open source
voice assistant. Each notebook runs for free in your browser on Kaggle. Click "Open in
Kaggle", turn on Internet (and a GPU when the table says so), and click Run All. You do not need to install anything.

New to notebooks? The [getting started guide](docs/getting-started.md) explains Kaggle and Colab step by step. The
[documentation index](docs/index.md) lists every guide. You can also let an AI coding agent run the notebooks for
you: see [Use an AI coding agent](docs/ai-agents.md).

## Wake words

A wake word is the phrase that makes the assistant start to listen, for example "hey mycroft". Start with
`kaggle_quickstart_ww`: it makes a wake-word model for any phrase, from start to end. [Train a wake word](docs/wake-words.md)
explains this group.

| Notebook | What it does | Needs | Run |
|---|---|---|---|
| [`kaggle_quickstart_ww`](notebooks/kaggle_quickstart_ww.ipynb) | Train a wake-word model for any phrase, start to finish | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/kaggle_quickstart_ww.ipynb) |
| [`synthetic_ww_dataset`](notebooks/synthetic_ww_dataset.ipynb) | Make a wake-word dataset. Run it several times, and train the quickstart on all the runs | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/synthetic_ww_dataset.ipynb) |
| [`ww_train_streaming`](notebooks/ww_train_streaming.ipynb) | Train a streaming wake-word model from a dataset made by `synthetic_ww_dataset` | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/ww_train_streaming.ipynb) |
| [`tts2ww_full_pipeline`](notebooks/tts2ww_full_pipeline.ipynb) | Make a larger set of examples of your phrase, with noise and room echo | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts2ww_full_pipeline.ipynb) |

## Text-to-speech voices

A text-to-speech (TTS) voice reads text aloud. Start with `tts_dataset_gen`, which makes a dataset in one voice, and
then `train_vits`, which trains the voice. [Train a TTS voice](docs/pipeline.md) explains this group, with two
complete tutorials.

| Notebook | What it does | Needs | Run |
|---|---|---|---|
| [`tts_dataset_gen`](notebooks/tts_dataset_gen.ipynb) | Make a dataset: a speech model reads about 2,000 sentences in your language, in one voice | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`train_vits`](notebooks/train_vits.ipynb) | Train the voice, starting from a finished voice, and export it as an `.onnx` file | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`asr2tts`](notebooks/asr2tts.ipynb) | Turn transcribed recordings, such as Common Voice, into a single-voice TTS dataset | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_corpus_ingest`](notebooks/tts_corpus_ingest.ipynb) | Read existing recordings into a list of clips for the next notebooks | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_corpus_ingest.ipynb) |
| [`tts_enhance`](notebooks/tts_enhance.ipynb) | Remove noise and restore the sound of every clip | CPU, or a GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_enhance.ipynb) |
| [`tts_measure`](notebooks/tts_measure.ipynb) | Give every clip quality scores | GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_measure.ipynb) |
| [`tts_select`](notebooks/tts_select.ipynb) | Keep the best clips of a dataset | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_select.ipynb) |
| [`tts_voice_convert`](notebooks/tts_voice_convert.ipynb) | Convert every clip of a dataset to a target voice | CPU, or a GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_voice_convert.ipynb) |
| [`tts_publish`](notebooks/tts_publish.ipynb) | Publish a finished dataset to Hugging Face | GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_publish.ipynb) |

## Benchmarks

The notebooks in [`benchmarks/`](benchmarks/) measure OpenVoiceOS plugins with the
[plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena), which publishes its results on Hugging Face.
[Benchmarks](docs/benchmarks.md) explains them.

| Notebook | What it does | Needs | Run |
|---|---|---|---|
| [`ww_leaderboard`](benchmarks/ww_leaderboard.ipynb) | Read the published wake-word results of the boards that the arena lists, score them again with the arena's code, and compare the plugins | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/benchmarks/ww_leaderboard.ipynb) |
| [`ww_benchmark`](benchmarks/ww_benchmark.ipynb) | Install every wake-word plugin, run each one on the same test clips, and score it with the arena's code | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/benchmarks/ww_benchmark.ipynb) |
| [`intent_benchmark`](benchmarks/intent_benchmark.ipynb) | Install the intent pipeline plugins, train each intent fighter on the arena's intent test sets, and score it with the arena's code | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/benchmarks/intent_benchmark.ipynb) |

Licensed under the [Apache License 2.0](LICENSE). To change a notebook, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Developed by [TigreGotico](https://tigregotico.pt) for [OpenVoiceOS](https://openvoiceos.org).

[![NGI0 Commons Fund](./ngi.png)](https://nlnet.nl/project/OpenVoiceOS)

This project was funded through the [NGI0 Commons Fund](https://nlnet.nl/commonsfund), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) programme, under the aegis of DG Communications Networks, Content and Technology under grant agreement No [101135429](https://cordis.europa.eu/project/id/101135429).
