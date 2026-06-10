# NGI0 Commons Fund — OpenVoiceOS Deliverable Notebooks

Developed by **TigreGotico** for **OpenVoiceOS**, funded by the
[NGI0 Commons Fund](https://nlnet.nl/project/OpenVoiceOS) /
[NLnet](https://nlnet.nl) grant **101135429**.

> This project was funded through the NGI0 Commons Fund, a fund established by NLnet
> with financial support from the European Commission's Next Generation Internet programme,
> under the aegis of DG Communications Networks, Content and Technology under grant
> agreement No 101135429. Additional funding is made available by the Swiss State
> Secretariat for Education, Research and Innovation (SERI).

Each notebook maps to one or more NGI0 work items and is written for
**non-developer audiences** — clear prose cells explain every step.

---

## Notebook index

| Notebook | NGI work item | Executed in CI | Cloud |
|---|---|---|---|
| [`train_vits.ipynb`](notebooks/train_vits.ipynb) | WP3 — TTS model training & export | ❌ parse-only (GPU training) | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/TigreGotico/train-vits) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) | WP3 — Hybrid low-resource TTS dataset pipeline | ❌ parse-only (GPU denoising + VC) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) | WP3 — Synthetic TTS dataset generation | ❌ parse-only (VC requires GPU) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb) | WP2 — Wake word model training (Kaggle) | ❌ parse-only (GPU training) | [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/TigreGotico/ww-trainer-quickstart) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/kaggle_quickstart_ww.ipynb) |
| [`ovos_intent_classifier_monolingual.ipynb`](notebooks/ovos_intent_classifier_monolingual.ipynb) | WP4 — Intent classification (monolingual) | ❌ parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_monolingual.ipynb) |
| [`ovos_intent_classifier_multilingual.ipynb`](notebooks/ovos_intent_classifier_multilingual.ipynb) | WP4 — Intent classification (multilingual) | ❌ parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_multilingual.ipynb) |
| [`ovos_intent_benchmark.ipynb`](notebooks/ovos_intent_benchmark.ipynb) | WP4 — Intent classification benchmark | ❌ parse-only (HF download + training) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TigreGotico/ngi0-notebooks/blob/dev/notebooks/ovos_intent_benchmark.ipynb) |
| [`interop_mcp_utcp_clients.ipynb`](notebooks/interop_mcp_utcp_clients.ipynb) | WP1 — MCP/UTCP interoperability | ✅ executed | — |
| [`speaker_verification.ipynb`](notebooks/speaker_verification.ipynb) | WP2 — Speaker verification & enrollment | ✅ executed | — |
| [`bus_message_validation.ipynb`](notebooks/bus_message_validation.ipynb) | WP1 — Bus message schema validation | ✅ executed | — |
| [`arena_prediction_runner.ipynb`](notebooks/arena_prediction_runner.ipynb) | WP4 — STT arena prediction slice | ✅ executed | — |
| [`synthetic_ww_dataset.ipynb`](notebooks/synthetic_ww_dataset.ipynb) | WP2 — Synthetic wake-word mini-dataset | ✅ executed | — |

**parse-only** notebooks are validated for syntax by CI but not executed (heavy GPU
training or multi-GB downloads). They carry a visible `⚠ NOT EXECUTED` banner.

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

`.github/workflows/ci.yml` runs on every push:
- **nbformat lint** for every notebook
- **`jupyter nbconvert --execute`** for notebooks without the `skip-execute` metadata tag

---

## Repository structure

```
notebooks/
  *.ipynb          — all deliverable notebooks
requirements/
  *.txt            — per-notebook extra dependencies
.github/workflows/
  ci.yml
```
