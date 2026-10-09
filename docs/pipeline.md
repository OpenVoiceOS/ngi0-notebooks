# TTS dataset pipeline

The TTS dataset notebooks form a chain. Each notebook reads a manifest, does one job and writes a
manifest. A notebook runs alone when you give it an input manifest. It does not need the notebook
before it to run in the same session. The manifest format is in [manifest.md](manifest.md).

Each clip is measured once, and the scores stay in the manifest. Selection is a separate step. It
reads the scores and writes a list of the clips it keeps. It never deletes or moves audio. So a
trainer can make a different selection from the same manifest without scoring again.

The donor for synthesis is [OmniVoice](https://github.com/k2-fsa/OmniVoice) unless `DONOR_MODEL`
names another: a voice id from the phoonnx catalog or an OVOS TTS plugin. OmniVoice speaks 646
languages, runs on a GPU and fixes one voice per run, because a training set needs one speaker.
A language OmniVoice does not speak stops the synthesis notebook with a message that names
`DONOR_MODEL`. The notebook keeps no list of models. The recogniser used for measurement comes
from `STT_MODULE`, an explicit OVOS STT plugin name.

## The chain

| Step | Notebook | Reads | Writes |
|---|---|---|---|
| 1-2a | [`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb): prompts and donor synthesis | text sources, and a voice (`REF_AUDIO` to clone, `VOICE_PROMPT` to design, or the default design) or a `DONOR_MODEL` | manifest with audio |
| 2b | [`tts_corpus_ingest.ipynb`](../notebooks/tts_corpus_ingest.ipynb): corpus ingest | a real speech corpus | manifest with audio |
| 3 | [`tts_enhance.ipynb`](../notebooks/tts_enhance.ipynb): enhancement | manifest with audio | manifest with enhanced audio; each row keeps its parent |
| 4 | [`tts_measure.ipynb`](../notebooks/tts_measure.ipynb): measure | any manifest with audio | the same manifest with scores added |
| 5 | [`tts_select.ipynb`](../notebooks/tts_select.ipynb): select | manifest with scores, and selection rules | selection file |
| 6 | [`tts_voice_convert.ipynb`](../notebooks/tts_voice_convert.ipynb): voice conversion | manifest (or a selection) and one reference clip per identity | one manifest per identity; each row keeps its parent |
| 7 | [`tts_measure.ipynb`](../notebooks/tts_measure.ipynb): measure | converted manifest | converted manifest with scores added |
| 8 | [`tts_select.ipynb`](../notebooks/tts_select.ipynb): select | converted manifest with scores | selection file for training |
| 9 | [`tts_publish.ipynb`](../notebooks/tts_publish.ipynb): publish | manifest and selection | Hugging Face dataset: audio, `metadata.csv` and the full manifest |
| 10 | [`train_vits.ipynb`](../notebooks/train_vits.ipynb) | published dataset (`metadata.csv`) | TTS model |

Steps 5 and 8 are optional. When you skip step 5, voice conversion takes every row.

## Voice identities

The published datasets carry two voice identities: miro (male) and dii (female). Voice conversion
turns source speech into each identity with [voiceclonnx](https://github.com/TigreGotico/voiceclonnx).
The source speech is either a donor TTS rendering or a real corpus recording. After conversion the
source speaker's timbre is gone. What stays is the pronunciation, the dialect and the prosody of the
source. For this reason, a donor or a corpus is chosen for its linguistic accuracy.

## Instruments

| Measurement | Package |
|---|---|
| Naturalness (UTMOS, DNSMOS, NISQA) | [speechonnxmetrics](https://pypi.org/project/speechonnxmetrics/) |
| Speaker similarity | [speakeronnx](https://pypi.org/project/speakeronnx/) |
| Recogniser round trip | one OVOS STT plugin, named explicitly via `STT_MODULE` |
| Donor synthesis | [OmniVoice](https://pypi.org/project/omnivoice/); or a [phoonnx](https://pypi.org/project/phoonnx/) catalog voice or an OVOS TTS plugin, named in `DONOR_MODEL` |
| Voice conversion | [voiceclonnx](https://pypi.org/project/voiceclonnx/) |

## Hardware

Every model in the chain runs on onnxruntime, except: the donor in step 1-2a (OmniVoice runs in
PyTorch fp16 on a GPU; a `DONOR_MODEL` plugin runs on whatever backend that plugin uses, and only
that step's optional super-resolution stage is onnxruntime); the recogniser in steps 4 and 7 (`STT_MODULE` names an OVOS
STT plugin, and the default, vosk, runs on Kaldi, not onnxruntime); and step 10 (`train_vits.ipynb`
trains and exports with phoonnx and PyTorch in a separate virtual environment; the ONNX export is
for inference elsewhere, not for this notebook's own training run).

The default install is CPU-only. For an NVIDIA card, install
`onnxruntime-gpu`. For an AMD card, install AMD's onnxruntime ROCm or MIGraphX build. Each notebook
takes the execution providers from the `ONNX_PROVIDERS` variable, and `auto` selects the best
provider that the installed build offers.
