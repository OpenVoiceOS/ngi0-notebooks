# Wake-word benchmark results

This page reports one full run of [`ww_benchmark.ipynb`](ww_benchmark.ipynb): 73 wake-word fighters from 8 OpenVoiceOS plugins, run on 27 test sets of the [OVOS plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena). Each fighter ran only on the test sets of its own phrase. The run made 24,180 result rows, one per clip. The rows are published in the arena's Hugging Face datasets, `OpenVoiceOS/ovos-wake-word-bench-<test set>`, and the arena's boards are built from them. The full table is [`ww_benchmark_results.csv`](ww_benchmark_results.csv).

[Benchmarks](../docs/benchmarks.md) explains the test sets and the numbers.

## What the run shows

On people's voices, the trained models make the fewest mistakes. On the `picovoice` sets of "alexa", "computer" and "jarvis", `wakeforge`, `efficientword-net` and `openwakeword` get 2.3% of the clips wrong or fewer.

The zero-shot fighter needs no recordings and no training, and it comes close. `wakeforge-zeroshot` gets only the phrase as phones. On the same three `picovoice` sets it gets 1.0% to 6.0% of the clips wrong. On 12 test sets it is the only fighter apart from `vosk`. On the three `picovoice` phrases that no trained model covers ("smart mirror", "snowboy", "view glass"), it misses 10% to 22% of the clips with the phrase.

The fighters rarely wake by mistake. 69 of the 83 results have no false accept at all. The exception is `microwakeword`: on the synthetic "hey jarvis" set, its three fighters wake on 22% to 43% of the clips without the phrase.

Two plugins miss most clips with the phrase. `vosk` misses 60% to 100% of them on every set. `precise-onnx` misses 98% on `picovoice-computer` and 91% on `picovoice-jarvis`, and 36% to 37% on the synthetic "hey mycroft" set.

The community recordings are the hardest test. On `community-computer`, `community-amelia`, `community-athena` and `community-hey-floyd`, the zero-shot fighter misses 67% to 94% of the clips with the phrase. The trained `wakeforge` models for "hey chatterbox", "hey floyd", "hey scout" and "hey ziggy" miss 17% or fewer, and `wakeforge-hey-k9` misses 56.5% of the 46 clips with its phrase. `wakeforge-computer` misses 82% on `community-computer`, but only 7% on `picovoice-computer`.

## How to read the numbers

Each result has 100 clips with the phrase and 200 clips without it, unless the test set has fewer clips with the phrase. The **error rate** counts both kinds, so a fighter that never wakes still scores 33% wrong. Read the false rejects and the false accepts, not only the error rate.

| Number | Meaning |
|---|---|
| False rejects % | Clips with the phrase that did not wake the fighter |
| False accepts % | Clips without the phrase that woke the fighter. One clip is 0.5% |
| Median ms | Median time to decide on one clip, on a laptop CPU |

## People's voices: the `picovoice` sets

