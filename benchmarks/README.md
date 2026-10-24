# Benchmark notebooks

These notebooks compare OpenVoiceOS plugins with the
[plugin arena](https://github.com/OpenVoiceOS/ovos-plugin-arena). [Benchmarks](../docs/benchmarks.md) explains the test
sets and how to read the numbers.

| Notebook | What it does | Needs | CI |
|---|---|---|---|
| [`ww_leaderboard`](ww_leaderboard.ipynb) | Reads every published wake-word result, scores it again with the arena's code, checks it against the arena's boards, and plots the plugins | CPU, internet | Linted, compiled under Python 3.11 and 3.12, and executed on the smoke path |
| [`ww_benchmark`](ww_benchmark.ipynb) | Installs every wake-word plugin, runs each one on the arena's test sets, scores it with the arena's code, and can send the results to the arena | CPU, internet | Linted, compiled under Python 3.11 and 3.12, and executed on the smoke path: one plugin, four clips with the phrase |

[`ww_benchmark_results.md`](ww_benchmark_results.md) reports one full run of `ww_benchmark`, and
[`ww_benchmark_results.csv`](ww_benchmark_results.csv) holds its table.

Each notebook has its own `requirements/<notebook>.txt`, the same as the notebooks in [`notebooks/`](../notebooks/).
