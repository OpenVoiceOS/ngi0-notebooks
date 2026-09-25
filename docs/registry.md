# Language registry

The file [`registry/tts.yaml`](../registry/tts.yaml) has one entry for each language or variety.
The entry names what the chain may use for that language. The notebooks take a donor or a judge
only from this file. No notebook picks an engine from a language code.

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
  judges:                    # OVOS STT plugins, combined with ovos-stt-plugin-rover
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

[tts-data-sources.md](tts-data-sources.md) lists the candidates for each language. The registry
holds only what was admitted.