| Test set | Fighter | Error % | False rejects % | False accepts % | Median ms |
|---|---|---|---|---|---|
| `picovoice-alexa` | `efficientword-net-alexa` | 0.7 | 2.0 | 0.0 | 188 |
| `picovoice-alexa` | `wakeforge-alexa` | 0.7 | 2.0 | 0.0 | 43 |
| `picovoice-alexa` | `openwakeword-alexa` | 1.0 | 2.0 | 0.5 | 156 |
| `picovoice-alexa` | `wakeforge-zeroshot-alexa` | 1.0 | 3.0 | 0.0 | 155 |
| `picovoice-alexa` | `local-wake-alexa` | 13.0 | 39.0 | 0.0 | 15 |
| `picovoice-alexa` | `vosk-ww-alexa` | 26.7 | 80.0 | 0.0 | 90 |
| `picovoice-computer` | `efficientword-net-computer` | 2.0 | 6.0 | 0.0 | 286 |
| `picovoice-computer` | `wakeforge-computer` | 2.3 | 7.0 | 0.0 | 275 |
| `picovoice-computer` | `wakeforge-zeroshot-computer` | 6.0 | 18.0 | 0.0 | 198 |
| `picovoice-computer` | `vosk-ww-computer` | 23.3 | 70.0 | 0.0 | 106 |
| `picovoice-computer` | `precise-onnx-computer` | 32.7 | 98.0 | 0.0 | 44 |
| `picovoice-jarvis` | `wakeforge-jarvis` | 0.0 | 0.0 | 0.0 | 52 |
| `picovoice-jarvis` | `wakeforge-zeroshot-jarvis` | 4.0 | 12.0 | 0.0 | 204 |
| `picovoice-jarvis` | `vosk-ww-jarvis` | 20.0 | 60.0 | 0.0 | 82 |
| `picovoice-jarvis` | `precise-onnx-jarvis` | 30.3 | 91.0 | 0.0 | 41 |
| `picovoice-smart-mirror` | `wakeforge-zeroshot-smart-mirror` | 5.3 | 16.0 | 0.0 | 221 |
| `picovoice-smart-mirror` | `vosk-ww-smart-mirror` | 32.7 | 98.0 | 0.0 | 116 |
| `picovoice-snowboy` | `wakeforge-zeroshot-snowboy` | 7.3 | 22.0 | 0.0 | 196 |
| `picovoice-snowboy` | `vosk-ww-snowboy` | 29.7 | 89.0 | 0.0 | 104 |
| `picovoice-view-glass` | `wakeforge-zeroshot-view-glass` | 3.3 | 10.0 | 0.0 | 211 |
| `picovoice-view-glass` | `vosk-ww-view-glass` | 33.3 | 99.0 | 0.5 | 103 |

## Community recordings

| Test set | With phrase | Fighter | Error % | False rejects % | False accepts % |
|---|---|---|---|---|---|
| `community-amelia` | 100 | `vosk-ww-amelia` | 22.7 | 67.0 | 0.5 |
| `community-amelia` | 100 | `wakeforge-zeroshot-amelia` | 31.3 | 94.0 | 0.0 |
| `community-athena` | 100 | `wakeforge-zeroshot-athena` | 22.3 | 67.0 | 0.0 |
| `community-athena` | 100 | `vosk-ww-athena` | 28.7 | 86.0 | 0.0 |
| `community-computer` | 100 | `efficientword-net-computer` | 5.0 | 15.0 | 0.0 |
| `community-computer` | 100 | `vosk-ww-computer` | 23.0 | 69.0 | 0.0 |
| `community-computer` | 100 | `wakeforge-computer` | 27.3 | 82.0 | 0.0 |
| `community-computer` | 100 | `wakeforge-zeroshot-computer` | 30.0 | 90.0 | 0.0 |
| `community-ey-ordenador` | 48 | `vosk-ww-ey-ordenador` | 19.4 | 100.0 | 0.0 |
| `community-hey-chatterbox` | 100 | `wakeforge-hey-chatterbox` | 5.7 | 17.0 | 0.0 |
| `community-hey-chatterbox` | 100 | `wakeforge-zeroshot-hey-chatterbox` | 17.0 | 51.0 | 0.0 |
| `community-hey-chatterbox` | 100 | `vosk-ww-hey-chatterbox` | 33.3 | 100.0 | 0.0 |
| `community-hey-floyd` | 96 | `wakeforge-hey-floyd` | 3.0 | 9.4 | 0.0 |
| `community-hey-floyd` | 96 | `wakeforge-zeroshot-hey-floyd` | 25.3 | 78.1 | 0.0 |
| `community-hey-floyd` | 96 | `vosk-ww-hey-floyd` | 31.4 | 96.9 | 0.0 |
| `community-hey-k9` | 46 | `wakeforge-zeroshot-hey-k9` | 9.8 | 52.2 | 0.0 |
| `community-hey-k9` | 46 | `wakeforge-hey-k9` | 10.6 | 56.5 | 0.0 |
| `community-hey-k9` | 46 | `vosk-ww-hey-k9` | 18.7 | 100.0 | 0.0 |
| `community-hey-savant` | 100 | `wakeforge-zeroshot-hey-savant` | 8.0 | 24.0 | 0.0 |
| `community-hey-savant` | 100 | `vosk-ww-hey-savant` | 33.0 | 99.0 | 0.0 |
| `community-hey-scout` | 34 | `wakeforge-zeroshot-hey-scout` | 0.0 | 0.0 | 0.0 |
| `community-hey-scout` | 34 | `wakeforge-hey-scout` | 0.9 | 5.9 | 0.0 |
| `community-hey-scout` | 34 | `vosk-ww-hey-scout` | 14.5 | 100.0 | 0.0 |
| `community-hey-ziggy` | 26 | `wakeforge-hey-ziggy` | 0.9 | 7.7 | 0.0 |
| `community-hey-ziggy` | 26 | `wakeforge-zeroshot-hey-ziggy` | 1.8 | 15.4 | 0.0 |
| `community-hey-ziggy` | 26 | `local-wake-hey-ziggy` | 5.3 | 46.2 | 0.0 |
| `community-hey-ziggy` | 26 | `vosk-ww-hey-ziggy` | 11.1 | 96.2 | 0.0 |

