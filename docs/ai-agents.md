<!-- For AI agents: read AGENTS.md at the root of this repository before you run a notebook. -->

# Use the notebooks with an AI coding agent

An AI coding agent is a program that reads files, runs commands and edits code for you, when you ask it in plain
words. Many people use one, so this page explains how to let an agent run these notebooks for you. We do not endorse
any agent. What an agent can do depends on the agent and on the model behind it, so check what it does, and check the
result.

With an agent, you can ask for a complete task in one sentence, for example: "Make a Portuguese TTS dataset with
OmniVoice on Kaggle, train a voice from it in two rounds, and download the voice." The agent edits the settings of the
notebooks, sends them to Kaggle, waits for each run, and passes the result of one notebook to the next.

## Choose an agent

[Mistral Vibe](https://github.com/mistralai/mistral-vibe) is the coding agent of Mistral AI, a European company. It is
free software under the Apache 2.0 licence, and it uses the Mistral models. Other agents work too, for example Aider,
OpenCode, Goose, Codex CLI, Gemini CLI and Claude Code. Some agents need an account or a paid plan with their
provider.

To install Mistral Vibe, first install [uv](https://docs.astral.sh/uv/), and then run this command:

```
uv tool install mistral-vibe
```

## Prepare once

These steps need a person, because they need your accounts. Do them once, before you give the work to the agent.

1. Make an account at [kaggle.com](https://www.kaggle.com), and confirm your phone number. Without it, Kaggle gives
   no GPU and no Internet to a notebook.
2. On the [Kaggle settings page](https://www.kaggle.com/settings/api), create an API token. Store it in the file
   `~/.kaggle/access_token`, or in the environment variable `KAGGLE_API_TOKEN`.
3. Install the Kaggle command-line tool with `uv tool install kaggle`, and check it with `kaggle kernels list --mine`.
4. Clone this repository, and start the agent in its folder:

```
git clone https://github.com/OpenVoiceOS/ngi0-notebooks
cd ngi0-notebooks
vibe
```

The file [`AGENTS.md`](../AGENTS.md) at the root of the repository tells the agent how to run the notebooks. Many
agents read it by themselves. If your agent does not, tell it to read `AGENTS.md` first.

## What the agent does

The agent uses the Kaggle command-line tool. It copies a notebook to a work folder, adds a first cell with your settings,
and writes a file `kernel-metadata.json` that turns on the GPU and Internet. Then it runs `kaggle kernels push`, which
sends the notebook to Kaggle and starts it. It checks the run with `kaggle kernels status`, and downloads the files
with `kaggle kernels output`. To give the result of one run to the next notebook, it names the first run in
`kernel_sources` of the second.

A notebook that needs no GPU can also run on your own computer. The agent then runs it with papermill, and
gives the settings as environment variables.

## Keep control

- **Your tokens.** Never let the agent write a Hugging Face token or a Kaggle token into a notebook that it sends to
  Kaggle or to a public place. A notebook keeps the text of its cells. Publish a dataset from your own computer,
  where the token stays in an environment variable.
- **Your GPU hours.** Kaggle gives a limited number of GPU hours each week. Tell the agent how many hours it can
  use, and check the runs on your Kaggle page.
- **The result.** Listen to some clips of each dataset, and to the samples of each trained voice. An agent cannot
  hear whether a voice speaks your language well.
- **Licences.** Tell the agent which licences you accept for the source speech.
  [Where the speech comes from](tts-approaches.md) explains the choices.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
