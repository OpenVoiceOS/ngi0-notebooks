# OpenVoiceOS Notebooks

Notebooks for [OpenVoiceOS](https://openvoiceos.org): wake words, text-to-speech voices and datasets, intents and more. Press a button to open a notebook on Kaggle, then **Run All**.

| Notebook | What it does | Needs | Run |
|---|---|---|---|
| [`kaggle_quickstart_ww`](notebooks/kaggle_quickstart_ww.ipynb) | Train a wake-word model for any phrase, start to finish | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/kaggle_quickstart_ww.ipynb) |
| [`synthetic_ww_dataset`](notebooks/synthetic_ww_dataset.ipynb) | Make a wake-word dataset; run several in parallel and train the quickstart on them | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/synthetic_ww_dataset.ipynb) |
| [`tts2ww_full_pipeline`](notebooks/tts2ww_full_pipeline.ipynb) | Build a larger wake-word practice set with noise and room echo | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts2ww_full_pipeline.ipynb) |
| [`tts_dataset_gen`](notebooks/tts_dataset_gen.ipynb) | Make a TTS dataset by synthesising text prompts in one voice | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`asr2tts`](notebooks/asr2tts.ipynb) | Turn transcribed recordings, such as Common Voice, into a single-voice TTS dataset | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_corpus_ingest`](notebooks/tts_corpus_ingest.ipynb) | Read a speech corpus into a dataset manifest | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_corpus_ingest.ipynb) |
| [`tts_enhance`](notebooks/tts_enhance.ipynb) | Denoise and clean every clip of a dataset | CPU; GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_enhance.ipynb) |
| [`tts_voice_convert`](notebooks/tts_voice_convert.ipynb) | Convert every clip of a dataset to a target voice | CPU; GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_voice_convert.ipynb) |
| [`tts_measure`](notebooks/tts_measure.ipynb) | Score every clip of a dataset for quality | GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_measure.ipynb) |
| [`tts_select`](notebooks/tts_select.ipynb) | Keep the best clips of a dataset | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_select.ipynb) |
| [`tts_publish`](notebooks/tts_publish.ipynb) | Publish a finished dataset to Hugging Face | GPU for the demo | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_publish.ipynb) |
| [`train_vits`](notebooks/train_vits.ipynb) | Train a TTS voice and export it to ONNX | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`ovos_intent_eval_and_train`](notebooks/ovos_intent_eval_and_train.ipynb) | Measure the published intent classifiers, language by language | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/ovos_intent_eval_and_train.ipynb) |
| [`speaker_verification`](notebooks/speaker_verification.ipynb) | Enrol a speaker and verify them by voice | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/speaker_verification.ipynb) |
| [`interop_mcp_utcp_clients`](notebooks/interop_mcp_utcp_clients.ipynb) | Call the OVOS TTS and STT servers through MCP and UTCP | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/interop_mcp_utcp_clients.ipynb) |
| [`bus_message_validation`](notebooks/bus_message_validation.ipynb) | Check OVOS bus messages against their schemas | CPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/bus_message_validation.ipynb) |
| [`arena_prediction_runner`](notebooks/arena_prediction_runner.ipynb) | Run a speech recogniser over a test set for the plugin arena | GPU | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/arena_prediction_runner.ipynb) |

On Kaggle, turn on **Internet** and, for a GPU notebook, pick a **GPU** accelerator in the notebook settings. New to notebooks? Read the [tester guide](docs/tester-guide.md); the TTS dataset steps and their order are in [docs/pipeline.md](docs/pipeline.md).

Licensed under the [Apache License 2.0](LICENSE). To change a notebook, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Developed by [TigreGotico](https://tigregotico.pt) for [OpenVoiceOS](https://openvoiceos.org).

[![NGI0 Commons Fund](./ngi.png)](https://nlnet.nl/project/OpenVoiceOS)

This project was funded through the [NGI0 Commons Fund](https://nlnet.nl/commonsfund), a fund established by [NLnet](https://nlnet.nl) with financial support from the European Commission's [Next Generation Internet](https://ngi.eu) programme, under the aegis of DG Communications Networks, Content and Technology under grant agreement No [101135429](https://cordis.europa.eu/project/id/101135429).
