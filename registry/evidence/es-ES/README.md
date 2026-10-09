# Spanish, European (es-ES): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_es-ES_dii_espeak` | 3.541 | 3.006 | 0.036 |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `OpenVoiceOS/ovos-intents` at revision `23ffd44a229198b041f57067c6828a1f8e75b760`, file es-ES/test.jsonl. `make_sentences.py` selects the sentences with a fixed seed.

## Judge

The round trip used `ovos-stt-plugin-onnx-asr` with the model `OpenVoiceOS/stt_es_fastconformer_hybrid_large_pc_onnx` (revision `8d1aff0e061f8a681b5cb3a39670e6335647abdf`). It is not Whisper. CER is the character error rate of the recogniser's transcript against the sentence, after NFC, case folding and punctuation removal. The recogniser has not been checked against real recordings of this language here, and the sentences are short commands, so read CER as a comparison between the voices above and not as an absolute error rate.

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_es-ES_dii_espeak` at revision `626210a1d0247b358d2297bfadcef9d42194ecc7` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
