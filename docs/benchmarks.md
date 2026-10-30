<!-- For AI agents: read AGENTS.md at the root of this repository. The benchmark notebooks are in benchmarks/: ww_leaderboard reads published results and needs no plugins; ww_benchmark installs and runs the wake-word plugins; intent_benchmark installs and runs the intent pipelines. -->

# Benchmarks

The benchmark notebooks compare OpenVoiceOS plugins on the same test sets. They use the
[plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena). The arena lists the plugins and their settings,
lists the test sets, runs each plugin on each clip, and publishes one result row per clip on Hugging Face. The notebooks
use the arena's own code. A number in a notebook is the same number the arena shows on its website.

If you have never used a notebook, read [Getting started](getting-started.md) first.

## The notebooks

| Notebook | What it does | Needs | Time |
|---|---|---|---|
| [`ww_leaderboard`](../benchmarks/ww_leaderboard.ipynb) | Reads the published wake-word results of the boards that the arena lists, on clips and on audio with no wake word, scores them again, checks the numbers against the arena's boards, and plots the plugins | CPU, internet | About 2 minutes |
| [`ww_benchmark`](../benchmarks/ww_benchmark.ipynb) | Installs every wake-word plugin, runs each one on the arena's test sets, and scores it. It can send the results to the arena | CPU, 3 GB of memory, internet | Hours. The default settings run 35 fighters on 9 test sets, 64 fighter runs in all |
| [`intent_benchmark`](../benchmarks/intent_benchmark.ipynb) | Installs the intent pipeline plugins, trains each intent fighter on each intent test set, runs it on the test sentences, and scores it. It can send the results to the arena | CPU, internet | Hours. The default settings run 36 fighters on 12 test sets, 1332 fighter runs (fighter, test set and language) in all. `SMOKE = True` trains one fighter and runs it on 40 sentences in a few minutes |

## Wake-word test sets

A wake-word test set has clips with the phrase and clips without it. A plugin must wake on the first kind and stay
quiet on the second kind.

| Test sets | The clips with the phrase | Why use them |
|---|---|---|
| `picovoice-*` | People recorded for the open Picovoice wake-word benchmark | No plugin trained on them, so this is the fairest test |
| `tigregotico-*` | The phrase from several text-to-speech engines and converted voices | Many voices, but no room echo and no microphone. A plugin that trained on a set is not scored on it |
| `synthetic-wakewords-*` | The phrase in many computer voices | Many phrases, but no room echo and no microphone, so it is easier than a home |

The clips without the phrase come from speech, sounds, music and noise. The sources are the TigreGotico
not-wake-word sets and the Multilingual Spoken Words corpus.

The arena's website lists a clip board when the board compares at least two trained models of the phrase on 50 or
more clips with the phrase, and when the arena features that phrase. The arena features five phrases: "alexa",
"hey jarvis", "hey mycroft", "hey robin" and "okay nabu". A test set of these phrases is listed when its board
exists and meets the rule. The default test sets of `ww_benchmark` are the 9 clip sets
of these phrases that meet the rule: `picovoice-alexa`, `synthetic-wakewords-alexa`, `tigregotico-alexa`,
`synthetic-wakewords-hey_jarvis`, `tigregotico-hey_jarvis`, `synthetic-wakewords-hey_mycroft`,
`tigregotico-hey_mycroft`, `synthetic-wakewords-hey_robin` and `tigregotico-ok_nabu`. `ww_leaderboard` reads the
boards that the arena lists.

The false wake-up sets, `ww-negatives-<language>`, are hours of audio with no wake word. The arena has one,
`ww-negatives-en-US`: 20 hours of read speech, meetings, radio and talks, music, household and outdoor sounds, and
speech in other languages. A fighter streams the whole set, and its board counts how often per hour the fighter woke,
for all the audio and for each kind of audio. A fighter gets the audio in 80 ms blocks. Vosk checks for the phrase on
a clock, so it gets the 2048-sample (128 ms) chunks of the OpenVoiceOS listener. Set `RUN_STREAM = True` in
`ww_benchmark` to run this test.

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
A fighter that trained on a test set does not run on it. Four plugins need no trained model for the phrase:

| Plugin | What it gets | Where it runs |
|---|---|---|
| `ovos-ww-plugin-wakeforge-zeroshot` | The phones of the phrase, made once with eSpeak NG | Test sets of the five phrases the arena features |
| `ovos-ww-plugin-vosk` | The phrase as text. A Vosk speech model of the language transcribes the audio, and the plugin wakes when the transcript has the phrase | Test sets of "alexa", "hey jarvis", "hey mycroft" and "hey robin" |
| `ovos-ww-plugin-efficientword-net` | Its own bundled reference embeddings | Test sets of "alexa" |
| `ovos-ww-plugin-local-wake` | Four synthetic recordings of the phrase | Test sets of "alexa". It never runs on `synthetic-wakewords-alexa`, the set the recordings come from |

Two plugins cannot run: `ovos-ww-plugin-pocketsphinx`, because its version on PyPI does not build, and
`ovos-ww-plugin-wakewordlab`, because it is not on PyPI.

## Intent test sets

`intent_benchmark` trains each intent fighter on the training data of a test set, and then gives it the test
sentences of that set. A fighter is one pipeline: one or more intent plugins in a fixed order, with fixed settings.
A fighter runs on a test set only when every plugin in it can train on the training data of that set. A keyword
plugin, for example, cannot train on a set that has only example sentences.

The default test sets are the 12 intent test sets of the arena: `intents-for-eval`, `ovos-intents-v5`,
`massive-templates`, `banking77`, `clinc150`, `snips` and the six `mtop-*` sets. The arena lists 44 intent fighters.
The default settings leave out the 7 fighters that use `ovos-jurebes-pipeline-plugin` (`EXCLUDE_PLUGINS`). Of the
other 37, 36 can train on at least one test set. `ovos-stock` runs on none of them.

Each league has its own boards:

| League | The fighters |
|---|---|
| `intent_online` | They train on the sentences of the test set |
| `intent_offline` | They use a model that was trained before |
| `intent_keyword` | They match keywords |
| `intent_zero_shot` | They do not train |

The **accuracy** is the share of test sentences that got the correct intent. A sentence with no correct intent counts
as correct when the fighter chose no intent. The boards rank on the **generalization accuracy**: the accuracy on the
test sentences that are not close to the training data. Higher is better. A result with fewer than 30 sentences is not
ranked.

## Send results to the arena

With `UPLOAD = True`, `ww_benchmark` and `intent_benchmark` send their rows to the arena's Hugging Face datasets. The
token comes from `HF_TOKEN`, from a Kaggle secret called `HF_TOKEN`, or from the login that `hf auth login` stores.
Ask the arena maintainers first. Each notebook adds the published rows that the run did not make, so it loses no
published row. `ww_benchmark` sends a test set only when every fighter on it has 30 or more clips. The arena builds
its boards from these datasets once a day.

## The arena code

The arena is not a package on PyPI. Each notebook downloads one fixed commit of it with git, set by `ARENA_REF` in the
Settings cell. The same commit gives the same plugin list, the same test sets and the same scores. To use a newer arena,
set `ARENA_REF` to a newer commit.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Benchmarks](benchmarks.md) · [AI coding agents](ai-agents.md)
