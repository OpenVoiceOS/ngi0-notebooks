<!-- For AI agents: read AGENTS.md at the root of this repository. The benchmark notebooks are in benchmarks/: ww_leaderboard reads published results and needs no plugins; ww_benchmark installs and runs the plugins. -->

# Benchmarks

The benchmark notebooks compare OpenVoiceOS plugins on the same test sets. They use the
[plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena). The arena lists the plugins and their settings,
lists the test sets, runs each plugin on each clip, and publishes one result row per clip on Hugging Face. The notebooks
use the arena's own code. A number in a notebook is the same number the arena shows on its website.

If you have never used a notebook, read [Getting started](getting-started.md) first.

## The notebooks

| Notebook | What it does | Needs | Time |
|---|---|---|---|
| [`ww_leaderboard`](../benchmarks/ww_leaderboard.ipynb) | Reads every published wake-word result, scores it again, checks the numbers against the arena's boards, and plots the plugins | CPU, internet | About 2 minutes |
| [`ww_benchmark`](../benchmarks/ww_benchmark.ipynb) | Installs every wake-word plugin, runs each one on the arena's test sets, and scores it. It can send the results to the arena | CPU, 3 GB of memory, internet | About one and a half hours with the default settings: 43 fighters, 9 test sets, 300 clips each |

## Wake-word test sets

A wake-word test set has clips with the phrase and clips without it. A plugin must wake on the first kind and stay
quiet on the second kind.

| Test sets | The clips with the phrase | Why use them |
|---|---|---|
| `picovoice-*` | People recorded for the open Picovoice wake-word benchmark | No plugin trained on them, so this is the fairest test |
| `community-*` | People from the OVOS community | Real voices and microphones. A plugin that trained on a set is not scored on it |
| `synthetic-wakewords-*` | The phrase in many computer voices | Many phrases, but no room echo and no microphone, so it is easier than a home |
| `sam-wake-word` | The phrase "sam" | It has its own hard negatives, so its false-accept rate is not comparable with the other sets |

The clips without the phrase come from speech, sounds, music and noise. The sources are the TigreGotico
not-wake-word sets and the Multilingual Spoken Words corpus.

## How to read the numbers

| Number | Meaning | Better |
|---|---|---|
| error rate | The share of clips the plugin got wrong | Lower |
| false rejects | The share of clips with the phrase that did not wake the plugin | Lower |
| false accepts | The share of clips without the phrase that woke the plugin | Lower |
| false wake-ups per hour | False accepts for each hour of audio without the phrase. It is shown only when there is at least a quarter hour of that audio | Lower |
| clips | The clips behind the numbers. A result with fewer than 30 clips is not ranked | More |

A result with no clips without the phrase tells you nothing about false wake-ups. The column `without phrase` shows
how many of those clips a result has.

By default, the notebooks score a plugin only on the test sets of its own phrase. A "computer" detector on a
"hey mycroft" set misses every clip with the phrase, and that tells you nothing new. Set `SAME_PHRASE_ONLY = False` to
see every row.

## Which plugins run

`ww_benchmark` runs every fighter that the arena lists for the phrase of a test set, when its plugin is installed.
A fighter that trained on a test set does not run on it. Three plugins need no trained model for the phrase:

| Plugin | What it gets | Where it runs |
|---|---|---|
| `ovos-ww-plugin-wakeforge-zeroshot` | The phones of the phrase, made once with eSpeak NG | Every English phrase that has a test set |
| `ovos-ww-plugin-efficientword-net` | Its own bundled recordings | Test sets of "alexa" and "computer" |
| `ovos-ww-plugin-local-wake` | Four synthetic recordings of the phrase | Test sets of "alexa" and "hey ziggy", except the set the recordings come from |

Two plugins cannot run: `ovos-ww-plugin-pocketsphinx`, because its version on PyPI does not build, and
`ovos-ww-plugin-wakewordlab`, because it is not on PyPI. The arena also defines a test of continuous audio
(`ww_stream_hey_mycroft`). Its recordings are not published, so no notebook runs it.

## Send results to the arena

With `UPLOAD = True` and a token in `HF_TOKEN`, `ww_benchmark` sends its rows to the arena's Hugging Face datasets.
Ask the arena maintainers first. The notebook adds the published rows that the run did not make, so it loses no
published row. It sends a test set only when every fighter on it has 30 or more clips. The arena builds its boards
from these datasets once a day.

## Results

[`ww_benchmark_results.md`](../benchmarks/ww_benchmark_results.md) reports one full run: 73 fighters on 27 test sets,
with the table in [`ww_benchmark_results.csv`](../benchmarks/ww_benchmark_results.csv).

## The arena code

The arena is not a package on PyPI. Each notebook downloads one fixed commit of it with git, set by `ARENA_REF` in the
Settings cell. The same commit gives the same plugin list, the same test sets and the same scores. To use a newer arena,
set `ARENA_REF` to a newer commit.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Benchmarks](benchmarks.md) · [AI coding agents](ai-agents.md)
