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

## TTS dataset pipeline

The TTS dataset notebooks form a chain: each one reads a manifest, does one step, and writes a
manifest for the next. Clips are measured once, and selection is a separate step. The chain,
the manifest format and the language registry are described in:

- [docs/pipeline.md](docs/pipeline.md): the steps and how they connect.
- [docs/manifest.md](docs/manifest.md): the manifest and selection file formats.
- [docs/registry.md](docs/registry.md): the per-language registry of admitted donors, corpora and
  judges ([registry/tts.yaml](registry/tts.yaml)).

## TTS voice datasets

OpenVoiceOS publishes single-speaker TTS datasets for two voice identities,
miro (male) and dii (female), across two Hugging Face collections:
[synthetic datasets](https://huggingface.co/collections/TigreGotico/synthetic-tts-datasets)
and [voice-converted datasets](https://huggingface.co/collections/TigreGotico/tts-voice-converted-datasets).
The source for each language is listed in [`docs/tts-data-sources.md`](docs/tts-data-sources.md).

| Language | miro | dii | Sources |
|---|---|---|---|
| Arabic, Modern Standard, diacritized | [9,994 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_ar-diacritics) | [9,995 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_ar-diacritics) | [Arabic, Modern Standard, diacritized](docs/tts-data-sources.md#arabic-modern-standard-diacritized-ar) |
| Arabic, Najdi and Hijazi | [1,099 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_ar-SA)<br>[8,189 clips](https://huggingface.co/datasets/TigreGotico/tts-vc-miro_ar-SA) | — | [Arabic, Najdi and Hijazi](docs/tts-data-sources.md#arabic-najdi-and-hijazi-ar-sa) |
| Arabic, Qatari | [7,592 clips](https://huggingface.co/datasets/TigreGotico/tts-vc-miro_ar-QA) | — | [Arabic, Qatari](docs/tts-data-sources.md#arabic-qatari-ar-qa) |
| Aragonese | [7,592 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_mcv-scripted-v23.0_an_miro) | [7,592 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_mcv-scripted-v23.0_an_dii) | [Aragonese](docs/tts-data-sources.md#aragonese-an) |
| Asturian | [720 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_mcv-scripted-v23.0_ast_miro) | [720 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_mcv-scripted-v23.0_ast_dii) | [Asturian](docs/tts-data-sources.md#asturian-ast) |
| Basque | [2,790 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_eu-ES) | [2,790 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_eu-ES) | [Basque](docs/tts-data-sources.md#basque-eu) |
| Catalan (Balearic) | [726 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_LaFrescat-ca-ES-balear_miro) | — | [Catalan (Balearic)](docs/tts-data-sources.md#catalan-ca) |
| Catalan (Central) | [899 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_LaFrescat-ca-ES-central_miro) | — | [Catalan (Central)](docs/tts-data-sources.md#catalan-ca) |
| Catalan (Occidental) | [659 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_LaFrescat-ca-ES-occidental_miro) | — | [Catalan (Occidental)](docs/tts-data-sources.md#catalan-ca) |
| Catalan (Valencian) | [574 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_LaFrescat-ca-ES-valencia_miro) | — | [Catalan (Valencian)](docs/tts-data-sources.md#catalan-ca) |
| Danish | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_da-DK) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_da-DK) | [Danish](docs/tts-data-sources.md#danish-da-dk) |
| Dutch, Netherlands | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_nl-NL) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_nl-NL) | [Dutch, Netherlands](docs/tts-data-sources.md#dutch-netherlands-nl-nl) |
| English, American | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_en-US) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_en-US) | [English, American](docs/tts-data-sources.md#english-american-en-us) |
| English, British and Irish | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_en-GB) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_en-GB) | [English, British and Irish](docs/tts-data-sources.md#english-british-and-irish-en-gb) |
| French | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_fr-FR_slow) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_fr-FR_slow) | [French](docs/tts-data-sources.md) |
| Galician | [9,999 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_sabela_gl-ES_miro) | [9,999 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_sabela_gl-ES_dii) | [Galician](docs/tts-data-sources.md#galician-gl) |
| German | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_de-DE) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_de-DE) | [German](docs/tts-data-sources.md#german-de-de) |
| Hebrew | [952 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_ILSpeech_he_miro) | [952 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_ILSpeech_he_dii) | [Hebrew](docs/tts-data-sources.md#hebrew-he-il) |
| Hindi | [1,100 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_hi-IN) | — | [Hindi](docs/tts-data-sources.md#hindi-hi-in) |
| Italian | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_it-IT)<br>[300 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_paola_it-IT_miro) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_it-IT)<br>[300 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_paola_it-IT_dii) | [Italian](docs/tts-data-sources.md) |
| Japanese | [1,100 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_ja-JP) | [1,100 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_ja-JP) | [Japanese](docs/tts-data-sources.md#japanese-ja-jp) |
| Kabyle | [57,383 clips](https://huggingface.co/datasets/fdemelo/tts-vc-kabyle-22khz-kab-dz-miro) | [57,383 clips](https://huggingface.co/datasets/fdemelo/tts-vc-kabyle-22khz-kab-dz-dii) | [Kabyle](docs/tts-data-sources.md#kabyle-kab) |
| Marwari | [4,247 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_Vaani_marwari_mwr_miro) | [4,247 clips](https://huggingface.co/datasets/TigreGotico/tts_vc_Vaani_marwari_mwr_dii) | [Marwari](docs/tts-data-sources.md#marwari-mwr-in) |
| Mirandese | [346 clips](https://huggingface.co/datasets/TigreGotico/vc-mwl-miro) | [345 clips](https://huggingface.co/datasets/TigreGotico/vc-mwl-dii) | [Mirandese](docs/tts-data-sources.md#mirandese-mwl) |
| Persian | [1,996 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_fa-IR) | [1,997 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_fa-IR) | [Persian](docs/tts-data-sources.md#persian-fa-ir) |
| Polish | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_pl-PL) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_pl-PL) | [Polish](docs/tts-data-sources.md#polish-pl) |
| Portuguese, Brazilian | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_pt-BR) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_pt-BR) | [Portuguese, Brazilian](docs/tts-data-sources.md#portuguese-brazilian-pt-br) |
| Portuguese, European | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_pt-PT_v2)<br>[1,349 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_pt-PT) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_pt-PT_v2)<br>[1,349 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_pt-PT) | [Portuguese, European](docs/tts-data-sources.md#portuguese-european-pt-pt) |
| Romanian | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_ro-RO) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_ro-RO) | [Romanian](docs/tts-data-sources.md#romanian-ro) |
| Spanish, Castilian | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_es-ES) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_es-ES) | [Spanish, Castilian](docs/tts-data-sources.md#spanish-castilian-es-es) |
| Spanish, Colombian | [5,192 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_es-CO) | [5,192 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_es-CO) | [Spanish, Colombian](docs/tts-data-sources.md#spanish-colombian-es-co) |
| Swedish | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-miro_sv-SE) | [1,150 clips](https://huggingface.co/datasets/TigreGotico/tts-train-synthetic-dii_sv-SE) | [Swedish](docs/tts-data-sources.md#swedish-sv-se) |
| West Frisian | [9,676 clips](https://huggingface.co/datasets/TigreGotico/tts-vc-mcv-scripted-v24.0-fy-nl-miro) | [9,676 clips](https://huggingface.co/datasets/TigreGotico/tts-vc-mcv-scripted-v24.0-fy-nl-dii) | [West Frisian](docs/tts-data-sources.md#west-frisian-fy-nl) |

---

## Notebook index

| Notebook | NGI work item | Cloud |
|---|---|---|
| [`train_vits.ipynb`](notebooks/train_vits.ipynb) | WP3: TTS model training & export | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/train_vits.ipynb) |
| [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) | WP3: Hybrid low-resource TTS dataset pipeline | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/asr2tts.ipynb) |
| [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) | WP3: Synthetic TTS dataset generation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_dataset_gen.ipynb) |
| [`tts_enhance.ipynb`](notebooks/tts_enhance.ipynb) | WP3: TTS dataset enhancement | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OpenVoiceOS/ngi0-notebooks/blob/dev/notebooks/tts_enhance.ipynb) |
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

Each notebook installs its own pinned dependencies in its first code cell; the
same pins are also listed in `requirements/<notebook>.txt`.

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
docs/
  *.md             - pipeline, manifest and registry reference
registry/
  tts.yaml         - admitted donors, corpora and judges per language
requirements/
  *.txt            - per-notebook extra dependencies
docs/
  tts-data-sources.md - speech sources for TTS dataset generation, by language
.github/workflows/
  ci.yml
LICENSE            - Apache License 2.0
```
