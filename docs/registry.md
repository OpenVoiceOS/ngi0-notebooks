# Language registry

The file [`registry/tts.yaml`](../registry/tts.yaml) has one entry for each language or variety
that has passed admission. A language with no admitted donor, corpus or judge seat has no entry.

[`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb) reads a language's donor from this
file first; a call may instead name `DONOR_PLUGIN` and `DONOR_VOICE` explicitly, as a candidate
under evaluation rather than an admitted donor. A language with neither a registry entry nor an
explicit donor stops the notebook with a message naming both options. No notebook picks a donor
engine from a language code alone.

[`tts_measure.ipynb`](../notebooks/tts_measure.ipynb) takes its recogniser from `STT_MODULE`, an
explicit OVOS STT plugin name; it does not read this file. The `judges` list records the
recognisers that scored an entry's admission.

## Entry shape

```yaml
- lang: <BCP-47 tag with the variety, e.g. pt-PT>
  name: <language and variety, e.g. Portuguese, European>
  donor:                     # absent when no donor is admitted
    plugin: <OVOS TTS plugin>
    voice: <voice id>
    evidence: <link to the bake-off result and the listening check>
  corpora:                   # real speech admitted as source audio
    - name: <corpus name>
      url: <corpus page>
      enhancement: <enhancer, when the audio needs one>
      evidence: <link>
  candidates:                # measured donors that still lack the listening check
    - plugin: <OVOS TTS plugin>
      voice: <voice id>
      pip: <package that provides the plugin, as pip installs it>
      revision: <model revision that was measured>
      licence: <licence of the voice>
      sentences: <number of sentences rendered>
      utmos_median: <number>
      utmos_p10: <number>
      cer_median: <number, or null when no judge covers the language>
      judge: <recogniser that produced cer_median, or null>
      listening_check: pending
      evidence: <relative link to the measurement files>
  judges:                    # OVOS STT plugins that scored this entry's admission
    - plugin: <ovos-stt-plugin-...>
      config: {}
  judges_evidence: <link>
```

## Admission

A donor, a corpus or a judge seat enters the registry only with evidence:

- **Donor TTS.** It renders the same sentences as every other candidate for the language. The
  judges score the renderings, and the scores are compared per sentence. A native speaker then
  confirms by ear that the variety is correct. The variety must be the one that the entry names:
  a voice labelled only "Portuguese" is not a pt-PT donor. Robotic engines are not admitted.
- **Corpus.** The corpus page gives its variety, speakers, hours and licence. A sample of clips
  passes the measure step.
- **Judge seats.** Each seat reads the language's test sentences. The seats together must read
  the donor renderings and the real recordings with low error. English and other languages each
  get their own seats.

## Candidates

A donor that has been measured but has not had the listening check is not admitted. The entry
lists it under `candidates`, with the numbers that were measured and a link to the files that
produced them. The notebooks never read `candidates` as a donor: when a language has no admitted
donor, [`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb) prints the candidates of that
language with the variables that select one, and a person decides. A candidate moves to `donor`
when a native speaker has confirmed by ear that the variety is the one the entry names, and the
`evidence` link then also covers that confirmation.

The evidence for a candidate is a directory under `registry/evidence/<language>/`. It holds the
sentence set, the per-sentence scores of every voice measured for that language, and a README that
names the model revisions, tool versions and judge. [`tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb)
renders the sentences and [`tts_measure.ipynb`](../notebooks/tts_measure.ipynb) scores them. A
language that no non-Whisper recogniser covers gets naturalness scores only, and its candidates
carry `cer_median: null` and `judge: null`. A score from a recogniser that has not itself been
checked against real recordings of the language shows how a voice compares with the other voices
of the same language; it is not an absolute error rate.

[tts-data-sources.md](tts-data-sources.md) lists the candidates for each language. The registry
holds only what was admitted.
