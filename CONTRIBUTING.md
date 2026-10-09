# Contributing

This repository holds the NGI0 Commons Fund deliverable notebooks for
OpenVoiceOS. Every notebook must stay runnable, honest about what it needs,
and clean in git history.

## Dependencies

- Reference PyPI package names only. Never `pip install git+...`.
- Every notebook installs into its own kernel the same way, in one line per
  install cell: `%pip install --quiet --pre "<spec>" "<spec>" ...`, every
  spec double-quoted (an unquoted spec with a shell metacharacter, such as a
  version range, is silently mangled by the shell `%pip` delegates to). This
  is the only install mechanism used in a notebook body: not `!pip`, not
  `subprocess`/`uv` invoked against `sys.executable`, and not a bare `pip
  install`. The one exception is `train_vits.ipynb`'s training step, which
  creates and installs into a **separate** virtual environment outside the
  Jupyter kernel (phoonnx's training stack does not need to share a Python
  with the notebook's own dependencies); that step uses `uv` via
  `subprocess`, since there is no kernel package set to install into.
- Never pass `--break-system-packages` to `pip`. If a notebook needs to
  install into a managed environment (Kaggle, Colab), use a virtual
  environment or accept the warning; do not damage the host Python.
- Never hardcode an absolute local path (`/home/<user>/...`). Every notebook
  writes to a path derived from its own working directory or an environment
  variable with a sane default.
- Each notebook has its own `requirements/<notebook-stem>.txt`. Add a new
  dependency there, not only inline in the notebook.

## Header and footer template

The first cell of every notebook is a single markdown cell with:

1. `# <Title>`
2. The NGI0 Commons Fund badge, linked to the project page:
   `[![NGI0 Commons Fund](../ngi.png)](https://nlnet.nl/project/OpenVoiceOS)`
3. The funding sentence, verbatim and in full, as its own paragraph (not a
   blockquote):

   This project was funded through the NGI0 Commons Fund, a fund
   established by NLnet with financial support from the European
   Commission's Next Generation Internet programme, under the aegis of DG
   Communications Networks, Content and Technology under grant agreement
   No 101135429. Additional funding is made available by the Swiss State
   Secretariat for Education, Research and Innovation (SERI).

   Grant agreement 101135429 is the European Commission's agreement with
   NLnet for NGI0 Commons Fund, not an NLnet grant to this project; never
   call it an "NLnet grant".
4. A one-line AI-assistance disclosure, as a blockquote: "This notebook was
   written with AI assistance (Claude, via Claude Code). Verify outputs
   before relying on them." One wording, used everywhere; it never names a
   specific model and never adds a second sentence.
5. A one-line purpose statement (a notebook with more to say about its own
   pipeline, inputs or outputs may add as much prose, and as many of its own
   tables, as it needs after this point; the summary table below still
   appears, even when a fuller explanation follows it).
6. A table with rows Inputs, Outputs, Runtime, Hardware, Cost (header row
   `| Field | Value |`). The Cost row states time or hardware, the same as
   Runtime and Hardware — none of the notebooks here spend money, so no Cost
   row ever states one.
7. A line stating exactly `CI: linted, compiled under Python 3.11 and 3.12,
   and executed on the smoke path.`, since every notebook in `notebooks/` is
   linted, compiled and smoke-run by `ci.yml`, and no notebook is exempt (the
   four evidence notebooks are additionally re-executed in full by the
   `evidence` job). A sentence of real detail may follow it in the same
   paragraph (for example, which branch the SMOKE path takes, or what the
   full run needs that CI does not exercise).

The three wake-word notebooks (`synthetic_ww_dataset`, `kaggle_quickstart_ww`,
`tts2ww_full_pipeline`) are written for people who do not program, so their
first cell differs from the template in three ways. It opens with the title
and the Open in Kaggle and Open in Colab badges, then a "Start here" section
in plain words: what the notebook does, how long it takes, whether it needs a
GPU, and the one thing to set (usually nothing). The funding badge, the
funding sentence and the AI-assistance disclosure move unchanged to the last
cell, above the licence line. And `SMOKE` defaults to `True` where a full run
is long, so that Run All with no edits finishes in minutes; the full run is a
one-word change in the parameters cell. `docs/tester-guide.md` describes these
three notebooks for a first-time tester.

The last cell of every notebook ends with exactly `Licensed under Apache-2.0.`

The funding sentence and the licence line each appear exactly once, in the
places above, nowhere else in the notebook.

## The parameters cell

The second cell of every notebook is a code cell tagged `parameters`
(Jupyter/papermill convention). CI calls every notebook the same way
(`-p SMOKE True -p N_SAMPLES 4 -p EPOCHS 1`), so the parameters cell defines
whichever of `SMOKE`, `N_SAMPLES` and `EPOCHS` change what the notebook does:

```python
SMOKE = False
N_SAMPLES = 32
EPOCHS = 1
```

and, where the notebook trains or loads one identifiable model, `MODEL_ID`
with the notebook's real default (`kaggle_quickstart_ww` has neither
`MODEL_ID` nor an equivalent: under `SMOKE` it shrinks the data, not the model). When `SMOKE` is `True`, the notebook takes the
smallest realistic path through its own logic: it slices a dataset to
`N_SAMPLES` rows, trains for `EPOCHS` step or epoch, and swaps in the
smallest available model where one is configurable. A notebook whose smoke
path still needs a GPU says so in its header instead of pretending
otherwise.

A notebook whose work does not scale with one of these three (a fixed
handful of payloads, a fixed handful of MCP calls, three fixed synthetic
voices) does not declare a dead variable for it: the parameters cell says so
in a comment instead, naming which of the three do not apply and why.
Passing `-p SMOKE True` to such a notebook still works — papermill injects
the value as a new variable — it is simply never read.

## Outputs

Notebook outputs are stripped before commit (`nbstripout`) with one
exception: `arena_prediction_runner`, `bus_message_validation`,
`interop_mcp_utcp_clients` and `speaker_verification` commit their outputs on
purpose, as evidence that the grant deliverable ran. Do not add a fifth
notebook to that list without discussing it with a maintainer first. Every
addition is either evidence or noise, never both.

## Running the smoke path locally

Python 3.11 or 3.12 (matching CI); Python 3.14 fails `nest_asyncio` with
`RuntimeError: Timeout should be used inside a task`.

```bash
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install --prerelease=allow pip jupyter papermill ipykernel nest_asyncio
uv pip install --prerelease=allow -r requirements/<notebook-stem>.txt
papermill notebooks/<notebook-stem>.ipynb /tmp/out.ipynb \
    -p SMOKE True -p N_SAMPLES 4 -p EPOCHS 1
```

A CPU machine is enough for every notebook's `SMOKE=True` path, including the
ones that train (`train_vits` and `kaggle_quickstart_ww`): the smoke path runs to
its last cell on CPU, the same as every other notebook here. A GPU is only needed
for a **full** (`SMOKE=False`) run of those two, where CPU would still finish but
too slowly to produce a usable model in practice.

## Before opening a PR

1. `pre-commit run --all-files` (installs `nbstripout` and `check-json`, see
   `.pre-commit-config.yaml`).
2. Run the smoke path for every notebook you touched and confirm the exit
   code.
3. Keep the README's notebook index in sync: task, hardware, wall time, and
   CI status per notebook.
