# Contributing

This repository holds the OpenVoiceOS notebooks. Every notebook must stay
runnable, honest about what it needs, and clean in git history.

## Dependencies

- Reference PyPI package names only. Never `pip install git+...`.
- Every notebook installs into its own kernel the same way, in one line per
  install cell: `%pip install --quiet --pre "<spec>" "<spec>" ...`, every
  spec double-quoted (an unquoted spec with a shell metacharacter, such as a
  version range, is silently mangled by the shell `%pip` delegates to). The
  notebooks that commit outputs from a Kaggle run (`arena_prediction_runner`,
  `interop_mcp_utcp_clients`, `speaker_verification`) write `%pip install
  --quiet --quiet --progress-bar off --pre ...` instead, so the saved outputs
  hold no download progress bars. This is the only install mechanism used in a notebook body: not `!pip`, not
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

## Notebook style

The readers are end users, and many have never programmed. A notebook is
written so that such a reader can press Run All and understand what they got.
`kaggle_quickstart_ww` is the worked example: copy its shape.

**Cells, in this order.**

1. One markdown cell: `# <Title>`, the Open in Kaggle and Open in Colab
   badges, then `## Start here` in three to five short sentences: what you
   get, how long it takes, whether it needs a GPU, and the one thing to
   change.
2. The Settings cell, tagged `parameters` (see the next section). It holds
   only what a beginner would change, each with a short comment, and
   whichever of `SMOKE`, `N_SAMPLES` and `EPOCHS` apply.
3. An "Advanced settings" cell with every other setting, each a plain
   variable with its default.
4. Numbered steps. Each is a heading `## Step N — <what happens>`, at most
   two short sentences, then the code.
5. `## What you got`: where the result is, how to use it in OVOS, and the
   measured numbers with one sentence on how to read them.
6. The closing markdown cell: the funding credit from the Credits section of
   `README.md`, the one-line AI-assistance note, and the line
   `Licensed under Apache-2.0.`

**Prose.** Short sentences and everyday words. A technical word gets a gloss
of about five words where it first appears. Say what a step does, not how it
was designed. Keep a caveat only if it changes what the reader does: for
example, that the numbers describe one run. Detail for a curious reader goes
into one collapsible `<details>` block per step, or is cut. No dates and no
account of how the notebook changed.

**Code.** Keep every check that protects the result, such as an assertion that
no voice is in both the training and the test data. Remove branches that
cannot run, helpers that repeat each other and checks that cannot trigger.
Settings are plain variables, not environment variables.

Helper code that a beginner should not have to read goes into hidden cells.
A hidden cell has the metadata `{"jupyter": {"source_hidden": true},
"_kg_hide-input": true, "cellView": "form"}` and starts with the line
`#@title Code for step N: <what it defines>`. JupyterLab and Kaggle collapse
such a cell and Colab shows only the title; `nbstripout` keeps the metadata.
The visible cell of a step then calls the helpers by name, one short
commented line each.

**Output.** Each step prints one line in plain words, such as `Step 3 done:
...`, and the last code cell prints a summary. Tables and traces print only
when the Advanced setting `SHOW_DETAILS` is `True`. An error a beginner can
cause says what to click: no GPU, no internet, a wrong folder.

The hardware a notebook needs goes in the Needs column of the notebook index
in `README.md`; how long it takes goes in its "Start here". A notebook that
opens with a
`| Field | Value |` summary table and a `CI:` line follows an older template;
give it this shape when you rework it, and do not start a notebook that way.

A notebook may default `SMOKE` to `True` when its full run takes hours, so
that Run All with no edits finishes in minutes; its "Start here" then says
that the full run is a one-word change. `docs/wake-words.md` describes the
wake-word notebooks for a first-time tester.
## Header and footer template

The first cell of every notebook is a single markdown cell with:

1. `# <Title>`
2. A one-line purpose statement (a notebook with more to say about its own
   pipeline, inputs or outputs may add as much prose, and as many of its own
   tables, as it needs after this point; the summary table below still
   appears, even when a fuller explanation follows it).
3. A table with rows Inputs, Outputs, Runtime, Hardware, Cost (header row
   `| Field | Value |`). The Cost row states time or hardware, the same as
   Runtime and Hardware — none of the notebooks here spend money, so no Cost
   row ever states one.
4. A line stating exactly `CI: linted, compiled under Python 3.11 and 3.12,
   and executed on the smoke path.`, since every notebook in `notebooks/` is
   linted, compiled and smoke-run by `ci.yml` (the notebooks that keep their
   outputs are additionally re-executed in full by the `evidence` job). The
   exception is a notebook that speaks with OmniVoice: OmniVoice needs a GPU
   and the CI runners have none, so `ci.yml` lists it as GPU-only and its line
   reads `CI: linted and compiled under Python 3.11 and 3.12.`, followed by
   why it is run on Kaggle instead. A sentence of real detail may follow it
   in the same paragraph (for example, which branch the SMOKE path takes, or
   what the full run needs that CI does not exercise).

The three wake-word notebooks (`synthetic_ww_dataset`, `kaggle_quickstart_ww`,
`tts2ww_full_pipeline`) are written for people who do not program, so their
first cell differs from the template in two ways. It opens with the title
and the Open in Kaggle and Open in Colab badges, then a "Start here" section
in plain words: what the notebook does, how long it takes, whether it needs a
GPU, and the one thing to set (usually nothing). And `SMOKE` defaults to
`True` where a full run is long, so that Run All with no edits finishes in
minutes; the full run is a one-word change in the parameters cell. `docs/wake-words.md` describes these
three notebooks for a first-time tester.

`ww_train_streaming` has the same badges and "Start here" section, but it
trains on a dataset made by `synthetic_ww_dataset`, so the one thing to set is
`DATASET_DIRS`. `SMOKE` defaults to `False`, and Run All with `DATASET_DIRS`
empty stops with a message that says what to set.

The last cell of every notebook is a markdown cell with the funding credit
from the Credits section of `README.md`, the one-line AI-assistance note, and
the closing line `Licensed under Apache-2.0.`

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
purpose, so that a reader sees what a full run produces without running it.
CI re-executes `bus_message_validation` in its `evidence` job; the other three
speak with OmniVoice, need a GPU, and keep the outputs of a Kaggle run with
the committed code. Do not add a fifth notebook to that list without
discussing it with a maintainer first.

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

A CPU machine is enough for the `SMOKE=True` path of every notebook that CI
smoke-runs, including `kaggle_quickstart_ww`, which trains. The notebooks that
speak with OmniVoice need a GPU even on their smoke path; `ci.yml` lists them,
and they are run on Kaggle with a GPU selected.

## Before opening a PR

1. `pre-commit run --all-files` (installs `nbstripout` and `check-json`, see
   `.pre-commit-config.yaml`).
2. Run the smoke path for every notebook you touched and confirm the exit
   code; for a notebook that speaks with OmniVoice, run it on Kaggle with a
   GPU.
3. Keep the README's notebook index in sync: what each notebook does and what
   it needs.
