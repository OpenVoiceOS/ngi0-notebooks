<!-- For AI agents: read AGENTS.md at the root of this repository. Show the person the rows for their language, with size and licence, and let them choose. -->

# TTS voice data sources

This page lists the sources of speech that are known for each language and dialect: recordings of real people, and
TTS voices. [Where the speech comes from](tts-approaches.md) explains when to use each kind, and
[Train a TTS voice](pipeline.md) explains the notebooks that read them.

## How to read the tables

Each language has a heading with its language code. Use this code as the value of `TTS_LANG`. Under the heading,
**Recordings** lists recordings of real people, and **TTS voices** lists existing voices. The
tables show only some of the datasets of Mozilla Data Collective, so look for your language in
[its list](mozilla-data-collective.md) too. When a language has no table and no dataset on that list, OmniVoice is
the only option, if it speaks the language.

The Access column of a voice tells you if you can download the voice, or if it is a paid cloud service. The Licence
column quotes the licence that the source states, and "not stated" means that the source states no licence. A licence
with "NC" (non-commercial) does not let you sell the voice or use it in a product that you sell. The column "Published
quality" gives a quality figure from the source's own publication, when one exists. Compare these figures only inside
one publication, because each publication measures in a different way.

## Europe

### Albanian, Gheg (aln)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice, Gheg Albanian](https://mozilladatacollective.com/datasets/cmmytg2r000eynz07epeq9u30) | Gheg | not stated | not stated |

### Albanian, Tosk (sq)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Albanian](https://mozilladatacollective.com/datasets/cmu5z0t4t00genq07z8zelxlo) | Tosk | not stated | "CC0-1.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [SpeechGen](https://speechgen.io/en/) | Tosk | paid cloud service | not measured |

### Alsatian (gsw-FR)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Aragonese (an)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Aragonese](https://mozilladatacollective.com/datasets/cmu5utcpg0085o1076su87se5) | not stated | not stated | "CC0-1.0" |

### Armenian (hy)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 160](https://www.openslr.org/160/) | Armenian | not stated, 70 h | "CC BY 4.0" |

### Aromanian (rup)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Asturian (ast)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Asturian](https://mozilladatacollective.com/datasets/cmu5p0nix00z0mi07xu0wumgo) | not stated | not stated | "CC0-1.0" |

