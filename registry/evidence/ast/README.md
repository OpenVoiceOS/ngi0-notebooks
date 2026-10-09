# Asturian (ast): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_ast_miro_unicode` | 3.058 | 2.759 | n/a |
| `OpenVoiceOS/phoonnx_ast_dii_unicode` | 3.136 | 2.677 | n/a |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `TigreGotico/tts_vc_mcv-scripted-v23.0_ast_miro` at revision `df1f19ae0325dd711c92d48b371fa5d012f56b06`, file metadata.csv. `make_sentences.py` selects the sentences with a fixed seed.

This set is the voice's own training corpus, not held out, so scores can be higher than on unseen text; the comparison between voices of the same language is on identical sentences.

## Judge

No non-Whisper recogniser in the onnx-asr model list covers this language, so the voices have naturalness scores only (`cer_median` is null in the registry).

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_ast_miro_unicode` at revision `80c19977e400ff6c8a61a42f097c6cbddd7502e4` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_ast_dii_unicode` at revision `5a8d91080966ac3f5da00077f50d641db2191bd0` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
