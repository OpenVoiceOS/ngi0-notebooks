# NGI0 Commons Fund: OpenVoiceOS Deliverable Notebooks

Developed by [TigreGótico](https://tigregotico.pt) for
[OpenVoiceOS](https://openvoiceos.org).

[![NGI0 Commons Fund](./ngi.png)](https://nlnet.nl/project/OpenVoiceOS)

This project was funded through the NGI0 Commons Fund, a fund established by NLnet
with financial support from the European Commission's Next Generation Internet
programme, under the aegis of DG Communications Networks, Content and Technology
under grant agreement No 101135429. Additional funding is made available by the
Swiss State Secretariat for Education, Research and Innovation (SERI).
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
  locally on CPU to build a small labelled wake-word dataset (positives and
  adversarial negatives, written as a `path,label` metadata CSV), then point
  [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb) at that
  dataset directory through its `DATASET_DIR` variable to train on Kaggle's
  GPU. `kaggle_quickstart_ww.ipynb` can also build its own dataset from
  scratch without `synthetic_ww_dataset.ipynb`. For a larger dataset with
  augmentation, use
  [`tts2ww_full_pipeline.ipynb`](notebooks/tts2ww_full_pipeline.ipynb) instead
  of the synthetic mini-dataset notebook.
- **TTS voice**: build or expand a voice dataset with
  [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) or
  [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) (both CPU), then train the model in
  [`train_vits.ipynb`](notebooks/train_vits.ipynb) (GPU).
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

TigreGotico publishes single-speaker TTS datasets for OpenVoiceOS, for two
voice identities, miro (male) and dii (female), across two Hugging Face
collections:
[synthetic datasets](https://huggingface.co/collections/TigreGotico/synthetic-tts-datasets)
and [voice-converted datasets](https://huggingface.co/collections/TigreGotico/tts-voice-converted-datasets).
Most language rows link a `TigreGotico` dataset; Kabyle links a dataset
published by [fdemelo](https://huggingface.co/fdemelo). The candidate real-speech
corpora and donor TTS engines behind each language are listed in
[`docs/tts-data-sources.md`](docs/tts-data-sources.md); French and Italian have
no dedicated section yet (only their regional varieties do), so those two rows
link the page itself rather than a section.

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

Wall time is the measured `SMOKE=True` run (`-p SMOKE True -p N_SAMPLES 4 -p
EPOCHS 1`, CPU only, one fresh `uv` venv per notebook, `papermill
--log-output`). A full-size run's time depends on dataset size, epoch count
and hardware; no full-run number is stated here because none was measured.

| Notebook | Task | Hardware | Wall time (smoke) | CI |
|---|---|---|---|---|
| [`train_vits.ipynb`](notebooks/train_vits.ipynb) | WP3: TTS model training & export | GPU (T4 or better) for a full run | 47 s | executed |
| [`asr2tts.ipynb`](notebooks/asr2tts.ipynb) | WP3: Hybrid low-resource TTS dataset pipeline | CPU (`onnxruntime`) | 117 s | executed |
| [`tts_dataset_gen.ipynb`](notebooks/tts_dataset_gen.ipynb) | WP3: TTS dataset generation, prompts and donor synthesis | CPU | 6 s | executed |
| [`tts_measure.ipynb`](notebooks/tts_measure.ipynb) | WP3: TTS dataset measurement | CPU (GPU optional) | 29 s | executed |
| [`tts_voice_convert.ipynb`](notebooks/tts_voice_convert.ipynb) | WP3: TTS voice conversion | CPU (GPU optional) | 73 s | executed |
| [`tts_enhance.ipynb`](notebooks/tts_enhance.ipynb) | WP3: TTS dataset enhancement | CPU (GPU optional) | 10 s | executed |
| [`tts_corpus_ingest.ipynb`](notebooks/tts_corpus_ingest.ipynb) | WP3: TTS dataset corpus ingest | CPU | 3 s | executed |
| [`tts_select.ipynb`](notebooks/tts_select.ipynb) | WP3: TTS dataset selection | CPU | 2 s | executed |
| [`tts_publish.ipynb`](notebooks/tts_publish.ipynb) | WP3: TTS dataset publish | CPU | 6 s | executed |
| [`kaggle_quickstart_ww.ipynb`](notebooks/kaggle_quickstart_ww.ipynb) | WP2: Wake word model training (Kaggle) | GPU (T4 or better) for a full run | 30 s | executed |
| [`tts2ww_full_pipeline.ipynb`](notebooks/tts2ww_full_pipeline.ipynb) | WP2: Wake word dataset generation and augmentation (full pipeline) | CPU (GPU optional) | 12 s | executed |
| [`ovos_intent_classifier_monolingual.ipynb`](notebooks/ovos_intent_classifier_monolingual.ipynb) | WP4: Intent classification (monolingual) | CPU; GPU recommended for a full run | 19 s | executed |
| [`ovos_intent_classifier_multilingual.ipynb`](notebooks/ovos_intent_classifier_multilingual.ipynb) | WP4: Intent classification (multilingual) | CPU; GPU recommended for a full run | 16 s | executed |
| [`ovos_intent_benchmark.ipynb`](notebooks/ovos_intent_benchmark.ipynb) | WP4: Intent classification benchmark | CPU; GPU recommended for a full run | 18 s | executed |
| [`interop_mcp_utcp_clients.ipynb`](notebooks/interop_mcp_utcp_clients.ipynb) | WP1: MCP/UTCP interoperability | CPU | 9 s | executed |
| [`speaker_verification.ipynb`](notebooks/speaker_verification.ipynb) | WP2: Speaker verification & enrollment | CPU | 8 s | executed |
| [`bus_message_validation.ipynb`](notebooks/bus_message_validation.ipynb) | WP1: Bus message schema validation | CPU | 2 s | executed |
| [`arena_prediction_runner.ipynb`](notebooks/arena_prediction_runner.ipynb) | WP4: STT arena prediction slice | CPU | 8 s | executed |
| [`synthetic_ww_dataset.ipynb`](notebooks/synthetic_ww_dataset.ipynb) | WP2: Synthetic wake-word mini-dataset | CPU | 7 s | executed |

The `smoke` CI job runs every notebook in `notebooks/` on every push, with
`SMOKE=True` and a handful of samples; the matrix is discovered from the
directory listing, so a new notebook without a matching
`requirements/<stem>.txt` fails CI rather than sitting outside it silently.
A green smoke run proves that the notebook runs from top to bottom at a small
size; it does not prove that a full-size run finishes. papermill raises on a
cell error, so a smoke job fails the pipeline for every notebook, with no
exception. A separate `compile` job compiles every code cell of every
notebook under Python 3.11 and 3.12, magics stripped, which catches a
`SyntaxError` that `nbformat.validate` (JSON-schema only) would not. The
[Actions tab](../../actions) shows the result of each job.

---

## Running locally

Python 3.11 and 3.12 are supported, matching what CI tests: every
`requirements/*.txt` resolves on both, and the `compile` job compiles every
notebook under both. `lint` runs on 3.11 and `smoke` runs on 3.12; neither
choice is load-bearing, since resolution and compilation are already
proven on both versions (a notebook is executed by CI on 3.12 only). Python 3.14 is not supported:
`nest_asyncio`, which several notebooks use to run `edge-tts` inside a
Jupyter kernel's already-running event loop, raises `RuntimeError: Timeout
should be used inside a task` there. Pass `--python 3.12` (or `3.11`) when
creating the venv rather than taking the system interpreter.

Three system packages are needed: `ffmpeg` (audio decoding), `sox` (used by
`ovos-tts-plugin-beepspeak` in `interop_mcp_utcp_clients`) and `espeak-ng`
(phonemisation in `train_vits`). On Debian or Ubuntu, including Colab and
Kaggle: `sudo apt-get install ffmpeg sox espeak-ng`. `train_vits` installs
`espeak-ng` itself with `apt-get` when it is missing; on other distributions,
install it with the system package manager first.

Every notebook has its own `requirements/<notebook-stem>.txt`. Install with
[uv](https://docs.astral.sh/uv/) and run the smoke path with
[papermill](https://papermill.readthedocs.io/):

```bash
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install --prerelease=allow pip jupyter papermill ipykernel nest_asyncio
uv pip install --prerelease=allow -r requirements/speaker_verification.txt

papermill notebooks/speaker_verification.ipynb /tmp/out.ipynb \
    -p SMOKE True -p N_SAMPLES 4 -p EPOCHS 1
```

Drop `-p SMOKE True ...` to run the notebook at full size. A full `train_vits`
or `kaggle_quickstart_ww` run needs a GPU; the three `ovos_intent_*` notebooks
can train a full model on CPU, but a GPU is recommended; every other notebook
runs on CPU, and the onnxruntime-based steps use a GPU when an onnxruntime GPU
build is installed. See `CONTRIBUTING.md` for the
header template and the `SMOKE`/`N_SAMPLES`/`EPOCHS`/`MODEL_ID` parameter
cell every notebook carries.

---

## CI

`.github/workflows/ci.yml` runs four jobs on every push:

- **`lint`** — validates notebook structure with `nbformat` and verifies that
  every notebook except the evidence allowlist
  (`arena_prediction_runner`, `bus_message_validation`,
  `interop_mcp_utcp_clients`, `speaker_verification`) has its outputs
  stripped (`nbstripout --verify`).
- **`compile`** — compiles every code cell of every notebook under Python
  3.11 and 3.12, with `!`/`%` magic lines (and their backslash continuations)
  stripped to blank statements first, so a real `SyntaxError` fails CI.
- **`discover`** — lists `notebooks/*.ipynb` for the smoke matrix and fails
  if a notebook has no `requirements/<stem>.txt`.
- **`smoke`** — a matrix discovered from `notebooks/*.ipynb`, one job per
  notebook. Each job installs that notebook's `requirements/<stem>.txt` with
  `uv` on a CPU runner and runs `papermill --log-output ... -p SMOKE True
  -p N_SAMPLES 4 -p EPOCHS 1`; papermill raises on a cell error, so every job
  can fail, with no exception.

---

## Repository structure

```
notebooks/
  *.ipynb          - all deliverable notebooks
docs/
  *.md             - pipeline, manifest, registry and data-source reference
registry/
  tts.yaml         - admitted donors, corpora and judges per language
requirements/
  *.txt            - one file per notebook, PyPI names only
.github/workflows/
  ci.yml
CONTRIBUTING.md    - header/footer template, dependency rules, local smoke run
.pre-commit-config.yaml
LICENSE            - Apache License 2.0
```
