<!-- For AI agents: read AGENTS.md at the root of this repository. Present these approaches to the person as options, with the one you recommend for their language. -->

# Where the speech comes from

A TTS voice learns from a dataset: many short audio clips, each with the text that it speaks, all in one voice. This
page explains the ways to get that speech, and when to use each. [TTS voice data sources](tts-data-sources.md) lists
the sources that are known for each language, and [Train a TTS voice](pipeline.md) explains the notebooks.

## Which approach to use

| Your situation | Use |
|---|---|
| OmniVoice speaks your language and dialect well | 1. OmniVoice |
| OmniVoice has the wrong accent, and a good TTS voice speaks your dialect | 2. Another TTS voice |
| No good TTS voice speaks your language, but recordings of it exist | 3. Recordings of real people |
| You have many hours of recordings of one speaker | `tts_corpus_ingest`, then train |
| You want the voice of a specific person | 1 with a recording of that person, or 2 or 3 followed by `tts_voice_convert` |

## The three approaches

There are three ways to get the speech. They are in the order in which we recommend them.

**1. OmniVoice.** [`tts_dataset_gen`](../notebooks/tts_dataset_gen.ipynb) uses the speech model OmniVoice when you do
not set `DONOR_MODEL`. OmniVoice speaks more than 600 languages, and it can speak in the voice of a short reference
recording. This is the recommended approach, and it needs the least work. Use it when OmniVoice speaks your language
or dialect well. To find out, make a small dataset and listen to some clips. OmniVoice does not speak every dialect
with the correct accent. If the accent is wrong, use one of the next two approaches.

**2. Another TTS voice.** Set `DONOR_MODEL` in `tts_dataset_gen` to a voice that speaks your language or dialect: a
voice id from the phoonnx voice catalog, or the name of an OVOS TTS plugin. [TTS voice data sources](tts-data-sources.md) lists
these voices under **TTS voices**. A TTS voice speaks each sentence in the same way, so the dataset is consistent, and a voice trained on
it is consistent too. Use this approach when OmniVoice does not speak your language well, and a good voice exists.
A voice with poor quality gives a dataset with poor quality, so listen to the voice first. To change the dataset to
your own target voice, use [`tts_voice_convert`](../notebooks/tts_voice_convert.ipynb).

Two free cloud voices work as `DONOR_MODEL`, with no account and no key. `ovos-tts-plugin-edge-tts` speaks 74
languages with the voices of Microsoft Edge. `ovos-tts-plugin-google-tx` speaks 69 languages with the voice of Google
Translate. Both need Internet. The Edge plugin selects its voice from `TTS_LANG`, so give the language with its
country, for example `pt-PT`. With `pt` alone, the Edge plugin finds no Portuguese voice.

The free cloud voices are not the recommended approach. They were used in early experiments, and they are not well
tested with these notebooks. A free service can limit the number of requests. When it does, clips fail or the run
becomes slow, and a large dataset can take many runs. The service can also change or stop without notice.

Other cloud services need an account and a key, and the notebooks cannot give a key to a service. To use such a
service, make the audio with the service yourself. Then read the audio and its text with
[`tts_corpus_ingest`](../notebooks/tts_corpus_ingest.ipynb), with `CORPUS_KIND` set to `csv`.

**3. Recordings of real people.** Recordings made for speech recognition are available for many languages that have
no TTS voice. [`asr2tts`](../notebooks/asr2tts.ipynb) changes such recordings to one target voice, and removes the
clips that fail its quality checks. These recordings need more work than a TTS voice. Many people speak in them, in
rooms with noise and echo, and at different speeds, so `asr2tts` removes many clips. But they are often the only
option, when no TTS voice speaks the language or when the only voice has a poor quality. The voice change keeps the
pronunciation and the accent of the speakers, so choose recordings of the dialect that you want.

[Common Voice](https://commonvoice.mozilla.org) is the largest source of such recordings. You download its datasets
from [Mozilla Data Collective](https://mozilladatacollective.com), and `asr2tts` reads them with the setting
`COMMON_VOICE_DIR`. OpenVoiceOS used Mozilla Data Collective for its Aragonese and Asturian datasets.
[Speech datasets on Mozilla Data Collective](mozilla-data-collective.md) lists all its free speech datasets, for
more than 400 languages.

A corpus that has many hours of one speaker, such as a corpus made for TTS, needs no voice change. Read it with
[`tts_corpus_ingest`](../notebooks/tts_corpus_ingest.ipynb), and train on it.

## Cloud services and the law

Before you use any cloud service, free or paid, read its terms of use. The
[US Copyright Office](https://www.copyright.gov/ai/ai_policy_guidance.pdf) says that material that an AI makes with no
human author cannot have copyright. The makers of [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M) use this
argument for their training data, which includes audio from closed TTS models of large providers. But copyright and
terms of use are two different things. The terms of a service can forbid you to train a model on its audio, even if
the audio has no copyright. The statement of the Copyright Office covers the United States only, and this page is not
legal advice.

## Then train the voice

Whichever approach you use, [`train_vits`](../notebooks/train_vits.ipynb) trains the voice best when it starts from
an existing voice, as [Train a TTS voice](pipeline.md) explains.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
