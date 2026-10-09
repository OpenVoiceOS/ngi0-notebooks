# Arabic (ar): phoonnx voices measured as donor candidates

The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and `tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.

| Voice | UTMOS median | UTMOS p10 | CER median |
|---|---|---|---|
| `OpenVoiceOS/phoonnx_ar_dii_espeak` | 3.027 | 2.587 | 0.022 |
| `OpenVoiceOS/phoonnx_ar_miro_espeak_V2` | 3.134 | 2.796 | 0.000 |

Every voice rendered the same 24 sentences. The listening check by a native speaker is pending, so no voice is admitted as a donor.

## Sentence set

Source: `TigreGotico/tts-train-synthetic-miro_ar-SA` at revision `1693cdc0da1c9c47c82ae09e6447321ae67c8195`, file metadata.csv. `make_sentences.py` selects the sentences with a fixed seed.

This set is the voice's own training corpus, not held out, so scores can be higher than on unseen text; the comparison between voices of the same language is on identical sentences.

## Judge

The round trip used `ovos-stt-plugin-onnx-asr` with the model `OpenVoiceOS/stt_ar_fastconformer_hybrid_large_pcd_v1.0_onnx` (revision `c5f78db4d5a8da706ab74cad73481c18b8d736b9`). It is not Whisper. CER is the character error rate of the recogniser's transcript against the sentence, after NFC, case folding and punctuation removal. The recogniser has not been checked against real recordings of this language here, and the sentences are short commands, so read CER as a comparison between the voices above and not as an absolute error rate.

## Voice revisions and tools

- `OpenVoiceOS/phoonnx_ar_dii_espeak` at revision `a5b2c6bc0d1a7a04d951e6352d55c1324f8e6bc5` (head of the main branch when measured)
- `OpenVoiceOS/phoonnx_ar_miro_espeak_V2` at revision `8c5783a11d450ffad2ed99fc7c6dc8d6c8f86ccb` (head of the main branch when measured)

Tools: phoonnx 1.93.1a2, ovos-plugin-manager 2.12.5a1, ovos-stt-plugin-onnx-asr 0.6.1a2, onnx-asr 0.12.0, speechonnxmetrics 0.0.2a3, speakeronnx 0.0.2a3, onnxruntime 1.30.0.

UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the wrapper script is `registry/evidence/run_voice.sh`.
