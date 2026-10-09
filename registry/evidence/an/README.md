# Aragonese (an): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_an_miro_unicode` | 3.446 | 3.028 | n/a |
| `OpenVoiceOS/phoonnx_an_dii_unicode` | 3.558 | 2.919 | n/a |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `OpenVoiceOS/ovos-intents` at revision `23ffd44a229198b041f57067c6828a1f8e75b760`, file an/train_templates.jsonl. `make_sentences.py` selects the sentences with a fixed seed.

## Judge

No non-Whisper recogniser in the onnx-asr model list covers this language, so the voices have naturalness scores only (`cer_median` is null in the registry).

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_an_miro_unicode` at revision `31cf76cbde9e3967ebd02586a6721362f647077e` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_an_dii_unicode` at revision `4c3fd73467175f338c325cbaa710f004c1fe008c` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