## Synthetic voices

Synthetic voices have no room echo and no microphone, so these sets are easier than a home. The trained `wakeforge` models learned from synthetic clips of their phrase, so they do not run on these sets. The table shows the best fighter on each set and the fighters of the other plugins.

| Test set | Fighter | Error % | False rejects % | False accepts % |
|---|---|---|---|---|
| `synthetic-wakewords-alexa` | `efficientword-net-alexa` | 0.3 | 1.0 | 0.0 |
| `synthetic-wakewords-alexa` | `openwakeword-alexa` | 0.7 | 1.0 | 0.5 |
| `synthetic-wakewords-alexa` | `wakeforge-zeroshot-alexa` | 8.3 | 25.0 | 0.0 |
| `synthetic-wakewords-hey_jarvis` | `openwakeword-hey-jarvis` | 0.3 | 1.0 | 0.0 |
| `synthetic-wakewords-hey_jarvis` | `wakeforge-zeroshot-hey-jarvis` | 1.7 | 5.0 | 0.0 |
| `synthetic-wakewords-hey_jarvis` | `microwakeword-hey-jarvis-silero` | 15.0 | 0.0 | 22.5 |
| `synthetic-wakewords-hey_jarvis` | `microwakeword-hey-jarvis` | 29.0 | 1.0 | 43.0 |
| `synthetic-wakewords-hey_mycroft` | `wakeforge-zeroshot-hey-mycroft` | 1.0 | 3.0 | 0.0 |
| `synthetic-wakewords-hey_mycroft` | `openwakeword-hey-mycroft-silero` | 1.7 | 5.0 | 0.0 |
| `synthetic-wakewords-hey_mycroft` | `openwakeword-hey-mycroft` | 2.0 | 5.0 | 0.5 |
| `synthetic-wakewords-hey_mycroft` | `precise-onnx-hey-mycroft` | 17.0 | 37.0 | 7.0 |
| `synthetic-wakewords-hey_robin` | `precise-onnx-hey-robin` | 0.0 | 0.0 | 0.0 |
| `synthetic-wakewords-hey_robin` | `wakeforge-zeroshot-hey-robin` | 1.3 | 4.0 | 0.0 |
| `synthetic-wakewords-hey_marvin` | `wakeforge-zeroshot-hey-marvin` | 1.0 | 3.0 | 0.0 |
| `synthetic-wakewords-hey_marvin` | `precise-onnx-marvin` | 29.3 | 87.0 | 0.5 |
| `synthetic-wakewords-hey_computer` | `wakeforge-zeroshot-hey-computer` | 1.0 | 3.0 | 0.0 |
| `synthetic-wakewords-hey_ziggy` | `wakeforge-zeroshot-hey-ziggy` | 2.0 | 6.0 | 0.0 |
| `synthetic-wakewords-hey_andromeda` | `wakeforge-zeroshot-hey-andromeda` | 2.7 | 8.0 | 0.0 |
| `synthetic-wakewords-hey_neon` | `wakeforge-zeroshot-hey-neon` | 4.3 | 13.0 | 0.0 |
| `synthetic-wakewords-wake_up` | `wakeforge-zeroshot-wake-up` | 4.3 | 13.0 | 0.0 |
| `synthetic-wakewords-hey_eggbert` | `wakeforge-zeroshot-hey-eggbert` | 6.0 | 18.0 | 0.0 |

