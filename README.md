# NGI0 Commons Fund: OpenVoiceOS Deliverable Notebooks

Developed by [TigreGótico](https://tigregotico.pt) for
[OpenVoiceOS](https://openvoiceos.org).

[![NGI0 Commons Fund](./ngi.png)](https://nlnet.nl/project/OpenVoiceOS)

This project was funded through the [NGI0 Commons Fund](https://nlnet.nl/commonsfund),
a fund established by [NLnet](https://nlnet.nl) with financial support from the
European Commission's [Next Generation Internet](https://ngi.eu) programme, under
the aegis of [DG Communications Networks, Content and Technology](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/communications-networks-content-and-technology_en)
under grant agreement No [101135429](https://cordis.europa.eu/project/id/101135429).
The individual project is NGI0 Commons Fund grant 2025-04-289, "OpenVoiceOS —
From Beta to Breakthrough".

Each notebook maps to one or more NGI0 work items. Each notebook is written for
non-developer audiences, with clear prose cells that explain every step.

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Start here

Notebooks form four independent pipelines; pick the one matching your goal
and run its notebooks in order.

- **Wake word**: run [`synthetic_ww_dataset.ipynb`](notebooks/synthetic_ww_dataset.ipynb)
  locally on CPU to build a small wake-word dataset, then take that dataset
  into [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb)
  on Kaggle for GPU training. For a larger dataset with augmentation, use
  [`tts2ww_full_pipeline.ipynb`](notebooks/tts2ww_full_pipeline.ipynb) instead
  of the synthetic mini-dataset notebook.
- **TTS voice**: build or expand a voice dataset with
  [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) or
  [`asr2tts.ipynb`](notebooks/asr2tts.ipynb), then train the model in
  [`train_vits.ipynb`](notebooks/train_vits.ipynb). All three need a GPU.
- **Intent classifier**: train a monolingual model with
  [`ovos_intent_classifier_monolingual.ipynb`](notebooks/ovos_intent_classifier_monolingual.ipynb)
  or a multilingual one with
  [`ovos_intent_classifier_multilingual.ipynb`](notebooks/ovos_intent_classifier_multilingual.ipynb),
  then compare results with
  [`ovos_intent_benchmark.ipynb`](notebooks/ovos_intent_benchmark.ipynb).
- **Interoperability and bus validation**: run
  [`interop_mcp_utcp_clients.ipynb`](notebooks/interop_mcp_utcp_clients.ipynb),
  [`bus_message_validation.ipynb`](notebooks/bus_message_validation.ipynb),
  [`speaker_verification.ipynb`](notebooks/speaker_verification.ipynb), and
  [`arena_prediction_runner.ipynb`](notebooks/arena_prediction_runner.ipynb)
  locally on CPU.

`synthetic_ww_dataset.ipynb` needs outbound internet access to reach the
Edge TTS service, and its local install needs the `nest_asyncio` package (see
"Running locally" below).

---

## Notebook index

| Notebook | NGI work item | Cloud |
|---|---|---|
| [`train_vits.ipynb`](notebooks/train_vits.ipynb) | WP3: TTS model training & export | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) | WP3: Hybrid low-resource TTS dataset pipeline | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) | WP3: Synthetic TTS dataset generation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb) | WP2: Wake word model training (Kaggle) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/kaggle_quickstart_ww.ipynb) |
| [`tts2ww_full_pipeline.ipynb`](notebooks/tts2ww_full_pipeline.ipynb) | WP2: Wake word dataset generation and augmentation (full pipeline) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts2ww_full_pipeline.ipynb) |
| [`ovos_intent_classifier_monolingual.ipynb`](notebooks/ovos_intent_classifier_monolingual.ipynb) | WP4: Intent classification (monolingual) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_monolingual.ipynb) |
| [`ovos_intent_classifier_multilingual.ipynb`](notebooks/ovos_intent_classifier_multilingual.ipynb) | WP4: Intent classification (multilingual) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/ovos_intent_classifier_multilingual.ipynb) |
| [`ovos_intent_benchmark.ipynb`](notebooks/ovos_intent_benchmark.ipynb) | WP4: Intent classification benchmark | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/ovos_intent_benchmark.ipynb) |
| [`interop_mcp_utcp_clients.ipynb`](notebooks/interop_mcp_utcp_clients.ipynb) | WP1: MCP/UTCP interoperability | n/a |
| [`speaker_verification.ipynb`](notebooks/speaker_verification.ipynb) | WP2: Speaker verification & enrollment | n/a |
| [`bus_message_validation.ipynb`](notebooks/bus_message_validation.ipynb) | WP1: Bus message schema validation | n/a |
| [`arena_prediction_runner.ipynb`](notebooks/arena_prediction_runner.ipynb) | WP4: STT arena prediction slice | n/a |
| [`synthetic_ww_dataset.ipynb`](notebooks/synthetic_ww_dataset.ipynb) | WP2: Synthetic wake-word mini-dataset | n/a |

Every notebook not tagged `skip_execute` in its metadata is attempted by the
CI execute job on each push; the [Actions tab](../../actions) shows, for the
latest run, exactly which notebooks executed successfully and which failed.
Notebooks tagged `skip_execute` (the ones needing a GPU or a multi-GB
download) are only syntax-checked by CI and carry a visible `NOT EXECUTED`
banner in the notebook itself.

---

## Running locally

```bash
pip install jupyter nbformat nbconvert edge-tts nest_asyncio

# Execute a single notebook (≤10 min cap)
jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 \
    notebooks/speaker_verification.ipynb --output notebooks/speaker_verification.ipynb
```

---

## CI

`.github/workflows/ci.yml` runs on every push and does two checks:
- **nbformat lint** on every notebook.
- **`jupyter nbconvert --execute`** on notebooks that do not carry the `skip_execute` metadata tag; a missing dependency fails the install step instead of surfacing later as a notebook failure.

---

## Repository structure

```
notebooks/
  *.ipynb          - all deliverable notebooks
requirements/
  *.txt            - per-notebook extra dependencies
.github/workflows/
  ci.yml
LICENSE            - Apache License 2.0
```