### Basque (eu)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 76](https://www.openslr.org/76/) | Basque | not stated | "Attribution-ShareAlike 4.0 International" |
| [HiTZ-Aholab speech synthesis dataset](https://zenodo.org/records/17952596) | Basque | 2 speakers, about 34.25 h combined | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [HiTZ/TTS-eu_antton](https://huggingface.co/HiTZ/TTS-eu_antton) | Basque | free download | not measured |

### Belarusian (be)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Belarusian](https://mozilladatacollective.com/datasets/cmu5kjjuj00pomi07klnk26oe) | not stated | not stated | "CC0-1.0" |

### Bosnian (bs)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Bosnia-Herzegovina subset) | not stated | not stated, 167,000 rows | "other" |

### Breton (br)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Audio Breton Corpus](https://huggingface.co/datasets/Bretagne/audio-breton-corpus) | Breton | 2 speakers, about 33.7 h combined | not stated |

### Bulgarian (bg)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Bulgaria subset) | not stated | not stated, 528,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (bg-BG) | Bulgarian | paid cloud service | not measured |

### Catalan (ca)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [festcat](https://huggingface.co/datasets/projecte-aina/festcat_trimmed_denoised) | Central | 11 speakers, 22.91 h | "CC BY-SA 3.0" |
| [LaFresCat](https://huggingface.co/datasets/projecte-aina/LaFrescat) | Balearic, Central, North-Western, Valencian | 8 speakers, 3.75 h | "CC BY-NC 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Matxa multiaccent](https://huggingface.co/projecte-aina/matxa-tts-cat-multiaccent) | Balearic, Central, North-Western, Valencian | free download | not measured |

### Cornish (kw)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Corsican (co)

No recordings or TTS voices that you can download are known.

### Croatian (hr)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ParlaSpeech 3.0](https://huggingface.co/datasets/classla/ParlaSpeech-HR) | Croatian | not stated, 3,110 h | "CC BY-SA 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (hr-HR) | Croatian | paid cloud service | not measured |

### Czech (cs)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (jirka, low/medium) | Czech | free download | not measured |

### Danish (da-DK)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Denmark subset) | not stated | not stated, 1,560,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Danish | free download | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (talesyntese, medium) | Danish | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (da-DK) | Danish | paid cloud service | not measured |

### Dutch, Flemish (nl-BE)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nl-BE) | Flemish | paid cloud service | not measured |

### Dutch, Netherlands (nl-NL)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Corpus Gesproken Nederlands](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/) | Netherlands and Flemish, split not stated | not stated, 900 h | "free, signed licence agreement required" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Dutch, variety not stated | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nl-NL) | Netherlands Dutch | paid cloud service | not measured |

### English, British and Irish (en-GB)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 83](https://www.openslr.org/83/) | Irish, Midlands, Northern England, Scottish, Southern England, Welsh | 120 volunteers, 31 h | "Attribution-ShareAlike 4.0 International" |
| [GLOBE](https://huggingface.co/datasets/MushanW/GLOBE) | 164 accents worldwide, including UK and Ireland | 23,519 speakers, 535 h | "CC0-1.0" |

### Estonian (et)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Estonia subset) | not stated | not stated, 215,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (et-EE) | Estonian | paid cloud service | not measured |

### Faroese (fo)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Basic LAnguage Resource Kit 1.0](https://www.openslr.org/125/) | six named dialect areas | 433 speakers, 100 h | "CC BY 4.0" |

### Finnish (fi)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Finnish | free download | not measured |

### Franco-Provençal (frp)

No recordings or TTS voices that you can download are known.

### Galician (gl)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Nos_Celtia-GL](https://zenodo.org/records/7716958) | Galician | 1 speaker, about 25 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [HiTZ/TTS-gl_sabela](https://huggingface.co/HiTZ/TTS-gl_sabela) | Galician | free download | not measured |

### Georgian (ka)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### German (de-DE)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Thorsten](https://www.openslr.org/95/) | German | 1 speaker, more than 23 h | "CC0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | German | free download | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (thorsten, low/medium/high) | German | free download | not measured |

### German, Swiss (gsw-CH)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [STT4SG-350](https://zenodo.org/records/10012816) | all Swiss German dialect regions | 316 speakers, 343 h | "META-SHARE NonCommercial NoRedistribution License" |

### Greek (el)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Greek](https://mozilladatacollective.com/datasets/cmu62fru800nko107kvyi4hrc) | not stated | not stated | "CC0-1.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (rapunzelina, low) | Greek | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (el-GR) | Greek | paid cloud service | not measured |

### Greek, regional (Cypriot, Cretan, Pontic)

No recordings or TTS voices that you can download are known.

### Hungarian (hu)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [KTH Hungarian single-speaker TTS](https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts) | Hungarian | 1 speaker, 4,515 segments (hours not stated) | "CC0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (3 voices) | Hungarian | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (hu-HU) | Hungarian | paid cloud service | not measured |

### Icelandic (is)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Samrómur 21.05](https://www.openslr.org/112/) | Icelandic | 8,392 speakers, 145 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (4 voices) | Icelandic | free download | not measured |

### Irish (ga)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [ABAIR](https://www.abair.ie) | Irish, variety not stated | online service, no download | not measured |

### Italian, Friulian (fur)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Italian, Ladin (lld)

No recordings or TTS voices that you can download are known.

### Italian, Lombard (lmo)

No recordings or TTS voices that you can download are known.

### Italian, Neapolitan (nap)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Italian, Piedmontese (pms)

No recordings or TTS voices that you can download are known.

### Italian, Sardinian (sc)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Italian, Sicilian (scn)

No recordings or TTS voices that you can download are known.

### Italian, Venetian (vec)

No recordings or TTS voices that you can download are known.

### Karelian (krl)

No recordings or TTS voices that you can download are known.

### Kashubian (csb)

No recordings or TTS voices that you can download are known.

### Latgalian (ltg)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Latvian (lv)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Latvia subset) | not stated | not stated, 292,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (aivars, medium) | Latvian | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (lv-LV) | Latvian | paid cloud service | not measured |

### Lithuanian (lt)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (lt-LT) | Lithuanian | paid cloud service | not measured |

### Livonian (liv)

No recordings or TTS voices that you can download are known.

### Low German (nds)

No free recordings and no natural-sounding TTS voice with a working link were found.

### Luxembourgish (lb)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [luxembourgish-speech-dataset](https://huggingface.co/datasets/shunyalabs/luxembourgish-speech-dataset) | not stated | not stated, 3,844 rows | not stated |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (marylux, medium) | Luxembourgish | free download | not measured |

### Macedonian (mk)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Maltese (mt)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Manx (gv)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Mirandese (mwl)

No recordings or TTS voices that you can download are known.

### Norwegian, Bokmål (nb-NO)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NPSC](https://huggingface.co/datasets/NbAiLab/NPSC) | 87.2% Bokmål, 12.8% Nynorsk | not stated, 140.3 h including pauses | "CC0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Norwegian | free download | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (talesyntese, medium) | Norwegian | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nb-NO) | Norwegian Bokmål | paid cloud service | not measured |

### Occitan (oc)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ReVoc](https://zenodo.org/records/11566430) | Aranese, Auvergnat, Gascon, Limousin, Languedocian, Niçard, Provençal, Vivaro-Alpine | not stated, 40,000+ files | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Votz](https://votz.eu) | Gascon, Languedocian | online service, no download | not measured |

### Polish (pl)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [MC Speech Dataset](https://www.openslr.org/142/) | Polish | 1 speaker, more than 22 h | "CC0 1.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Polish | free download | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (4 voices) | Polish | free download | not measured |

### Portuguese, European (pt-PT)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [FalAR](https://huggingface.co/datasets/inesc-id/FalAR) | European | 1,180 speakers, about 4.9k h of parliamentary sessions, 16 kHz; the rooms carry heavy echo, so the audio needs enhancement (for example [callenhancer](https://huggingface.co/TigreGotico/audiosronnx-callenhancer)) before use | "cc-by-4.0" |
| [Tugão 1.0](https://mozilladatacollective.com/datasets/cmiui8v3101cpnv074qwggdsj) | European | 1 speaker, about 1.5 h | "CC0-1.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Azure neural voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) | European (pt-PT locale) | paid cloud service | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (tugão, medium) | European | free download | not measured |

### Romani (rom)

No recordings or TTS voices that you can download are known.

### Romanian (ro)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [romanian-speech-v2](https://huggingface.co/datasets/eduardem/romanian-speech-v2) | Romanian | 21 speakers, 360.16 h | "released strictly for personal research and educational purposes" |

### Romanian, Moldovan (ro-MD)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Moldovan dialectal Romanian speech corpus](https://huggingface.co/datasets/FraPiz/moldovan-dialectal-romanian-speech-corpus) | Moldovan | about 56 speakers, 70.67 h | "source-content-rights-reserved" |

### Romansh (rm)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Russian (ru)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [RUSLAN](https://ruslan-corpus.github.io/) | Russian | 1 speaker, 31+ h | "CC BY-NC-SA 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Russian | free download | not measured |

### Rusyn (rue)

No recordings or TTS voices that you can download are known.

### Sami, Lule (smj)

No free recordings and no natural-sounding TTS voice with a working link were found.

### Sami, Northern (se)

No free recordings and no natural-sounding TTS voice with a working link were found.

### Scottish Gaelic (gd)

No recordings or TTS voices that you can download are known.

### Serbian (sr)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ParlaSpeech 3.0](https://huggingface.co/datasets/classla/ParlaSpeech-RS) | Serbian | not stated, 896 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (serbski_institut, medium) | Serbian | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sr-RS) | Serbian | paid cloud service | not measured |

### Slovak (sk)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SloPalSpeech](https://huggingface.co/datasets/NaiveNeuron/SloPalSpeech) | Slovak | not stated, 2,806 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (lili, medium) | Slovak | free download | not measured |

### Slovenian (sl)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Slovenia subset) | not stated | not stated, 278,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (artur, medium) | Slovenian | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sl-SI) | Slovenian | paid cloud service | not measured |

### Sorbian (hsb)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Spanish, Castilian (es-ES)

No free recordings that are certainly Castilian Spanish were found.

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-es) (Spain finetune) | Castilian | free download | not measured |
| [Azure neural TTS](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) (es-ES, 19+ voices) | Castilian | paid cloud service | not measured |

### Swedish (sv-SE)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Sweden subset) | not stated | not stated, 556,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Swedish | free download | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices) | Swedish | free download | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sv-SE) | Swedish | paid cloud service | not measured |

### Ukrainian (uk)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Ukraine subset) | not stated | not stated, 283,000 rows | "other" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices) | Ukrainian | free download | not measured |

### Welsh (cy)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Welsh](https://huggingface.co/datasets/techiaith/commonvoice_16_1_cy) | not stated | 1,832 speakers, 155.12 h recorded, 122.22 h validated | "CC0-1.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices, medium) | Welsh | free download | not measured |

### West Frisian (fy-NL)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Scripted Speech 27.0 - Frisian](https://mozilladatacollective.com/datasets/cmu5wsbsd00dwnq07h3qbbsz7) | not stated | not stated | "CC0-1.0" |

### Yiddish (yi)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

## Middle East and Africa

### Afrikaans (af-ZA)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NCHLT Afrikaans](https://repo.sadilar.org/handle/20.500.12185/280) | not stated | 8 speakers in its test suite, about 56 h | Creative Commons Attribution 3.0 Unported (CC BY 3.0) |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Azure `af-ZA` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | paid cloud service | not measured |

### Amharic (am-ET)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ALFFA](https://openslr.org/25/) | not stated | not stated | MIT |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Azure `am-ET` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | paid cloud service | not measured |

### Arabic, Algerian Darja (ar-DZ)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://huggingface.co/datasets/UBC-NLP/Casablanca) | Algerian, one of 8 labelled dialects in a pooled release | not stated | "CC BY-NC-ND 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Hadra-TTS-f5](https://huggingface.co/algerian-nlp/Hadra-TTS-f5) | Algerian Darja | free download | not measured (about 399 h of training audio, model card) |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Algeria identifier | Algerian | free download | UTMOS 2.46, WER-O 31.18 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Classical (ar)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ClArTTS](https://huggingface.co/datasets/MBZUAI/ClArTTS) | Classical Arabic, not Modern Standard | one male speaker, about 12 h | "cc-by-4.0" |

No natural-sounding TTS voice is known.

### Arabic, Egyptian (ar-EG)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [F5-TTS Egyptian Arabic](https://huggingface.co/MAdel121/f5-tts-egyptian-arabic) | Egyptian, inherits about 85% Modern Standard Arabic from its base | free download | UTMOS 2.63, WER 20.4% with a Whisper Small Arabic recogniser (model card) |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Egypt identifier | Egyptian | free download | UTMOS 2.14, WER-O 18.58 ([paper](https://arxiv.org/html/2601.13802v1)) |
| [NAMAA-Egyptian-TTS](https://huggingface.co/NAMAA-Space/NAMAA-Egyptian-TTS) | Egyptian, everyday conversational speech | free download | not measured |

### Arabic, Emirati (ar-AE)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), UAE identifier | Emirati | free download | UTMOS 2.75, WER-O 5.15, speaker similarity 0.782 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Iraqi (ar-IQ)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Ghadeer speech crowd corpus](https://data.mendeley.com/datasets/mkhjfnzty5/1) | Iraqi, more than one accent | 210 speakers, 15,626 samples | "CC BY" |
| [Iraqi Dialect TTS Corpus](https://github.com/hayderkharrufa/iraqi-dialect-tts-corpus) | Iraqi, with the extra Iraqi phonemes گ چ پ ڤ ۆ ڵ ێ | not stated | "Creative Commons Attribution 4.0 International License (CC BY 4.0)" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Iraq identifier | Iraqi | free download | UTMOS 2.48, WER-O 17.12 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Mauritanian (ar-MR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://huggingface.co/datasets/UBC-NLP/Casablanca) | Mauritanian, one of 8 labelled dialects in a pooled release | not stated | "CC BY-NC-ND 4.0" |

No natural-sounding TTS voice is known.

### Arabic, Modern Standard, diacritized (ar)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ArVoice](https://huggingface.co/datasets/MBZUAI/ArVoice) | Modern Standard Arabic, diacritized, read by speakers native to Egypt, Jordan, Morocco, Palestine and Syria | 7 human voices, about 10 h human speech within 83.52 h total | "Creative Commons Attribution 4.0 International License (CC BY 4.0)" for the ASC-derived and synthetic parts; the professionally recorded human subset needs a separate data usage agreement |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Arabic-F5-TTS-v2](https://huggingface.co/IbrahimSalah/Arabic-F5-TTS-v2) | Modern Standard Arabic, requires fully diacritized input text | free download | not measured |
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox), Arabic | not stated | free download | not measured |

### Arabic, Moroccan Darija (ar-MA)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://huggingface.co/datasets/UBC-NLP/Casablanca) | Moroccan, one of 8 labelled dialects in a pooled release | not stated | "CC BY-NC-ND 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Morocco identifier | Moroccan | free download | UTMOS 1.98, WER-O 40.02 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Najdi and Hijazi (ar-SA)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SADA](https://huggingface.co/datasets/MohamedRashad/SADA22) | broadcast pool naming Najdi, Hijazi and Khaliji speakers, no per-dialect split given | not stated, over 667 h | "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [NAMAA-Saudi-TTS](https://huggingface.co/NAMAA-Space/NAMAA-Saudi-TTS) | Saudi, colloquial rather than Modern Standard Arabic | free download | not measured |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Saudi Arabia identifier | Saudi, pooled (not split into Najdi or Hijazi) | free download | UTMOS 1.68, WER-O 13.96 ([paper](https://arxiv.org/html/2601.13802v1)) |
| [SILMA TTS](https://silma.ai/tts) | Modern Standard Arabic and Saudi Najdi, with English code-switching | paid cloud service | not measured |

### Arabic, Qatari (ar-QA)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Hamsa](https://docs.tryhamsa.com/text-to-speech/introduction), `qat` voice code | Qatari | paid cloud service | not measured |

### Arabic, South Levantine (ajp)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Arabic Speech Corpus](https://en.arabicspeechcorpus.com/) | South Levantine, Damascene accent | one male speaker, not stated (1,813 utterances) | "Creative Commons Attribution 4.0 International License" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Levantine identifier | Levantine | free download | not measured |

### Arabic, Sudanese (ar-SD)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Sudanese dialect speech dataset](https://zenodo.org/records/7426918) | Sudanese, Khartoum-centred | not stated | "Creative Commons Attribution 4.0 International (CC-BY-4.0)" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Sudan identifier | Sudanese | free download | not measured |

### Arabic, Tunisian (ar-TN)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Tunisia identifier | Tunisian | free download | not measured |

### Azerbaijani (az-AZ)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Azure `az-AZ` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | paid cloud service | not measured |

### Balochi (bal)

No recordings or TTS voices that you can download are known.

### Hausa (ha)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Hausa, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Hausa-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |

No natural-sounding TTS voice is known.

### Hebrew (he-IL)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SASPEECH](https://www.openslr.org/134/) | not stated | one speaker, 30 h (4 h manually transcribed, 26 h machine-transcribed) | custom non-commercial, held by the Israeli Public Broadcasting Corporation |
| [ivrit.ai](https://huggingface.co/ivrit-ai) | not stated | many speakers, over 22,000 h | custom licence permitting commercial AI training |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox), Hebrew | not stated | free download | not measured |

### Igbo (ig)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Igbo, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Igbo-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |

No natural-sounding TTS voice is known.

### Kabyle (kab)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Kabyle, 26.0](https://huggingface.co/datasets/taqbaylit/common-voice-scripted-speech-kab-26-huge) | not stated | 1,330 speakers, about 520.4 h (567,727 clips) | CC0-1.0 |

### Kinyarwanda (rw-RW)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [kinyarwanda-speech-1000h](https://huggingface.co/datasets/badrex/kinyarwanda-speech-1000h) | not stated | not stated, about 1,000 h | Creative Commons Attribution 4.0 (CC BY 4.0) |

No natural-sounding TTS voice is known.

### Kurdish, Kurmanji (kmr)

No natural-sounding TTS voice is known.

### Kurdish, Sorani (ckb)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SoraniTTS](https://data.mendeley.com/datasets/jmtn248cc9/5) | Central Kurdish (Sorani) | one male speaker, about 19 h (6,565 sentence/audio pairs) | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Central Kurdish TTS](https://huggingface.co/aranemini/central-kurdish-tts) | Central Kurdish (Sorani) | free download | TTS MOS 4.08, character error rate 3.7-5.6% (model card) |

### Lingala (ln)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [lingala-speech-dataset](https://huggingface.co/datasets/shunyalabs/lingala-speech-dataset) | not stated | not stated (4,420 rows) | not stated |

No natural-sounding TTS voice is known.

### Luganda (lg-UG)

No natural-sounding TTS voice is known.

### Oromo (om)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Sagalee](https://openslr.org/157/) | not stated, mobile-app collected | not stated | "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)" |

No natural-sounding TTS voice is known.

### Pashto (ps-AF)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Pashto](https://commonvoice.mozilla.org/en/languages) | not stated | 1,483 contributors, 82.33 h validated of 147.07 h total | CC-0 |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Azure `ps-AF` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | paid cloud service | not measured |

### Persian (fa-IR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ManaTTS](https://github.com/MahtaFetrat/ManaTTS-Persian-Speech-Dataset) | not stated | one speaker, 86 h (paper) or 114 h (project README, the two sources disagree) | CC-0 1.0 |
| [ParsVoice](https://huggingface.co/datasets/MohammadJRanjbar/ParsVoice) | not stated | 1,815 speakers, 2,200 h | "CC BY-NC 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [ParsVoice-XTTS](https://huggingface.co/MohammadJRanjbar/ParsVoice-XTTS) fine-tune | not stated | free download | naturalness MOS 3.6, speaker-similarity MOS 4.0 ([paper](https://arxiv.org/abs/2510.10774)) |

### Pulaar (ff)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 32 h (11 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No natural-sounding TTS voice is known.

### Sereer (srr)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 38 h (11 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No natural-sounding TTS voice is known.

### Somali (so-SO)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [somali-speech-dataset](https://huggingface.co/datasets/shunyalabs/somali-speech-dataset) | not stated | not stated (4,600 rows) | not stated |

No natural-sounding TTS voice is known.

### Swahili (sw)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ALFFA](https://openslr.org/25/) | not stated | not stated | MIT |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Piper `lanfrica` ([voice list](https://github.com/rhasspy/piper/blob/master/VOICES.md)), language code `sw_CD` | Congolese, per its own language code | free download | not measured |

### Tachelhit (shi)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Tamazight-Speech-to-Arabic-Text](https://huggingface.co/datasets/EMINES/Tamazight-Speech-to-Arabic-Text) | Tachelhit | not stated, about 15.5 h | Apache-2.0 |

### Tamasheq (taq)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IWSLT 2022 Tamasheq speech data](https://github.com/mzboito/IWSLT2022_Tamasheq_data) | Tamasheq, aligned to French translations rather than Tamasheq-script transcripts, radio speech | not stated, 17 h clean / 19 h full labelled | Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported |

### Tamazight, Central Atlas (tzm)

No recordings or TTS voices that you can download are known.

### Tarifit, Riffian (rif)

No recordings or TTS voices that you can download are known.

### Tigrinya (ti-ET)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [tigrinya-speech](https://huggingface.co/datasets/badrex/tigrinya-speech) | `ti_ET` | 72 speakers, not stated (14,780 rows) | not stated |

No natural-sounding TTS voice is known.

### Turkish (tr-TR)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| Piper `tr_TR` ([voice list](https://github.com/rhasspy/piper/blob/master/VOICES.md)), voices `dfki`, `fahrettin`, `fettah` | not stated | free download | not measured |

### Twi, Asante (tw-GH)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Akiti-TTS](https://github.com/AfriSpeech/akiti-tts) (weights: [michsethowusu/Akiti-TTS](https://huggingface.co/michsethowusu/Akiti-TTS)) | Asante Twi | free download | not measured |

### Wolof (wo)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 55 h (13 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No natural-sounding TTS voice is known.

### Xhosa (xh-ZA)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 32](https://openslr.org/32/), isiXhosa portion | not stated | not stated (907 MB of audio) | "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" |

No natural-sounding TTS voice is known.

### Yoruba (yo)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Yoruba, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Yoruba-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |
| [OpenSLR 86](https://openslr.org/86/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice is known.

### Zulu (zu-ZA)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NCHLT isiZulu](https://huggingface.co/datasets/Max5ive/nchlt_speech_zulu) | isiZulu | not stated (44,673 rows) | "Creative Commons Attribution 3.0 Unported License (CC BY 3.0)" |

No natural-sounding TTS voice is known.

## Asia and the Pacific

### Bengali (bn-IN / bn-BD)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | Indian Bengali (bn-IN) | 617 speakers, 111.99 h | "CC BY 4.0" |
| [OpenSLR37](https://www.openslr.org/37/) | separate archives for Bangladesh Bengali (bn-BD) and Indian Bengali (bn-IN) | not stated | "Attribution-ShareAlike 4.0" |

### Bhojpuri (bho-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SYSPIN](https://vaani.iisc.ac.in/dataset/syspindataset) | pooled across 9 Indian languages; the Bhojpuri share of the total is not stated | not stated for Bhojpuri alone; the pooled total is 18 speakers, 920 h across 9 languages | "CC-BY-4.0" |

### Burmese (my-MM)

No recordings or TTS voices that you can download are known.

### Cantonese (yue)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [WenetSpeech-Yue](https://huggingface.co/datasets/ASLP-lab/WenetSpeech-Yue) | Cantonese, ten content domains | not stated, 21,800 h | "CC BY-NC 4.0" |

### Cebuano (ceb-PH)

No recordings or TTS voices that you can download are known.

### Gujarati (gu-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 45 speakers, 8.94 h | "CC BY 4.0" |
| [OpenSLR78](https://www.openslr.org/78/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

### Hakka (hak-TW)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [VoxHakka](https://huggingface.co/formospeech/yourtts-htia-240704) | Taiwanese Hakka, six dialects | free download | not measured |

### Hawaiian (haw-US)

No recordings or TTS voices that you can download are known.

### Hindi (hi-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SYSPIN](https://vaani.iisc.ac.in/dataset/syspindataset) | pooled across 9 Indian languages, per-language split not stated | 18 speakers, 920 h combined for all 9 languages | "CC-BY-4.0" |
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 399 speakers, 74.60 h | "CC BY 4.0" |
| [IndicTTS](https://voice.cis-india.org/indic-tts.html) | standard Hindi | 2 speakers, 20 h native + 20 h English | "available free of cost to researchers" on login; commercial use needs a Memorandum of Understanding |
| [OpenSLR118](https://www.openslr.org/118/) | not stated | 1,111 h (100 h labelled train, 5 h dev, 3 h eval, about 1,000 h unlabelled) | "can be used freely for academic purposes"; commercial use needs written permission |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper hi_IN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (pratham, priyamvada) | not stated | free download | not measured |
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | free download | not measured |
| [Chatterbox Multilingual, Hindi finetune](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-hi) | not stated | free download | not measured |

### Indonesian (id-ID)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Japanese (ja-JP)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kokoro-Speech-Dataset](https://github.com/kaiidams/Kokoro-Speech-Dataset) | standard Japanese | 1 speaker, about 59 h | public domain in the United States |
| [JSUT](https://sites.google.com/site/shinnosuketakamichi/publication/jsut) | standard Japanese | 1 speaker, 10 h | text: "CC-BY-SA 4.0"; audio for academic and non-commercial research and personal use, redistribution not permitted, commercial use by arrangement |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Style-Bert-VITS2, JVNV voices](https://huggingface.co/litagin/style_bert_vits2_jvnv) | standard Japanese | free download | [naturalness MOS 4.37 vs. 4.38 for human ground truth](https://arxiv.org/abs/2505.17320) |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) | standard Japanese | free download | not measured |

### Javanese (jv-ID)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR41](https://www.openslr.org/41/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Kannada (kn-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 452 speakers, 44.61 h | "CC BY 4.0" |

### Kazakh (kk-KZ)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR102](https://www.openslr.org/102/) | not stated | not stated, about 332 h | "Attribution 4.0 International" |
| [OpenSLR140](https://www.openslr.org/140/) | not stated | not stated, about 554 h | "Attribution-ShareAlike 3.0 Unported" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper kk_KZ](https://github.com/rhasspy/piper/blob/master/VOICES.md) (issai) | not stated | free download | not measured |

### Khmer (km-KH)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR42](https://www.openslr.org/42/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Korean (ko-KR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Zeroth Korean](https://github.com/goodatlas/zeroth) | standard Korean | 181 speakers, 95.7 h | "CC BY 4.0" |

### Kyrgyz (ky-KG)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Lao (lo-LA)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Maithili (mai-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 627 speakers, 81.77 h | "CC BY 4.0" |

### Malay (ms-MY)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Malayalam (ml-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 462 speakers, 82.57 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper ml_IN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (arjun, meera) | not stated | free download | not measured |
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | free download | not measured |

### Mandarin Chinese (zh-CN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR68, MAGICDATA](https://www.openslr.org/68/) | Putonghua, speakers from several accent regions of China | 1,080 speakers, 755 h | "Attribution-NonCommercial-NoDerivatives 4.0 International" |
| [OpenSLR121, WenetSpeech](https://www.openslr.org/121/) | multi-domain, not clean single-speaker | 22,400+ h total, over 10,000 h labelled | "Creative Commons Attribution 4.0 International (CC BY 4.0)" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox Multilingual, Mandarin finetune](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-zh-cmn) | not stated | free download | not measured |
| [Piper zh_CN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (huayan) | not stated | free download | not measured |

### Maori (mi-NZ)

No recordings or TTS voices that you can download are known.

### Marathi (mr-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 359 speakers, 50.90 h | "CC BY 4.0" |
| [OpenSLR64](https://www.openslr.org/64/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

### Marwari (mwr-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Vaani](https://huggingface.co/datasets/ARTPARK-IISc/Vaani) | Marwari is named among the 112 languages and dialects collected; hours for Marwari alone are not stated | not stated for Marwari alone; the whole corpus totals 31,270 h, about 2,067 h transcribed | "CC BY 4.0" |
| [IndicTTS](https://voice.cis-india.org/indic-tts.html) | listed as "Rajasthani", a macro-label that also covers Mewari and Dhundhari; not confirmed as Marwari specifically | 2 speakers, 20 h native + 20 h English | "available free of cost to researchers" on login; commercial use needs a Memorandum of Understanding |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [AI4Bharat Indic-TTS, Rajasthani model](https://github.com/AI4Bharat/Indic-TTS) | listed as "Rajasthani", not confirmed as Marwari specifically | free download | not measured |

### Mongolian (mn-MN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [MnTTS](https://github.com/walker-hyf/MnTTS) | Cyrillic-script standard Mongolian | 1 speaker, hours not stated | "Unlicense" |

### Nepali (ne-NP)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR43](https://www.openslr.org/43/) | Nepal, collected by Google | not stated | "Attribution-ShareAlike 4.0" |
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | India, not Nepal's standard variety | 716 speakers, 105.87 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper ne_NP](https://github.com/rhasspy/piper/blob/master/VOICES.md) (chitwan, google) | not stated | free download | not measured |

### Punjabi, Gurmukhi (pa-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | Gurmukhi-script, India | 335 speakers, 74.94 h | "CC BY 4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | free download | not measured |

### Punjabi, Shahmukhi (pa-PK)

No recordings or TTS voices that you can download are known.

### Samoan (sm-WS)

No recordings or TTS voices that you can download are known.

### Sindhi (sd-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | India-side Sindhi | 204 speakers, 10.48 h | "CC BY 4.0" |

### Sinhala (si-LK)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR52](https://www.openslr.org/52/) | not stated | about 185,000 utterances, hours not stated | "Attribution-ShareAlike 4.0 International" |

### Sundanese (su-ID)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR44](https://www.openslr.org/44/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Tagalog / Filipino (fil-PH)

No recordings or TTS voices that you can download are known.

### Tajik (tg-TJ)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Tamil (ta-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 1,084 speakers, 99.47 h | "CC BY 4.0" |

### Telugu (te-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | not stated | 681 speakers, 136.40 h | "CC BY 4.0" |

### Thai (th-TH)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [KhanomTan TTS v1.0](https://github.com/wannaphong/KhanomTan-TTS-v1.0) | Thai and English | free download | not measured |

### Tibetan, Lhasa (bo)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NICT-Tib1](https://www.openslr.org/158/) | Lhasa (Ü-Tsang) dialect | 20 speakers, 33.5 h | "Creative Commons Attribution 4.0 International" |

### Tongan (to-TO)

No recordings or TTS voices that you can download are known.

### Turkmen (tk-TM)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Urdu (ur-IN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://huggingface.co/datasets/ai4bharat/indicvoices_r) | India-side Urdu | 460 speakers, 78.61 h | "CC BY 4.0" |
| [Urdu Multi-Speaker TTS Dataset](https://mozilladatacollective.com/datasets/cmmvykcrs0050ny07vkwww5gi) | not stated | 3 speakers, about 10 h | "CC-BY-NC-4.0"; the licence also states the data may not be used to clone or imitate voices or to train text-to-speech systems |

### Uyghur (ug-CN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [THUYG-20](https://www.openslr.org/22/) | not stated | 348 speakers, 20 h train + 1 h test | "totally open and free" |

### Uzbek (uz-UZ)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [FeruzaSpeech](https://huggingface.co/datasets/k2speech/FeruzaSpeech) | Tashkent | 1 speaker, 60 h | "Creative Commons Attribution 4.0"; the authors must approve each download |

### Vietnamese (vi-VN)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [VIVOS](https://zenodo.org/record/7068130) | standard Vietnamese | 65 speakers, 15 h | "Creative Commons Attribution NonCommercial ShareAlike v4.0" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper vi_VN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (25hours_single, vais1000, vivos) | not stated | free download | not measured |

### Wu Chinese (wuu)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [WenetSpeech-Wu](https://huggingface.co/datasets/ASLP-lab/WenetSpeech-Wu) | 8 Wu sub-dialects | not stated, about 8,000 h | "Apache-2.0" |

## The Americas

### Aymara (aym)

No natural-sounding TTS voice for Aymara is known.

### Cherokee (chr)

No recordings or TTS voices that you can download are known.

### Cree, Plains (crk)

No recordings or TTS voices that you can download are known.

### English, American (en-US)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [LJ Speech](https://keithito.com/LJ-Speech-Dataset/) | American, accent not stated | 1 speaker, 13,100 clips, 23 h 55 min, 22,050 Hz | "Public Domain" |
| [Hi-Fi TTS](https://www.openslr.org/109/) | not stated, LibriVox readers | 10 speakers, about 291.6 h total, at least 17 h per speaker, 44.1 kHz | "CC BY 4.0" |
| [CORAAL](https://oraal.uoregon.edu/coraal) | African American Language, region-labelled across multiple US cities | over 220 sociolinguistic interviews, speakers born 1888-2005; hours not stated on the fetched page | not stated |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Kokoro-82M (af_heart)](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) | American, trained on American English voice data | free download | Overall Grade A, published on the model's own voice table |

### English, Canadian (en-CA)

No recordings or TTS voices that you can download are known.

### French, Acadian (fr)

No recordings or TTS voices that you can download are known.

### French, Québécois (fr-CA)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Google Chirp 3 HD (fr-CA)](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) | Canadian French, listed as a locale distinct from France French | paid cloud service | not measured |

### Guaraní, Paraguayan (gn)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Haitian Creole (ht)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [F5-TTS-OpenBible-Haitian-Creole](https://huggingface.co/multilingual-tts/F5-TTS-OpenBible-Haitian-Creole) | Haitian Creole | free download | not measured |

### Inuktitut (iu)

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Azure neural TTS, Inuktitut](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) | `iu-Cans-CA-SiqiniqNeural` and `iu-Cans-CA-TaqqiqNeural` (Syllabics); matching Latin-script voices also exist | paid cloud service | not measured |

No free recordings of Inuktitut are known.

### Jamaican Patois (jam)

No natural-sounding TTS voice for Jamaican Patois is known.

### K'iche' (quc)

Mozilla Data Collective has recordings of this language: see [its list](mozilla-data-collective.md).

### Mapudungun (arn)

No natural-sounding TTS voice for Mapudungun is known. The recordings come with an older statistical voice (CLUSTERGEN), which does not sound natural.

### Mixtec, Yoloxóchitl (xty)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Yoloxóchitl-Mixtec](https://www.openslr.org/89/) | Yoloxóchitl Mixtec, field-recorded, ELAN time-coded | speaker count and hours not stated on the resource page (86 GB archive) | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No natural-sounding TTS voice for Mixtec is known.

### Nahuatl, Highland Puebla (azz)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Puebla-Nahuatl](https://www.openslr.org/92/) | Sierra Nororiental / Sierra Norte de Puebla, field-recorded conversation, ELAN time-coded | speaker count and hours not stated on the resource page (about 84.8 GB of audio) | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No natural-sounding TTS voice for Nahuatl is known.

### Navajo (nv)

No recordings or TTS voices that you can download are known.

### Papiamento (pap)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Speech-to-text dataset for keyword spotting within a healthcare environment](https://zenodo.org/records/15794240) | Papiamento, one-second isolated-word clips (numbers, yes/no, unknowns) | about 280 contributors, 16,766 samples after filtering | "Apache License 2.0" |

No natural-sounding TTS voice for Papiamento is known.

### Portuguese, Brazilian (pt-BR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [TTS-Portuguese Corpus](https://github.com/Edresson/TTS-Portuguese-Corpus) | Brazilian | 1 speaker, 10 h 28 min, 48 kHz, 3,632 files | "Creative Commons Attribution 4.0 (CC BY 4.0)" |
| [CORAA](https://github.com/nilc-nlp/CORAA) | Brazilian (five sub-corpora by region) plus 4.69 h of European Portuguese in the same release | 290.77 h validated, 400k+ segmented clips | not stated |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-pt-br) (Brazilian Portuguese finetune) | Brazilian | free download | not measured |
| [Piper pt_BR-faber](https://github.com/rhasspy/piper) | Brazilian | free download | not measured |
| [Piper pt_BR-cadu](https://github.com/rhasspy/piper) | Brazilian | free download | not measured |
| [Piper pt_BR-jeff](https://github.com/rhasspy/piper) | Brazilian | free download | not measured |
| [Piper pt_BR-edresson](https://github.com/rhasspy/piper) | Brazilian | free download | not measured |

### Quechua, Central (qu)

No natural-sounding TTS voice for Central Quechua is known.

### Quechua, Southern (quy)

No natural-sounding TTS voice for Southern Quechua is known.

### Shipibo-Konibo (shp)

No natural-sounding TTS voice for Shipibo-Konibo is known.

### Spanish, Argentinian (es-AR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Argentinian Spanish speech data set](https://www.openslr.org/61/) | Argentinian, recorded in Buenos Aires | 44 native speakers (paper); 5,739 recordings; hours not split out on the resource page | "Attribution-ShareAlike 4.0 International" |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Piper es_AR-daniela](https://github.com/rhasspy/piper) | Argentinian | free download | not measured |

### Spanish, Chilean (es-CL)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Chilean Spanish speech data set](https://www.openslr.org/71/) | Chilean, recorded in Santiago | 31 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice trained on Chilean Spanish is known.

### Spanish, Colombian (es-CO)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Colombian Spanish speech data set](https://www.openslr.org/72/) | Colombian, recorded in Bogotá | 33 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice trained on Colombian Spanish is known.

### Spanish, Mexican (es-MX)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [CIEMPIESS](https://ciempiess.org/downloads) | Mexican, radio broadcast (moderator and guests, legal-affairs domain) | multi-speaker (78% male / 22% female); 17 h | "Creative Commons Attribution-ShareAlike 4.0 International License" |
| [Common Voice Scripted Speech 26.0 - Mexican Spanish (Female)](https://mozilladatacollective.com/datasets/cmr3zunmk00flnt07p7ai9p43) | Mexican, self-reported accent (Mexico City, central Mexico, Oaxaca, San Luis Potosí and elsewhere); female speakers only | 59,560 train / 158 dev / 186 test clips, about 84 h | CC0-1.0 |

**TTS voices**

| Voice | Variety | Access | Published quality |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-mx-latam) (Latin American Spanish finetune) | Latin American Spanish (es-419/es-MX) | free download | not measured |
| [Piper es_MX-claude](https://github.com/rhasspy/piper) | Mexican | free download | not measured |
| [Piper es_MX-ald](https://github.com/rhasspy/piper) | Mexican | free download | not measured |

### Spanish, Peruvian (es-PE)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Peruvian Spanish speech data set](https://www.openslr.org/73/) | Peruvian, recorded in Lima | 38 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice trained on Peruvian Spanish is known.

### Spanish, Puerto Rican (es-PR)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Puerto Rico Spanish speech data set](https://www.openslr.org/74/) | Puerto Rican; recorded in the continental United States, not on the island; the resource page ships female-speaker files only | 5 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice trained on Puerto Rican Spanish is known.

### Spanish, Venezuelan (es-VE)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Venezuelan Spanish speech data set](https://www.openslr.org/75/) | Venezuelan; recorded in the United States and the United Kingdom, not in Venezuela | 23 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No natural-sounding TTS voice trained on Venezuelan Spanish is known.

### Totonac, Highland (tos)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Totonac Resources](https://www.openslr.org/107/) | Highland Totonac, communities of Ecatlán, Nanacatlán, Tonalixco and Zongozotla, field-recorded | speaker count and hours not stated on the resource page | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No natural-sounding TTS voice for Totonac is known.

### Wayuu (guc)

No recordings or TTS voices that you can download are known.

### Yucatec Maya (yua)

**Recordings**

| Recordings | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Yucatec Maya, DoReCo](https://doreco.huma-num.fr/languages/yuca1254) | Yucatec Maya, translated to Spanish | not stated | not stated |

No natural-sounding TTS voice for Yucatec Maya is known.

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
