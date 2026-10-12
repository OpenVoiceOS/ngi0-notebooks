# TTS voice data sources

This page lists speech sources for building a single-speaker text-to-speech dataset in a language or dialect. There are two kinds of source. A real speech corpus supplies source audio for voice conversion to one speaker. A donor TTS engine renders text in the right dialect and supplies synthetic source audio instead. The Basis column gives a published quality figure where one exists. The Licence column quotes each source's stated licence. The notebook that uses these sources is [`notebooks/tts_dataset_gen.ipynb`](../notebooks/tts_dataset_gen.ipynb).

## Europe

### Albanian, Gheg (aln)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice, Gheg Albanian](https://mozilladatacollective.com/datasets/cmmytg2r000eynz07epeq9u30) | Gheg | not stated | not stated |

### Albanian, Tosk (sq)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | Tosk | not stated | "CC0-1.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [SpeechGen](https://speechgen.io/en/) | Tosk | no | not measured |

### Alsatian (gsw-FR)

No open corpus or human-like TTS is known.

### Aragonese (an)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | not stated | not stated | "CC0-1.0" |

### Armenian (hy)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 160](https://www.openslr.org/160/) | Armenian | not stated, 70 h | "CC BY 4.0" |

### Aromanian (rup)

No open corpus or human-like TTS is known.

### Asturian (ast)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | not stated | not stated | "CC0-1.0" |