`vosk` misses 71% to 100% of the clips with the phrase on every synthetic set. The CSV has every row.

## The new fighters

This run added three plugins to the arena as 27 fighters ([ovos-plugin-arena#228](https://github.com/OpenVoiceOS/ovos-plugin-arena/pull/228)):

| Plugin | Fighters | How it knows the phrase |
|---|---|---|
| `ovos-ww-plugin-wakeforge-zeroshot` | 23, one per English phrase with a test set | The phrase as phones from eSpeak NG. "Hey mycroft" has hand-written phones, because eSpeak NG reads the name with the vowel of "mick" |
| `ovos-ww-plugin-efficientword-net` | "alexa", "computer" | Its own bundled recordings |
| `ovos-ww-plugin-local-wake` | "alexa", "hey ziggy" | Four synthetic clips of the phrase. It does not run on the set the clips come from |

`local-wake` misses 39% to 46% of the clips with the phrase. A "computer" fighter with references from the community recordings woke on every clip, because those recordings hold seconds of room sound around the word, so the arena does not list it.

## The run

| Item | Value |
|---|---|
| Arena commit | `270629d714f66e2c32a3dcbf70f8acdaae707231` |
| Test set revisions | `picovoice-*` `f047dd73`, `community-*` `1a3ad631`, `synthetic-wakewords-*` `73211e16` |
| Clips | 100 with the phrase per set, 100 without it from the set's own pool, 100 from the Multilingual Spoken Words pool |
| Plugins | `ovos-ww-plugin-wakeforge` 0.18.0a1, `-efficientword-net` 0.0.1a2, `-local-wake` 0.0.1a2, `-openwakeword` 0.4.6, `-microwakeword` 0.0.1a4, `-precise-onnx` 0.1.2a1, `-vosk` 0.1.11a3; `ovoscope` 1.11.3a1, `ovos-plugin-manager` 2.12.5a1, `onnxruntime` 1.31.0 |
| Machine | One laptop, Intel Core i9-11900H, CPU only, three notebook runs at the same time with 4 GB of memory each |
| Time | 58 minutes for the 83 fighter runs |
| Checks | The notebook's own count of mistakes agrees with the arena's score on all 83 results. All 83 uploaded files hold the same clips as the local rows |

The arena's boards for these sets also hold 512 older published rows, which the run kept. The tables on this page come from this run's rows only. The boards at arena commit `72a05099` hold all 83 results. 47 of them equal the numbers on this page, and the other 36 differ only by the older rows.

## Limits

- No result has enough audio without the phrase for a count of false wake-ups per hour. A clip is about one second long.
- The fighters ran only on the test sets of their own phrase.
- `ovos-ww-plugin-pocketsphinx` did not run, because its version on PyPI does not build. `ovos-ww-plugin-wakewordlab` did not run, because it is not on PyPI.
- The rows record the machine as `gpu`, because `onnxruntime` lists its Azure provider on every machine. The laptop has no GPU.
- `community-ey-ordenador` is the only test set that is not English, and only `vosk` has a fighter for it.

## Run it again

Open [`ww_benchmark.ipynb`](ww_benchmark.ipynb) and set these values in the Settings cell, or give them as environment variables:

```python
DATASETS = ["picovoice-alexa", "picovoice-computer", ...]   # the 27 sets in the CSV
MAX_PER_CLASS = 100
ARENA_REF = "270629d714f66e2c32a3dcbf70f8acdaae707231"   # the notebook default, 72a05099, has the same code
```

One run of all 27 sets on one CPU takes about three hours. Three runs with different `DATASETS` and `OUTPUT_DIR` can share one machine.

---

[Benchmarks](../docs/benchmarks.md) · [`ww_benchmark.ipynb`](ww_benchmark.ipynb) · [`ww_leaderboard.ipynb`](ww_leaderboard.ipynb)
