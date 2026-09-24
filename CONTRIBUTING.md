# Contributing

This repository holds the NGI0 Commons Fund deliverable notebooks for
OpenVoiceOS. Every notebook must stay runnable, honest about what it needs,
and clean in git history.

## Dependencies

- Reference PyPI package names only. Never `pip install git+...`.
- Pre-release channel packages install with `--pre` (`pip install --pre
  <package>`). A `uv pip install --prerelease=allow` line is equivalent and
  preferred for local runs.
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
2. A one-line purpose statement.
3. A table with rows Inputs, Outputs, Runtime, Hardware, Cost.
4. A line stating `CI: executed on the smoke path` or `CI: syntax check only
   (<reason>)`.

The last cell of every notebook is exactly:

> Licensed under Apache-2.0. Funded through the NGI0 Commons Fund, established
> by NLnet with financial support from the European Commission's Next
> Generation Internet programme (grant agreement 101135429).

Funding and licensing text appears nowhere else in the notebook.

## The parameters cell

The second cell of every notebook is a code cell tagged `parameters`
(Jupyter/papermill convention) defining at least:

```python
SMOKE = False
N_SAMPLES = 32
EPOCHS = 1
```

and, where the notebook trains or loads a model, `MODEL_ID` with the
notebook's real default. When `SMOKE` is `True`, the notebook takes the
smallest realistic path through its own logic: it slices a dataset to
`N_SAMPLES` rows, trains for `EPOCHS` step or epoch, and swaps in the
smallest available model where one is configurable. A notebook whose smoke
path still needs a GPU says so in its header instead of pretending
otherwise.

## Outputs

Notebook outputs are stripped before commit (`nbstripout`) with one
exception: `arena_prediction_runner`, `bus_message_validation`,
`interop_mcp_utcp_clients` and `speaker_verification` commit their outputs on
purpose, as evidence that the grant deliverable ran. Do not add a fifth
notebook to that list without discussing it with a maintainer first. Every
addition is either evidence or noise, never both.

## Running the smoke path locally

```bash
uv venv .venv
source .venv/bin/activate
uv pip install --prerelease=allow jupyter papermill ipykernel nest_asyncio
uv pip install --prerelease=allow -r requirements/<notebook-stem>.txt
papermill notebooks/<notebook-stem>.ipynb /tmp/out.ipynb \
    -p SMOKE True -p N_SAMPLES 4 -p EPOCHS 1
```

A CPU machine is enough for `arena_prediction_runner`,
`bus_message_validation`, `interop_mcp_utcp_clients`,
`speaker_verification`, and `synthetic_ww_dataset`. The rest need a GPU for
a training step that actually produces a model. On CPU, papermill still
proves the notebook parses and runs its early cells without raising.

## Before opening a PR

1. `pre-commit run --all-files` (installs `nbstripout` and `check-json`, see
   `.pre-commit-config.yaml`).
2. Run the smoke path for every notebook you touched and confirm the exit
   code.
3. Keep the README's notebook index in sync: task, hardware, wall time, and
   CI status per notebook.
