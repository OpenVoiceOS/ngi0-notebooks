# NGI0 Commons Fund: OpenVoiceOS Deliverable Notebooks

Developed by [TigreGótico](https://tigregotico.pt) for
[OpenVoiceOS](https://openvoiceos.org).

[![NGI0 Commons Fund](./ngi.png)](https://nlnet.nl/project/OpenVoiceOS)

This project was funded through the [NGI0 Commons Fund](https://nlnet.nl/commonsfund),
a fund established by [NLnet](https://nlnet.nl) with financial support from the
European Commission's [Next Generation Internet](https://ngi.eu) programme, under
the aegis of [DG Communications Networks, Content and Technology](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/communications-networks-content-and-technology_en)
under grant agreement No [101135429](https://cordis.europa.eu/project/id/101135429).

Each notebook maps to one or more NGI0 work items. Each notebook is written for
non-developer audiences, with clear prose cells that explain every step.

---

## Notebook index

| Notebook | NGI work item | Executed in CI | Cloud |
|---|---|---|---|
| [`train_vits.ipynb`](notebooks/train_vits.ipynb) | WP3: TTS model training & export | No, parse-only (GPU training) | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/TigreGotico/train-vits) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) | WP3: Hybrid low-resource TTS dataset pipeline | No, parse-only (GPU denoising + VC) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) | WP3: Synthetic TTS dataset generation | No, parse-only (VC requires GPU) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb) | WP2: Wake word model training (Kaggle) | No, parse-only (GPU training) | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/TigreGotico/ww-trainer-quickstart) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/kaggle_quickstart_ww.ipynb) |
| [`tts2ww_full_pipeline.ipynb`](notebooks/tts2ww_full_pipeline.ipynb) | WP2: Wake word dataset generation and augmentation (full pipeline) | No, parse-only (GPU training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/tts2ww_full_pipeline.ipynb) |
| [`ovos_intent_classifier_monolingual.ipynb`](notebooks/ovos_intent_classifier_monolingual.ipynb) | WP4: Intent classification (monolingual) | No, parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_monolingual.ipynb) |
| [`ovos_intent_classifier_multilingual.ipynb`](notebooks/ovos_intent_classifier_multilingual.ipynb) | WP4: Intent classification (multilingual) | No, parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_multilingual.ipynb) |
| [`ovos_intent_benchmark.ipynb`](notebooks/ovos_intent_benchmark.ipynb) | WP4: Intent classification benchmark | No, parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_benchmark.ipynb) |
| [`interop_mcp_utcp_clients.ipynb`](notebooks/interop_mcp_utcp_clients.ipynb) | WP1: MCP/UTCP interoperability | Yes | n/a |
| [`speaker_verification.ipynb`](notebooks/speaker_verification.ipynb) | WP2: Speaker verification & enrollment | Yes | n/a |
| [`bus_message_validation.ipynb`](notebooks/bus_message_validation.ipynb) | WP1: Bus message schema validation | Yes | n/a |
| [`arena_prediction_runner.ipynb`](notebooks/arena_prediction_runner.ipynb) | WP4: STT arena prediction slice | Yes | n/a |
| [`synthetic_ww_dataset.ipynb`](notebooks/synthetic_ww_dataset.ipynb) | WP2: Synthetic wake-word mini-dataset | Yes | n/a |

CI validates the syntax of **parse-only** notebooks but does not run them, because they need GPU training or multi-GB downloads. Each parse-only notebook shows a visible `NOT EXECUTED` banner.

---

## Running locally

```bash
pip install jupyter nbformat nbconvert edge-tts

# Execute a single notebook (≤10 min cap)
jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 \
    notebooks/speaker_verification.ipynb --output notebooks/speaker_verification.ipynb
```

---

## CI

`.github/workflows/ci.yml` runs on every push and does two checks:
- **nbformat lint** on every notebook.
- **`jupyter nbconvert --execute`** on notebooks that do not carry the `skip-execute` metadata tag.

---

## Repository structure

```
notebooks/
  *.ipynb          - all deliverable notebooks
requirements/
  *.txt            - per-notebook extra dependencies
.github/workflows/
  ci.yml
```
