# Portuguese, European (pt-PT): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_pt-PT_miro_tugaphone` | 3.446 | 3.002 | 0.319 |
| `OpenVoiceOS/phoonnx_pt-PT_dii_tugaphone` | 3.763 | 3.410 | 0.248 |
| `OpenVoiceOS/phoonnx_pt-PT_miro_unicode` | 3.569 | 3.231 | 0.168 |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `OpenVoiceOS/ovos-intents` at revision `23ffd44a229198b041f57067c6828a1f8e75b760`, file pt-PT/test.jsonl. `make_sentences.py` selects the sentences with a fixed seed.

## Judge

The round trip used `ovos-stt-plugin-onnx-asr` with the model `OpenVoiceOS/yuriyvnv-parakeet-tdt-0.6b-pt-onnx` (revision `7d4181938f5d0890ac9731cca3c0336b92913b57`). It is not Whisper. CER is the character error rate of the recogniser's transcript against the sentence, after NFC, case folding and punctuation removal. The recogniser has not been checked against real recordings of this language here, and the sentences are short commands, so read CER as a comparison between the voices above and not as an absolute error rate.

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_pt-PT_miro_tugaphone` at revision `0de46f57d00587e027e8c196b7170a268bf424b1` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_pt-PT_dii_tugaphone` at revision `9a9d9fbb5b666d089caad01626d220fb174cdc2c` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_pt-PT_miro_unicode` at revision `022c02388e552e2827ff31745cf1461a7ddd4f37` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