### Basque (eu)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 76](https://www.openslr.org/76/) | Basque | not stated | "Attribution-ShareAlike 4.0 International" |
| [HiTZ-Aholab speech synthesis dataset](https://zenodo.org/records/17952596) | Basque | 2 speakers, about 34.25 h combined | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [HiTZ/TTS-eu_antton](https://huggingface.co/HiTZ/TTS-eu_antton) | Basque | yes | not measured |

### Belarusian (be)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | not stated | not stated | "CC0-1.0" |

### Bosnian (bs)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Bosnia-Herzegovina subset) | not stated | not stated, 167,000 rows | "other" |

### Breton (br)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Audio Breton Corpus](https://huggingface.co/datasets/Bretagne/audio-breton-corpus) | Breton | 2 speakers, about 33.7 h combined | not stated |

### Bulgarian (bg)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Bulgaria subset) | not stated | not stated, 528,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (bg-BG) | Bulgarian | no | not measured |

### Catalan (ca)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [festcat](https://huggingface.co/datasets/projecte-aina/festcat_trimmed_denoised) | Central | 11 speakers, 22.91 h | "CC BY-SA 3.0" |
| [LaFresCat](https://huggingface.co/datasets/projecte-aina/LaFrescat) | Balearic, Central, North-Western, Valencian | 8 speakers, 3.75 h | "CC BY-NC 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Matxa multiaccent](https://huggingface.co/projecte-aina/matxa-tts-cat-multiaccent) | Balearic, Central, North-Western, Valencian | yes | not measured |

### Cornish (kw)

No open corpus or human-like TTS is known.

### Corsican (co)

No open corpus or human-like TTS is known.

### Croatian (hr)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ParlaSpeech 3.0](https://arxiv.org/html/2511.01619) | Croatian | not stated, 3,110 h | "CC BY-SA 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (hr-HR) | Croatian | no | not measured |

### Czech (cs)

No open corpus of Czech speech with a working link was found.

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (jirka, low/medium) | Czech | yes | not measured |

### Danish (da-DK)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Denmark subset) | not stated | not stated, 1,560,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Danish | yes | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (talesyntese, medium) | Danish | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (da-DK) | Danish | no | not measured |

### Dutch, Flemish (nl-BE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [GCND](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.536) | French Flemish, West Flemish, East Flemish, Zeelandic Flemish, Flemish Brabant, Belgian Limburgish | 653 recordings, hours not stated | "CC-BY-SA, non-commercial research only" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nl-BE) | Flemish | no | not measured |

### Dutch, Netherlands (nl-NL)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Corpus Gesproken Nederlands](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/) | Netherlands and Flemish, split not stated | not stated, 900 h | "free, signed licence agreement required" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Dutch, variety not stated | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nl-NL) | Netherlands Dutch | no | not measured |

### English, British and Irish (en-GB)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 83](https://www.openslr.org/83/) | Irish, Midlands, Northern England, Scottish, Southern England, Welsh | 120 volunteers, 31 h | "Attribution-ShareAlike 4.0 International" |
| [GLOBE](https://huggingface.co/datasets/MushanW/GLOBE) | 164 accents worldwide, including UK and Ireland | 23,519 speakers, 535 h | "CC0-1.0" |

### Estonian (et)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Estonia subset) | not stated | not stated, 215,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (et-EE) | Estonian | no | not measured |

### Faroese (fo)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Basic LAnguage Resource Kit 1.0](https://www.openslr.org/125/) | six named dialect areas | 433 speakers, 100 h | "CC BY 4.0" |

### Finnish (fi)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [FinSyn](https://blogs.helsinki.fi/speech-synthesis/2022/05/13/finsyn-a-new-speech-synthesis-corpus-for-finnish/) | Finnish | 2 speakers, about 60 h | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Finnish | yes | not measured |

### Franco-Provençal (frp)

No open corpus or human-like TTS is known.

### Galician (gl)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Nos_Celtia-GL](https://zenodo.org/records/7716958) | Galician | 1 speaker, about 25 h | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [HiTZ/TTS-gl_sabela](https://huggingface.co/HiTZ/TTS-gl_sabela) | Galician | yes | not measured |

### Georgian (ka)

No open corpus or human-like TTS with a working link was found.

### German (de-DE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Thorsten](https://www.openslr.org/95/) | German | 1 speaker, more than 23 h | "CC0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | German | yes | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (thorsten, low/medium/high) | German | yes | not measured |

### German, Swiss (gsw-CH)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [STT4SG-350](https://zenodo.org/records/10012816) | all Swiss German dialect regions | 316 speakers, 343 h | "META-SHARE NonCommercial NoRedistribution License" |

### Greek (el)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | not stated | not stated | "CC0-1.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (rapunzelina, low) | Greek | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (el-GR) | Greek | no | not measured |

### Greek, regional (Cypriot, Cretan, Pontic)

No open corpus or human-like TTS is known.

### Hungarian (hu)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [KTH Hungarian single-speaker TTS](https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts) | Hungarian | 1 speaker, 4,515 segments (hours not stated) | "CC0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (3 voices) | Hungarian | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (hu-HU) | Hungarian | no | not measured |

### Icelandic (is)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Samrómur 21.05](https://www.openslr.org/112/) | Icelandic | 8,392 speakers, 145 h | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (4 voices) | Icelandic | yes | not measured |

### Irish (ga)

No open corpus of Irish speech was found.

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [ABAIR](https://www.abair.ie) | Irish, variety not stated | no | not measured |

### Italian, Friulian (fur)

No open corpus or human-like TTS is known.

### Italian, Ladin (lld)

No open corpus or human-like TTS is known.

### Italian, Lombard (lmo)

No open corpus or human-like TTS is known.

### Italian, Neapolitan (nap)

No open corpus or human-like TTS is known.

### Italian, Piedmontese (pms)

No open corpus or human-like TTS is known.

### Italian, Sardinian (sc)

No open corpus or human-like TTS is known.

### Italian, Sicilian (scn)

No open corpus or human-like TTS is known.

### Italian, Venetian (vec)

No open corpus or human-like TTS is known.

### Karelian (krl)

No open corpus or human-like TTS is known.

### Kashubian (csb)

No open corpus or human-like TTS is known.

### Latgalian (ltg)

No open corpus or human-like TTS is known.

### Latvian (lv)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Latvia subset) | not stated | not stated, 292,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (aivars, medium) | Latvian | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (lv-LV) | Latvian | no | not measured |

### Lithuanian (lt)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [LIEPA](https://informatica.vu.lt/journal/INFORMATICA/article/1083/read) (synthesis part) | Lithuanian | 4 speakers, 13 h | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (lt-LT) | Lithuanian | no | not measured |

### Livonian (liv)

No open corpus or human-like TTS is known.

### Low German (nds)

No open corpus or human-like TTS with a working link was found.

### Luxembourgish (lb)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [luxembourgish-speech-dataset](https://huggingface.co/datasets/shunyalabs/luxembourgish-speech-dataset) | not stated | not stated, 3,844 rows | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (marylux, medium) | Luxembourgish | yes | not measured |

### Macedonian (mk)

No open corpus or human-like TTS with a working link was found.

### Maltese (mt)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [MASRI-HEADSET](https://aclanthology.org/2020.lrec-1.784/) | Maltese | not stated, 8 h | "publicly available for research and academic purposes" |

### Manx (gv)

No open corpus or human-like TTS is known.

### Mirandese (mwl)

No open corpus or human-like TTS is known.

### Norwegian, Bokmål (nb-NO)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NPSC](https://huggingface.co/datasets/NbAiLab/NPSC) | 87.2% Bokmål, 12.8% Nynorsk | not stated, 140.3 h including pauses | "CC0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Norwegian | yes | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (talesyntese, medium) | Norwegian | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (nb-NO) | Norwegian Bokmål | no | not measured |

### Occitan (oc)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ReVoc](https://zenodo.org/records/11566430) | Aranese, Auvergnat, Gascon, Limousin, Languedocian, Niçard, Provençal, Vivaro-Alpine | not stated, 40,000+ files | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Votz](https://votz.eu) | Gascon, Languedocian | no | not measured |

### Polish (pl)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [MC Speech Dataset](https://www.openslr.org/142/) | Polish | 1 speaker, more than 22 h | "CC0 1.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Polish | yes | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (4 voices) | Polish | yes | not measured |

### Portuguese, European (pt-PT)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [FalAR](https://huggingface.co/datasets/inesc-id/FalAR) | European | 1,180 speakers, about 4.9k h of parliamentary sessions, 16 kHz; the rooms carry heavy echo, so the audio needs enhancement (for example [callenhancer](https://huggingface.co/TigreGotico/audiosronnx-callenhancer)) before use | "cc-by-4.0" |
| [Tugão 1.0](https://mozilladatacollective.com/datasets/cmiui8v3101cpnv074qwggdsj) | European | 1 speaker, about 1.5 h | "CC0-1.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Azure neural voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) | European (pt-PT locale) | no | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (tugão, medium) | European | yes | not measured |

### Romani (rom)

No open corpus or human-like TTS is known.

### Romanian (ro)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [romanian-speech-v2](https://huggingface.co/datasets/eduardem/romanian-speech-v2) | Romanian | 21 speakers, 360.16 h | "released strictly for personal research and educational purposes" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [F5-TTS-RO](https://github.com/racai-ro/Ro-F5TTS) | Romanian | not stated | not measured |

### Romanian, Moldovan (ro-MD)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Moldovan dialectal Romanian speech corpus](https://huggingface.co/datasets/FraPiz/moldovan-dialectal-romanian-speech-corpus) | Moldovan | about 56 speakers, 70.67 h | "source-content-rights-reserved" |

### Romansh (rm)

No open corpus or human-like TTS is known.

### Russian (ru)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [RUSLAN](https://ruslan-corpus.github.io/) | Russian | 1 speaker, 31+ h | "CC BY-NC-SA 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Russian | yes | not measured |

### Rusyn (rue)

No open corpus or human-like TTS is known.

### Sami, Lule (smj)

No open corpus or human-like TTS with a working link was found.

### Sami, Northern (se)

No open corpus or human-like TTS with a working link was found.

### Scottish Gaelic (gd)

No open corpus or human-like TTS is known.

### Serbian (sr)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ParlaSpeech 3.0](https://arxiv.org/html/2511.01619) | Serbian | not stated, 896 h | "CC BY-SA 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (serbski_institut, medium) | Serbian | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sr-RS) | Serbian | no | not measured |

### Slovak (sk)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SloPalSpeech](https://arxiv.org/abs/2509.19270) | Slovak | not stated, 2,806 h | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (lili, medium) | Slovak | yes | not measured |

### Slovenian (sl)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Slovenia subset) | not stated | not stated, 278,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (artur, medium) | Slovenian | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sl-SI) | Slovenian | no | not measured |

### Sorbian (hsb)

No open corpus or human-like TTS is known.

### Spanish, Castilian (es-ES)

No open corpus of confirmed Castilian speech was found.

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-es) (Spain finetune) | Castilian | yes | not measured |
| [Azure neural TTS](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) (es-ES, 19+ voices) | Castilian | no | not measured |

### Swedish (sv-SE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Sweden subset) | not stated | not stated, 556,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox) | Swedish | yes | not measured |
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices) | Swedish | yes | not measured |
| [Google Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) (sv-SE) | Swedish | no | not measured |

### Ukrainian (uk)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [EuroSpeech](https://huggingface.co/datasets/disco-eth/EuroSpeech) (Ukraine subset) | not stated | not stated, 283,000 rows | "other" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices) | Ukrainian | yes | not measured |

### Welsh (cy)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Welsh](https://huggingface.co/datasets/techiaith/commonvoice_16_1_cy) | not stated | 1,832 speakers, 155.12 h recorded, 122.22 h validated | "CC0-1.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper](https://github.com/rhasspy/piper/blob/master/VOICES.md) (2 voices, medium) | Welsh | yes | not measured |

### West Frisian (fy-NL)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice](https://commonvoice.mozilla.org/en/languages) | not stated | not stated | "CC0-1.0" |

### Yiddish (yi)

No open corpus or human-like TTS is known.

## Middle East and Africa

### Afrikaans (af-ZA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NCHLT Afrikaans](https://repo.sadilar.org/handle/20.500.12185/280) | not stated | 8 speakers in its test suite, about 56 h | Creative Commons Attribution 3.0 Unported (CC BY 3.0) |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Azure `af-ZA` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | no | not measured |

### Amharic (am-ET)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ALFFA](https://openslr.org/25/) | not stated | not stated | MIT |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Azure `am-ET` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | no | not measured |

### Arabic, Algerian Darja (ar-DZ)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://aclanthology.org/2024.emnlp-main.1211/) | Algerian, one of 8 labelled dialects in a pooled release | not stated | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Hadra-TTS-f5](https://huggingface.co/algerian-nlp/Hadra-TTS-f5) | Algerian Darja | yes | not measured (about 399 h of training audio, model card) |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Algeria identifier | Algerian | yes | UTMOS 2.46, WER-O 31.18 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Classical (ar)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ClArTTS](https://huggingface.co/datasets/MBZUAI/ClArTTS) | Classical Arabic, not Modern Standard | one male speaker, about 12 h | "cc-by-4.0" |

No human-like TTS is known.

### Arabic, Egyptian (ar-EG)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [F5-TTS Egyptian Arabic](https://huggingface.co/MAdel121/f5-tts-egyptian-arabic) | Egyptian, inherits about 85% Modern Standard Arabic from its base | yes | UTMOS 2.63, WER 20.4% with a Whisper Small Arabic recogniser (model card) |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Egypt identifier | Egyptian | yes | UTMOS 2.14, WER-O 18.58 ([paper](https://arxiv.org/html/2601.13802v1)) |
| [NAMAA-Egyptian-TTS](https://huggingface.co/NAMAA-Space/NAMAA-Egyptian-TTS) | Egyptian, everyday conversational speech | yes | not measured |

### Arabic, Emirati (ar-AE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Ramsa](https://aclanthology.org/2026.lrec-1.250/) | Emirati, spanning Urban, Bedouin and Mountain (Shihhi) sub-dialects | 157 speakers (59 female, 98 male), 41 h | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), UAE identifier | Emirati | yes | UTMOS 2.75, WER-O 5.15, speaker similarity 0.782 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Iraqi (ar-IQ)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Ghadeer speech crowd corpus](https://pmc.ncbi.nlm.nih.gov/articles/PMC11754659/) | Iraqi, more than one accent | 210 speakers, 15,626 samples | "CC BY" |
| [Iraqi Dialect TTS Corpus](https://github.com/hayderkharrufa/iraqi-dialect-tts-corpus) | Iraqi, with the extra Iraqi phonemes گ چ پ ڤ ۆ ڵ ێ | not stated | "Creative Commons Attribution 4.0 International License (CC BY 4.0)" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Iraq identifier | Iraqi | yes | UTMOS 2.48, WER-O 17.12 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Mauritanian (ar-MR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://aclanthology.org/2024.emnlp-main.1211/) | Mauritanian, one of 8 labelled dialects in a pooled release | not stated | not stated |

No human-like TTS is known.

### Arabic, Modern Standard, diacritized (ar)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ArVoice](https://arxiv.org/html/2505.20506v1) | Modern Standard Arabic, diacritized, read by speakers native to Egypt, Jordan, Morocco, Palestine and Syria | 7 human voices, about 10 h human speech within 83.52 h total | "Creative Commons Attribution 4.0 International License (CC BY 4.0)" for the ASC-derived and synthetic parts; the professionally recorded human subset needs a separate data usage agreement |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Arabic-F5-TTS-v2](https://huggingface.co/IbrahimSalah/Arabic-F5-TTS-v2) | Modern Standard Arabic, requires fully diacritized input text | yes | not measured |
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox), Arabic | not stated | yes | not measured |

### Arabic, Moroccan Darija (ar-MA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Casablanca](https://aclanthology.org/2024.emnlp-main.1211/) | Moroccan, one of 8 labelled dialects in a pooled release | not stated | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Morocco identifier | Moroccan | yes | UTMOS 1.98, WER-O 40.02 ([paper](https://arxiv.org/html/2601.13802v1)) |

### Arabic, Najdi and Hijazi (ar-SA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SADA](https://huggingface.co/datasets/MohamedRashad/SADA22) | broadcast pool naming Najdi, Hijazi and Khaliji speakers, no per-dialect split given | not stated, over 667 h | "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [NAMAA-Saudi-TTS](https://huggingface.co/NAMAA-Space/NAMAA-Saudi-TTS) | Saudi, colloquial rather than Modern Standard Arabic | yes | not measured |
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Saudi Arabia identifier | Saudi, pooled (not split into Najdi or Hijazi) | yes | UTMOS 1.68, WER-O 13.96 ([paper](https://arxiv.org/html/2601.13802v1)) |
| [SILMA TTS](https://silma.ai/tts) | Modern Standard Arabic and Saudi Najdi, with English code-switching | no | not measured |

### Arabic, Qatari (ar-QA)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Hamsa](https://docs.tryhamsa.com/text-to-speech/introduction), `qat` voice code | Qatari | no | not measured |

### Arabic, South Levantine (ajp)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Arabic Speech Corpus](https://en.arabicspeechcorpus.com/) | South Levantine, Damascene accent | one male speaker, not stated (1,813 utterances) | "Creative Commons Attribution 4.0 International License" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Levantine identifier | Levantine | yes | not measured |

### Arabic, Sudanese (ar-SD)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Sudanese dialect speech dataset](https://zenodo.org/records/7426918) | Sudanese, Khartoum-centred | not stated | "Creative Commons Attribution 4.0 International (CC-BY-4.0)" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Sudan identifier | Sudanese | yes | not measured |

### Arabic, Tunisian (ar-TN)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Habibi](https://huggingface.co/SWivid/Habibi-TTS), Tunisia identifier | Tunisian | yes | not measured |

### Azerbaijani (az-AZ)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Azure `az-AZ` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | no | not measured |

### Balochi (bal)

No open corpus or human-like TTS is known.

### Hausa (ha)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Hausa, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Hausa-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |

No human-like TTS is known.

### Hebrew (he-IL)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SASPEECH](https://www.openslr.org/134/) | not stated | one speaker, 30 h (4 h manually transcribed, 26 h machine-transcribed) | custom non-commercial, held by the Israeli Public Broadcasting Corporation |
| [ivrit.ai](https://ivrit.ai) | not stated | many speakers, over 22,000 h | custom licence permitting commercial AI training |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual](https://huggingface.co/ResembleAI/chatterbox), Hebrew | not stated | yes | not measured |

### Igbo (ig)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Igbo, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Igbo-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |

No human-like TTS is known.

### Kabyle (kab)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Kabyle, 26.0](https://huggingface.co/datasets/taqbaylit/common-voice-scripted-speech-kab-26-huge) | not stated | 1,330 speakers, about 520.4 h (567,727 clips) | CC0-1.0 |

### Kinyarwanda (rw-RW)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [kinyarwanda-speech-1000h](https://huggingface.co/datasets/badrex/kinyarwanda-speech-1000h) | not stated | not stated, about 1,000 h | Creative Commons Attribution 4.0 (CC BY 4.0) |

No human-like TTS is known.

### Kurdish, Kurmanji (kmr)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [KASET](https://catalog.ldc.upenn.edu/LDC2024S01) | Kurmanji and Sorani together | not stated, about 147 h (about 60 h transcribed) | LDC User Agreement, paid access |

No human-like TTS is known.

### Kurdish, Sorani (ckb)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SoraniTTS](https://data.mendeley.com/datasets/jmtn248cc9/5) | Central Kurdish (Sorani) | one male speaker, about 19 h (6,565 sentence/audio pairs) | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Central Kurdish TTS](https://huggingface.co/aranemini/central-kurdish-tts) | Central Kurdish (Sorani) | yes | TTS MOS 4.08, character error rate 3.7-5.6% (model card) |

### Lingala (ln)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [lingala-speech-dataset](https://huggingface.co/datasets/shunyalabs/lingala-speech-dataset) | not stated | not stated (4,420 rows) | not stated |

No human-like TTS is known.

### Luganda (lg-UG)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Luganda crowdsourced TTS set](https://pmc.ncbi.nlm.nih.gov/articles/PMC12337013/) | not stated | 6 female speakers, about 19.2 h (7,842 utterances), filtered to WV-MOS 3.5 or above | Creative Commons Attribution, via Common Voice |

No human-like TTS is known.

### Oromo (om)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Sagalee](https://openslr.org/157/) | not stated, mobile-app collected | not stated | "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)" |

No human-like TTS is known.

### Pashto (ps-AF)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Common Voice Pashto](https://arxiv.org/html/2603.27021v1) | not stated | 1,483 contributors, 82.33 h validated of 147.07 h total | CC-0 |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Azure `ps-AF` ([voice list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)) | not stated | no | not measured |

### Persian (fa-IR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ManaTTS](https://github.com/MahtaFetrat/ManaTTS-Persian-Speech-Dataset) | not stated | one speaker, 86 h (paper) or 114 h (project README, the two sources disagree) | CC-0 1.0 |
| [ParsVoice](https://arxiv.org/abs/2510.10774) | not stated | 1,815 speakers, 2,200 h | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [ParsVoice-XTTS](https://huggingface.co/MohammadJRanjbar/ParsVoice-XTTS) fine-tune | not stated | yes | naturalness MOS 3.6, speaker-similarity MOS 4.0 ([paper](https://arxiv.org/abs/2510.10774)) |

### Pulaar (ff)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 32 h (11 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No human-like TTS is known.

### Sereer (srr)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 38 h (11 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No human-like TTS is known.

### Somali (so-SO)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [somali-speech-dataset](https://huggingface.co/datasets/shunyalabs/somali-speech-dataset) | not stated | not stated (4,600 rows) | not stated |

No human-like TTS is known.

### Swahili (sw)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [ALFFA](https://openslr.org/25/) | not stated | not stated | MIT |
| [Kiswahili crowdsourced TTS set](https://pmc.ncbi.nlm.nih.gov/articles/PMC12337013/) | not stated | 6 female speakers, about 15.1 h (6,324 utterances), filtered to WV-MOS 3.5 or above | Creative Commons Attribution, via Common Voice |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Piper `lanfrica` ([voice list](https://github.com/rhasspy/piper/blob/master/VOICES.md)), language code `sw_CD` | Congolese, per its own language code | yes | not measured |

### Tachelhit (shi)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Tamazight-Speech-to-Arabic-Text](https://huggingface.co/datasets/EMINES/Tamazight-Speech-to-Arabic-Text) | Tachelhit | not stated, about 15.5 h | Apache-2.0 |

### Tajik (tg)

No open corpus or human-like TTS is known.

### Tamasheq (taq)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IWSLT 2022 Tamasheq speech data](https://github.com/mzboito/IWSLT2022_Tamasheq_data) | Tamasheq, aligned to French translations rather than Tamasheq-script transcripts, radio speech | not stated, 17 h clean / 19 h full labelled | Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported |

### Tamazight, Central Atlas (tzm)

No open corpus or human-like TTS is known.

### Tarifit, Riffian (rif)

No open corpus or human-like TTS is known.

### Tigrinya (ti-ET)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [tigrinya-speech](https://huggingface.co/datasets/badrex/tigrinya-speech) | `ti_ET` | 72 speakers, not stated (14,780 rows) | not stated |

No human-like TTS is known.

### Turkish (tr-TR)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| Piper `tr_TR` ([voice list](https://github.com/rhasspy/piper/blob/master/VOICES.md)), voices `dfki`, `fahrettin`, `fettah` | not stated | yes | not measured |

### Turkmen (tk)

No open corpus or human-like TTS is known.

### Twi, Asante (tw-GH)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Akiti-TTS](https://github.com/AfriSpeech/akiti-tts) (weights: [michsethowusu/Akiti-TTS](https://huggingface.co/michsethowusu/Akiti-TTS)) | Asante Twi | yes | not measured |

### Wolof (wo)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kallaama](https://openslr.org/151/) | not stated, spontaneous radio and interview speech | not stated, 55 h (13 h validated) | Creative Commons Attribution 4.0 International (CC-BY-4.0) |

No human-like TTS is known.

### Xhosa (xh-ZA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR 32](https://openslr.org/32/), isiXhosa portion | not stated | not stated (907 MB of audio) | "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" |

No human-like TTS is known.

### Yoruba (yo)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NaijaVoices](https://huggingface.co/datasets/naijavoices/naijavoices-dataset) | Yoruba, one of three languages in a pooled release (1,800 h and over 5,000 speakers total across Hausa, Yoruba and Igbo; the Yoruba-only split is not stated) | not stated | "cc-by-nc-sa-4.0" |
| [OpenSLR 86](https://openslr.org/86/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

No human-like TTS is known.

### Zulu (zu-ZA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NCHLT isiZulu](https://huggingface.co/datasets/Max5ive/nchlt_speech_zulu) | isiZulu | not stated (44,673 rows) | "Creative Commons Attribution 3.0 Unported License (CC BY 3.0)" |

No human-like TTS is known.

## Asia and the Pacific

### Bengali (bn-IN / bn-BD)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | Indian Bengali (bn-IN) | 617 speakers, 111.99 h | "CC BY 4.0" |
| [OpenSLR37](https://www.openslr.org/37/) | separate archives for Bangladesh Bengali (bn-BD) and Indian Bengali (bn-IN) | not stated | "Attribution-ShareAlike 4.0" |

### Bhojpuri (bho-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SYSPIN](https://vaani.iisc.ac.in/dataset/syspindataset) | pooled across 9 Indian languages; the Bhojpuri share of the total is not stated | not stated for Bhojpuri alone; the pooled total is 18 speakers, 920 h across 9 languages | "CC-BY-4.0" |

### Burmese (my-MM)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Burmese speech corpus, LREC 2020](https://aclanthology.org/2020.lrec-1.777.pdf) | not stated | not stated | not stated |

### Cantonese (yue)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [WenetSpeech-Yue](https://github.com/ASLP-lab/WenetSpeech-Yue) | Cantonese, ten content domains | not stated, 21,800 h | "Apache-2.0" |

### Cebuano (ceb-PH)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Philippine Languages Database](https://sigul-2024.ilc.cnr.it/wp-content/uploads/2024/05/Cajote-et-al.pdf) | Cebuano, one of ten Philippine languages in this corpus, its own split not stated | not stated | not stated |

### Gujarati (gu-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 45 speakers, 8.94 h | "CC BY 4.0" |
| [OpenSLR78](https://www.openslr.org/78/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

### Hakka (hak-TW)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [VoxHakka](https://huggingface.co/formospeech/yourtts-htia-240704) | Taiwanese Hakka, six dialects | yes | not measured |

### Hawaiian (haw-US)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Text-to-speech on Edge Devices for Te Reo Māori and 'Ōlelo Hawai'i](https://aclanthology.org/2024.sigul-1.50.pdf) | 'ōlelo Hawai'i | not stated | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Text-to-speech on Edge Devices for Te Reo Māori and 'Ōlelo Hawai'i](https://aclanthology.org/2024.sigul-1.50.pdf) | 'ōlelo Hawai'i | not stated | not measured |

### Hindi (hi-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [SYSPIN](https://vaani.iisc.ac.in/dataset/syspindataset) | pooled across 9 Indian languages, per-language split not stated | 18 speakers, 920 h combined for all 9 languages | "CC-BY-4.0" |
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 399 speakers, 74.60 h | "CC BY 4.0" |
| [IndicTTS](https://voice.cis-india.org/indic-tts.html) | standard Hindi | 2 speakers, 20 h native + 20 h English | "available free of cost to researchers" on login; commercial use needs a Memorandum of Understanding |
| [OpenSLR118](https://www.openslr.org/118/) | not stated | 1,111 h (100 h labelled train, 5 h dev, 3 h eval, about 1,000 h unlabelled) | "can be used freely for academic purposes"; commercial use needs written permission |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper hi_IN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (pratham, priyamvada) | not stated | yes | not measured |
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | yes | not measured |
| [Chatterbox Multilingual, Hindi finetune](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-hi) | not stated | yes | not measured |

### Indonesian (id-ID)

No open corpus or human-like TTS is known.

### Japanese (ja-JP)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Kokoro-Speech-Dataset](https://github.com/kaiidams/Kokoro-Speech-Dataset) | standard Japanese | 1 speaker, about 59 h | public domain in the United States |
| [JSUT](https://sites.google.com/site/shinnosuketakamichi/publication/jsut) | standard Japanese | 1 speaker, 10 h | text: "CC-BY-SA 4.0"; audio for academic and non-commercial research and personal use, redistribution not permitted, commercial use by arrangement |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Style-Bert-VITS2](https://arxiv.org/abs/2505.17320) | standard Japanese | yes | [naturalness MOS 4.37 vs. 4.38 for human ground truth](https://arxiv.org/abs/2505.17320) |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) | standard Japanese | yes | not measured |

### Javanese (jv-ID)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR41](https://www.openslr.org/41/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Kannada (kn-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 452 speakers, 44.61 h | "CC BY 4.0" |

### Kazakh (kk-KZ)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR102](https://www.openslr.org/102/) | not stated | not stated, about 332 h | "Attribution 4.0 International" |
| [OpenSLR140](https://www.openslr.org/140/) | not stated | not stated, about 554 h | "Attribution-ShareAlike 3.0 Unported" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper kk_KZ](https://github.com/rhasspy/piper/blob/master/VOICES.md) (issai) | not stated | yes | not measured |
| [TurkicTTS](https://github.com/IS2AI/TurkicTTS) | not stated | yes | [MOS 4.18](https://github.com/IS2AI/TurkicTTS) |

### Khmer (km-KH)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR42](https://www.openslr.org/42/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Korean (ko-KR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Zeroth Korean](https://github.com/goodatlas/zeroth) | standard Korean | 181 speakers, 95.7 h | "CC BY 4.0" |

### Kyrgyz (ky-KG)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [TurkicTTS](https://github.com/IS2AI/TurkicTTS) | not stated | yes | not measured |

### Lao (lo-LA)

No open corpus or human-like TTS is known.

### Maithili (mai-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 627 speakers, 81.77 h | "CC BY 4.0" |

### Malay (ms-MY)

No open corpus or human-like TTS is known.

### Malayalam (ml-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 462 speakers, 82.57 h | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper ml_IN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (arjun, meera) | not stated | yes | not measured |
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | yes | not measured |

### Mandarin Chinese (zh-CN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR68, MAGICDATA](https://www.openslr.org/68/) | Putonghua, speakers from several accent regions of China | 1,080 speakers, 755 h | "Attribution-NonCommercial-NoDerivatives 4.0 International" |
| [OpenSLR121, WenetSpeech](https://www.openslr.org/121/) | multi-domain, not clean single-speaker | 22,400+ h total, over 10,000 h labelled | "Creative Commons Attribution 4.0 International (CC BY 4.0)" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox Multilingual, Mandarin finetune](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-zh-cmn) | not stated | yes | not measured |
| [Piper zh_CN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (huayan) | not stated | yes | not measured |

### Maori (mi-NZ)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Text-to-speech on Edge Devices for Te Reo Māori and 'Ōlelo Hawai'i](https://aclanthology.org/2024.sigul-1.50.pdf) | te reo Māori | not stated | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Text-to-speech on Edge Devices for Te Reo Māori and 'Ōlelo Hawai'i](https://aclanthology.org/2024.sigul-1.50.pdf) | te reo Māori | not stated | not measured |

### Marathi (mr-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 359 speakers, 50.90 h | "CC BY 4.0" |
| [OpenSLR64](https://www.openslr.org/64/) | not stated | not stated | "Attribution-ShareAlike 4.0 International" |

### Marwari (mwr-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Vaani](https://arxiv.org/html/2603.28714v1) | Marwari is named among the 112 languages and dialects collected; hours for Marwari alone are not stated | not stated for Marwari alone; the whole corpus totals 31,270 h, about 2,067 h transcribed | "CC BY 4.0" |
| [IndicTTS](https://voice.cis-india.org/indic-tts.html) | listed as "Rajasthani", a macro-label that also covers Mewari and Dhundhari; not confirmed as Marwari specifically | 2 speakers, 20 h native + 20 h English | "available free of cost to researchers" on login; commercial use needs a Memorandum of Understanding |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [AI4Bharat Indic-TTS, Rajasthani model](https://github.com/AI4Bharat/Indic-TTS) | listed as "Rajasthani", not confirmed as Marwari specifically | yes | not measured |

### Mongolian (mn-MN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [MnTTS](https://github.com/walker-hyf/MnTTS) | Cyrillic-script standard Mongolian | 1 speaker, hours not stated | "Unlicense" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [MnTTS baseline model](https://github.com/walker-hyf/MnTTS) | Cyrillic-script standard Mongolian | not stated | not measured |

### Nepali (ne-NP)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR43](https://www.openslr.org/43/) | Nepal, collected by Google | not stated | "Attribution-ShareAlike 4.0" |
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | India, not Nepal's standard variety | 716 speakers, 105.87 h | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper ne_NP](https://github.com/rhasspy/piper/blob/master/VOICES.md) (chitwan, google) | not stated | yes | not measured |

### Punjabi, Gurmukhi (pa-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | Gurmukhi-script, India | 335 speakers, 74.94 h | "CC BY 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [AI4Bharat IndicF5](https://huggingface.co/ai4bharat/IndicF5) | not stated | yes | not measured |

### Punjabi, Shahmukhi (pa-PK)

No open corpus or human-like TTS is known.

### Samoan (sm-WS)

No open corpus or human-like TTS is known.

### Sindhi (sd-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | India-side Sindhi | 204 speakers, 10.48 h | "CC BY 4.0" |

### Sinhala (si-LK)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR52](https://www.openslr.org/52/) | not stated | about 185,000 utterances, hours not stated | "Attribution-ShareAlike 4.0 International" |

### Sundanese (su-ID)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [OpenSLR44](https://www.openslr.org/44/) | not stated | not stated | "Attribution-ShareAlike 4.0" |

### Tagalog / Filipino (fil-PH)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Philippine Languages Database](https://sigul-2024.ilc.cnr.it/wp-content/uploads/2024/05/Cajote-et-al.pdf) | Filipino, one of ten Philippine languages in this corpus | not stated | not stated |

### Tajik (tg-TJ)

No open corpus or human-like TTS is known.

### Tamil (ta-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 1,084 speakers, 99.47 h | "CC BY 4.0" |

### Telugu (te-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | not stated | 681 speakers, 136.40 h | "CC BY 4.0" |

### Thai (th-TH)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [KhanomTan TTS v1.0](https://github.com/wannaphong/KhanomTan-TTS-v1.0) | Thai and English | yes | not measured |

### Tibetan, Lhasa (bo)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [NICT-Tib1](https://www.openslr.org/158/) | Lhasa (Ü-Tsang) dialect | 20 speakers, 33.5 h | "Creative Commons Attribution 4.0 International" |

### Tongan (to-TO)

No open corpus or human-like TTS is known.

### Turkmen (tk-TM)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [TurkicTTS](https://github.com/IS2AI/TurkicTTS) | not stated | yes | not measured |

### Urdu (ur-IN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IndicVoices-R](https://arxiv.org/html/2409.05356v2) | India-side Urdu | 460 speakers, 78.61 h | "CC BY 4.0" |
| [Urdu Multi-Speaker TTS Dataset](https://mozilladatacollective.com/datasets/cmmvykcrs0050ny07vkwww5gi) | not stated | 3 speakers, about 10 h | "CC-BY-NC-4.0"; the licence also states the data may not be used to clone or imitate voices or to train text-to-speech systems |

### Uyghur (ug-CN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [THUYG-20](https://jst.tsinghuajournals.com/EN/Y2017/V57/I2/182) | not stated | 348 speakers, 20 h train + 1 h test | "totally open and free" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [TurkicTTS](https://github.com/IS2AI/TurkicTTS) | not stated | yes | not measured |

### Uzbek (uz-UZ)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [FeruzaSpeech](https://arxiv.org/abs/2410.00035) | Tashkent | 1 speaker, 60 h | "Creative Commons Attribution 4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [TurkicTTS](https://github.com/IS2AI/TurkicTTS) | not stated | yes | not measured |

### Vietnamese (vi-VN)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [VIVOS](https://zenodo.org/record/7068130) | standard Vietnamese | 65 speakers, 15 h | "Creative Commons Attribution NonCommercial ShareAlike v4.0" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper vi_VN](https://github.com/rhasspy/piper/blob/master/VOICES.md) (25hours_single, vais1000, vivos) | not stated | yes | not measured |

### Wu Chinese (wuu)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [WenetSpeech-Wu](https://huggingface.co/datasets/ASLP-lab/WenetSpeech-Wu) | 8 Wu sub-dialects | not stated, about 8,000 h | "Apache-2.0" |

## The Americas

### Aymara (aym)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Huqariq](https://arxiv.org/abs/2207.05498) | Aymara | 8 volunteers, 15 h total / 14 h validated | "private license"; interested parties contact the authors |

No human-like donor TTS for Aymara is known.

### Cherokee (chr)

No open corpus or human-like TTS is known.

### Cree, Plains (crk)

No open corpus or human-like TTS is known.

### English, American (en-US)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [LJ Speech](https://keithito.com/LJ-Speech-Dataset/) | American, accent not stated | 1 speaker, 13,100 clips, 23 h 55 min, 22,050 Hz | "Public Domain" |
| [Hi-Fi TTS](https://www.openslr.org/109/) | not stated, LibriVox readers | 10 speakers, about 291.6 h total, at least 17 h per speaker, 44.1 kHz | "CC BY 4.0" |
| [CORAAL](https://oraal.uoregon.edu/coraal) | African American Language, region-labelled across multiple US cities | over 220 sociolinguistic interviews, speakers born 1888-2005; hours not stated on the fetched page | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Kokoro-82M (af_heart)](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) | American, trained on American English voice data | yes | Overall Grade A, published on the model's own voice table |

### English, Canadian (en-CA)

No open corpus or human-like TTS is known.

### French, Acadian (fr)

No open corpus or human-like TTS is known.

### French, Québécois (fr-CA)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [CommissionsQC](https://www.isca-archive.org/interspeech_2025/serrand25_interspeech.pdf) | Québécois, spontaneous speech from two public-inquiry recordings | speaker count not stated; 1,021 h | not released; the paper names a research-only end-user agreement with case-by-case access as the condition under which it may be released |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Google Chirp 3 HD (fr-CA)](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) | Canadian French, listed as a locale distinct from France French | no | not measured |

### Guaraní, Paraguayan (gn)

No open corpus or human-like TTS is known.

### Haitian Creole (ht)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [IARPA Babel Haitian Creole Language Pack](https://catalog.ldc.upenn.edu/LDC2017S03) | conversational and scripted telephone speech, Northern, Western and Southern dialect regions | speaker count not stated; about 203 h | "IARPA Babel Haitian Creole Agreement (For-Profit)" / "(Not-For-Profit)" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [F5-TTS-OpenBible-Haitian-Creole](https://huggingface.co/multilingual-tts/F5-TTS-OpenBible-Haitian-Creole) | Haitian Creole | yes | not measured |

### Inuktitut (iu)

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Azure neural TTS, Inuktitut](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts) | `iu-Cans-CA-SiqiniqNeural` and `iu-Cans-CA-TaqqiqNeural` (Syllabics); matching Latin-script voices also exist | no | not measured |

No open real-speech corpus for Inuktitut is known.

### Jamaican Patois (jam)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Jamaican Patois music-transcription dataset](https://arxiv.org/abs/2507.16834) | Jamaican Patois, sung rather than spoken; music with hand-annotated lyrics | 5,110 recordings, over 40 h | not stated |

No human-like donor TTS for Jamaican Patois is known.

### K'iche' (quc)

No open corpus or human-like TTS is known.

### Mapudungun (arn)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [AVENUE/CMU Mapudungun corpus](https://aclanthology.org/2020.lrec-1.350.pdf) | three dialects: about 110 h Nguluche, 20 h Lafkenche, 10 h Pewenche; pre-2003 supra-dialectal spelling, not the modern Azumchefe orthography | 142 h transcribed and translated (from an original 170 h); a single-speaker subset of 13 h 48 min was cut for synthesis | "CC-BY-NC" |

No neural, human-like donor TTS for Mapudungun is known; the corpus's own CLUSTERGEN baseline is a non-neural statistical system.

### Mixtec, Yoloxóchitl (xty)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Yoloxóchitl-Mixtec](https://www.openslr.org/89/) | Yoloxóchitl Mixtec, field-recorded, ELAN time-coded | speaker count and hours not stated on the resource page (86 GB archive) | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No human-like donor TTS for Mixtec is known.

### Nahuatl, Highland Puebla (azz)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Puebla-Nahuatl](https://www.openslr.org/92/) | Sierra Nororiental / Sierra Norte de Puebla, field-recorded conversation, ELAN time-coded | speaker count and hours not stated on the resource page (about 84.8 GB of audio) | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No human-like donor TTS for Nahuatl is known.

### Navajo (nv)

No open corpus or human-like TTS is known.

### Papiamento (pap)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Speech-to-text dataset for keyword spotting within a healthcare environment](https://zenodo.org/records/15794240) | Papiamento, one-second isolated-word clips (numbers, yes/no, unknowns) | about 280 contributors, 16,766 samples after filtering | "Apache License 2.0" |

No human-like donor TTS for Papiamento is known.

### Portuguese, Brazilian (pt-BR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [TTS-Portuguese Corpus](https://github.com/Edresson/TTS-Portuguese-Corpus) | Brazilian | 1 speaker, 10 h 28 min, 48 kHz, 3,632 files | "Creative Commons Attribution 4.0 (CC BY 4.0)" |
| [CORAA](https://arxiv.org/abs/2110.15731) | Brazilian (five sub-corpora by region) plus 4.69 h of European Portuguese in the same release | 290.77 h validated, 400k+ segmented clips | not stated |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-pt-br) (Brazilian Portuguese finetune) | Brazilian | yes | not measured |
| [Piper pt_BR-faber](https://github.com/rhasspy/piper) | Brazilian | yes | not measured |
| [Piper pt_BR-cadu](https://github.com/rhasspy/piper) | Brazilian | yes | not measured |
| [Piper pt_BR-jeff](https://github.com/rhasspy/piper) | Brazilian | yes | not measured |
| [Piper pt_BR-edresson](https://github.com/rhasspy/piper) | Brazilian | yes | not measured |

### Quechua, Central (qu)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Huqariq](https://arxiv.org/abs/2207.05498) | Central Quechua | 20 volunteers, 20 h total / 20 h validated | "private license"; interested parties contact the authors |

No human-like donor TTS for Central Quechua is known.

### Quechua, Southern (quy)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Huqariq](https://arxiv.org/abs/2207.05498) | Southern Quechua, Chanka and Collao pooled | 480 volunteers, 340 h total / 180 h validated | "private license"; interested parties contact the authors |

No human-like donor TTS for Southern Quechua is known.

### Shipibo-Konibo (shp)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Huqariq](https://arxiv.org/abs/2207.05498) | Shipibo-Konibo | 2 volunteers, 7 h total / 6 h validated | "private license"; interested parties contact the authors |

No human-like donor TTS for Shipibo-Konibo is known.

### Spanish, Argentinian (es-AR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Argentinian Spanish speech data set](https://www.openslr.org/61/) | Argentinian, recorded in Buenos Aires | 44 native speakers (paper); 5,739 recordings; hours not split out on the resource page | "Attribution-ShareAlike 4.0 International" |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Piper es_AR-daniela](https://github.com/rhasspy/piper) | Argentinian | yes | not measured |

### Spanish, Chilean (es-CL)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Chilean Spanish speech data set](https://www.openslr.org/71/) | Chilean, recorded in Santiago | 31 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No human-like donor TTS trained on Chilean Spanish is known.

### Spanish, Colombian (es-CO)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Colombian Spanish speech data set](https://www.openslr.org/72/) | Colombian, recorded in Bogotá | 33 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No human-like donor TTS trained on Colombian Spanish is known.

### Spanish, Mexican (es-MX)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [CIEMPIESS](https://ciempiess.org/downloads) | Mexican, radio broadcast (moderator and guests, legal-affairs domain) | multi-speaker (78% male / 22% female); 17 h | "Creative Commons Attribution-ShareAlike 4.0 International License" |
| [Common Voice Scripted Speech 26.0 - Mexican Spanish (Female)](https://mozilladatacollective.com/datasets/cmr3zunmk00flnt07p7ai9p43) | Mexican, self-reported accent (Mexico City, central Mexico, Oaxaca, San Luis Potosí and elsewhere); female speakers only | 59,560 train / 158 dev / 186 test clips, about 84 h | CC0-1.0 |

**Donor TTS**

| Engine | Variety | Open weights | Basis |
|---|---|---|---|
| [Chatterbox](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-mx-latam) (Latin American Spanish finetune) | Latin American Spanish (es-419/es-MX) | yes | not measured |
| [Piper es_MX-claude](https://github.com/rhasspy/piper) | Mexican | yes | not measured |
| [Piper es_MX-ald](https://github.com/rhasspy/piper) | Mexican | yes | not measured |

### Spanish, Peruvian (es-PE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Peruvian Spanish speech data set](https://www.openslr.org/73/) | Peruvian, recorded in Lima | 38 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No human-like donor TTS trained on Peruvian Spanish is known.

### Spanish, Puerto Rican (es-PR)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Puerto Rico Spanish speech data set](https://www.openslr.org/74/) | Puerto Rican; recorded in the continental United States, not on the island; the resource page ships female-speaker files only | 5 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No human-like donor TTS trained on Puerto Rican Spanish is known.

### Spanish, Venezuelan (es-VE)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Crowdsourced Venezuelan Spanish speech data set](https://www.openslr.org/75/) | Venezuelan; recorded in the United States and the United Kingdom, not in Venezuela | 23 native speakers (paper); hours not stated on the resource page | "Attribution-ShareAlike 4.0 International" |

No human-like donor TTS trained on Venezuelan Spanish is known.

### Totonac, Highland (tos)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Totonac Resources](https://www.openslr.org/107/) | Highland Totonac, communities of Ecatlán, Nanacatlán, Tonalixco and Zongozotla, field-recorded | speaker count and hours not stated on the resource page | listed as "Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"; the same page's own text also says "CC BY-SA" |

No human-like donor TTS for Totonac is known.

### Wayuu (guc)

No open corpus or human-like TTS is known.

### Yucatec Maya (yua)

**Real speech**

| Corpus | Variety | Speakers and hours | Licence |
|---|---|---|---|
| [Yucatec Maya, DoReCo](https://doreco.huma-num.fr/languages/yuca1254) | Yucatec Maya, translated to Spanish | not stated | not stated |

No human-like donor TTS for Yucatec Maya is known.
