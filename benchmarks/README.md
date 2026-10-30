# Benchmark notebooks

These notebooks compare OpenVoiceOS plugins with the
[plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena). [Benchmarks](../docs/benchmarks.md) explains the test
sets and how to read the numbers.

| Notebook | What it does | Needs | CI |
|---|---|---|---|
| [`ww_leaderboard`](ww_leaderboard.ipynb) | Reads the published wake-word results of the boards that the arena lists, on clips and on audio with no wake word, scores it again with the arena's code, checks it against the arena's boards, and plots the plugins | CPU, internet | Linted, compiled under Python 3.11 and 3.12, and executed on the smoke path |
| [`ww_benchmark`](ww_benchmark.ipynb) | Installs every wake-word plugin, runs each one on the arena's test sets of clips and on hours of audio with no wake word, scores it with the arena's code, and can send the results to the arena | CPU, internet | Linted, compiled under Python 3.11 and 3.12, and executed on the smoke path: one plugin, four clips with the phrase |
| [`intent_benchmark`](intent_benchmark.ipynb) | Installs the intent pipeline plugins, trains each intent fighter of the arena on the training data of each intent test set, runs it on the test sentences, scores it with the arena's code, and can send the results to the arena | CPU, internet | Linted, compiled under Python 3.11 and 3.12, and executed on the smoke path: one fighter, 40 English sentences |

Each notebook has its own `requirements/<notebook>.txt`, the same as the notebooks in [`notebooks/`](../notebooks/).
