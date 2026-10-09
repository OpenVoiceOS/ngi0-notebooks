# Western Frisian (fy-NL): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_fy-NL_miro_unicode` | 3.158 | 2.949 | n/a |
| `OpenVoiceOS/phoonnx_fy-NL_dii_unicode` | 3.243 | 2.898 | n/a |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `TigreGotico/tts-vc-mcv-scripted-v24.0-fy-nl-miro` at revision `ee6d8f60a9e3bdf906c1a4f9a86e64909a02aef5`, file metadata.csv. `make_sentences.py` selects the sentences with a fixed seed.

This set is the voice's own training corpus, not held out, so scores can be higher than on unseen text; the comparison between voices of the same language is on identical sentences.

## Judge

No non-Whisper recogniser in the onnx-asr model list covers this language, so the voices have naturalness scores only (`cer_median` is null in the registry).

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_fy-NL_miro_unicode` at revision `f1b0b1d9c26ecbed10545a935f4d9d685a4632f8` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_fy-NL_dii_unicode` at revision `b1e18fb73313979b0bf1a9837b7c9d33d0ab9fa5` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
