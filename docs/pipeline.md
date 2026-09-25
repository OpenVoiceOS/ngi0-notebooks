# TTS dataset pipeline

The TTS dataset notebooks form a chain. Each notebook reads a manifest, does one job and writes a
manifest. A notebook runs alone when you give it an input manifest. It does not need the notebook
before it to run in the same session. The manifest format is in [manifest.md](manifest.md).

Each clip is measured once, and the scores stay in the manifest. Selection is a separate step. It
reads the scores and writes a list of the clips it keeps. It never deletes or moves audio. So a
trainer can make a different selection from the same manifest without scoring again.

The donor TTS and the recognisers for a language come from the registry. The registry is described
in [registry.md](registry.md). A language that has no registry entry has no donor, and the
synthesis notebook stops with a message.

## The chain

| Step | Notebook | Reads | Writes |
|---|---|---|---|
| 1-2a | [`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb): prompts and donor synthesis | text sources and the registry's donor | manifest with audio |
| 2b | Corpus ingest | a real speech corpus | manifest with audio |
| 3 | Enhancement | manifest with audio | manifest with enhanced audio; each row keeps its parent |
| 4 | Measure | any manifest with audio | the same manifest with scores added |
| 5 | Select | manifest with scores, and selection rules | selection file |
| 6 | Voice conversion | manifest (or a selection) and one reference clip per identity | one manifest per identity; each row keeps its parent |
| 7 | Measure | converted manifest | converted manifest with scores added |
| 8 | Select | converted manifest with scores | selection file for training |
| 9 | [`tts_publish.ipynb`](../notebooks/tts_publish.ipynb): publish | manifest and selection | Hugging Face dataset: audio, `metadata.csv` and the full manifest |
| 10 | [`train_vits.ipynb`](../notebooks/train_vits.ipynb) | published dataset and a selection | TTS model |

Steps 5 and 8 are optional. When you skip step 5, voice conversion takes every row.

## Voice identities

The published datasets carry two voice identities: miro (male) and dii (female). Voice conversion
turns source speech into each identity with [voiceclonnx](https://github.com/TigreGotico/voiceclonnx).
The source speech is either a donor TTS rendering or a real corpus recording. After conversion the
source speaker's timbre is gone. What stays is the pronunciation, the dialect and the prosody of the
source. For this reason, the registry admits a donor or a corpus on its linguistic accuracy.

## Instruments

| Measurement | Package |
|---|---|
| Naturalness (UTMOS, DNSMOS, NISQA) | [speechonnxmetrics](https://pypi.org/project/speechonnxmetrics/) |
| Speaker similarity | [speakeronnx](https://pypi.org/project/speakeronnx/) |
| Recogniser round trip | OVOS STT plugins, combined with [ovos-stt-plugin-rover](https://pypi.org/project/ovos-stt-plugin-rover/) |
| Donor synthesis | OVOS TTS plugins, [phoonnx](https://pypi.org/project/phoonnx/) voices where the registry admits one |
| Voice conversion | [voiceclonnx](https://pypi.org/project/voiceclonnx/) |

## Hardware

Every model in the chain runs on onnxruntime, except a donor plugin itself in step 1-2a: it runs on
whatever backend that OVOS TTS plugin uses, onnxruntime or otherwise, and only that step's optional
super-resolution stage is onnxruntime. The default install is CPU-only. For an NVIDIA card, install
`onnxruntime-gpu`. For an AMD card, install AMD's onnxruntime ROCm or MIGraphX build. Each notebook
takes the execution providers from the `ONNX_PROVIDERS` variable, and `auto` selects the best
provider that the installed build offers.
