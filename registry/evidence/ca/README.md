# Catalan (ca): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_ca_miro_espeak` | 3.485 | 3.157 | 0.202 |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `OpenVoiceOS/ovos-intents` at revision `23ffd44a229198b041f57067c6828a1f8e75b760`, file ca-ES/test.jsonl. `make_sentences.py` selects the sentences with a fixed seed.

## Judge

The round trip used `ovos-stt-plugin-onnx-asr` with the model `OpenVoiceOS/nvidia-ca-conformer-transducer-large-onnx` (revision `4a6522eae6fb83ee34e4fef2780ae4bcdd5c6978`). It is not Whisper. CER is the character error rate of the recogniser's transcript against the sentence, after NFC, case folding and punctuation removal. The recogniser has not been checked against real recordings of this language here, and the sentences are short commands, so read CER as a comparison between the voices above and not as an absolute error rate.

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_ca_miro_espeak` at revision `66161af4e61601420198d37a416e8d228db8939e` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
