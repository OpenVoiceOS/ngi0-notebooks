#!/usr/bin/env bash
# Render one voice's sentence set with tts_dataset_gen and score it with tts_measure.
#
#   run_voice.sh <sentences-dir> <tts-lang> <voice-repo> <work-dir> [<stt-model> <stt-lang>]
#
# Run from the repository root inside a venv that holds the notebooks' requirements plus
# phoonnx and ovos-stt-plugin-onnx-asr. Without <stt-model> only UTMOS is scored.
set -euo pipefail
sent="$1"; lang="$2"; voice="$3"; work="$4"; stt_model="${5:-}"; stt_lang="${6:-}"
mkdir -p "$work"
export PROMPTS_FILE="$sent/sentences.txt" TTS_LANG="$lang" OUTPUT_DIR="$work" \
       DONOR_PLUGIN=ovos-tts-plugin-phoonnx DONOR_VOICE="$voice" PROMPTS_SOURCE_NAME=bakeoff
papermill --no-progress-bar notebooks/tts_dataset_gen.ipynb "$work/dataset_gen.out.ipynb" -p SMOKE False
export MANIFEST_PATH="$work/manifest.jsonl" QUALITY_FAMILIES=utmos
if [ -n "$stt_model" ]; then
  export STT_MODULE=ovos-stt-plugin-onnx-asr STT_LANG="$stt_lang"
  export STT_CONFIG="{\"model\": \"$stt_model\"}"
else
  export STT_MODULE=
fi
papermill --no-progress-bar notebooks/tts_measure.ipynb "$work/measure.out.ipynb" -p SMOKE False
