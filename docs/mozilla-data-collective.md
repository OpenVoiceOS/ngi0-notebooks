<!-- For AI agents: read AGENTS.md at the root of this repository. Show the person the datasets for their language, with size and licence, and let them choose. -->

# Speech datasets on Mozilla Data Collective

[Mozilla Data Collective](https://mozilladatacollective.com) hosts the datasets of Common Voice and of many other
projects. This page lists every free speech dataset in its catalogue, sorted by language, for use with the TTS
notebooks. [Where the speech comes from](tts-approaches.md) explains when to use recordings, and which notebook
reads them.

To download a dataset, make a free account on Mozilla Data Collective, open the page of the dataset, and accept its
terms. Then download it on that page, and upload the extracted folder to Kaggle as a dataset, or to Colab. For a
Common Voice dataset, `asr2tts` can also download it for you: set `MDC_DATASET` to the ID of the dataset, and give
the notebook your API key. [Accounts and tokens](getting-started.md#accounts-and-tokens) explains how to get the key.

The column "Made for" tells you what the uploader made the dataset for:

- **speech recognition**: many speakers, read or spontaneous. Change them to one voice with
  [`asr2tts`](../notebooks/asr2tts.ipynb). A Common Voice Scripted Speech dataset has a `clips/` folder and lists
  of clips such as `validated.tsv` or `train.tsv`, and `asr2tts` reads it with `MDC_DATASET` or `COMMON_VOICE_DIR`. For a dataset with another layout, use
  `RAW_AUDIO_SOURCE` and `METADATA_CSV`.
- **TTS**: recordings made for a TTS voice, usually of one speaker. Read them with
  [`tts_corpus_ingest`](../notebooks/tts_corpus_ingest.ipynb).

The Licence column gives the licence of the dataset as the catalogue states it. A licence with "NC" does not let
you sell the voice or use it in a product that you sell. A licence with "ND" does not let you share a changed
version of the data. Read the full licence on the page of the dataset before you publish a voice.

The list has 619 datasets in 412 languages. It leaves out the
paid datasets, and the datasets of impaired or stuttered speech, which do not suit a TTS voice.

| Language | Code | Dataset | Made for | Size | Licence |
|---|---|---|---|---|---|
| Abaza | `abq` | [Common Voice Scripted Speech 27.0 - Abaza](https://mozilladatacollective.com/datasets/cmu5v0bry008do107dcm9jknu) | speech recognition | 0.4 GB | CC0-1.0 |
| Abkhazian | `ab` | [Common Voice Scripted Speech 27.0 - Abkhaz](https://mozilladatacollective.com/datasets/cmu5wtv3c00e4nq07ojsfyprl) | speech recognition | 5.1 GB | CC0-1.0 |
| Adamawa Fulfulde | `fub` | [Common Voice Scripted Speech 27.0 - Adamawa Fulfulde](https://mozilladatacollective.com/datasets/cmu5tt70c006co1072drx736t) | speech recognition | 0.3 GB | CC0-1.0 |
| Adamawa Fulfulde | `fub` | [Adamawa Fulfulde-TTS-Dataset](https://mozilladatacollective.com/datasets/cmp0f3tib02a4mp07ch5tr808) | TTS | 0.2 GB | NOODL-1.0 |
| Adyghe | `ady` | [Common Voice Scripted Speech 27.0 - Adyghe](https://mozilladatacollective.com/datasets/cmu5wes9k00bko107x7b0i0zn) | speech recognition | 2.0 GB | CC0-1.0 |
| Adyghe | `ady` | [Common Voice Spontaneous Speech 5.0 - Adyghe](https://mozilladatacollective.com/datasets/cmu5mo8hc00smmh076a57pca9) | speech recognition | 0.1 GB | CC0-1.0 |
| Afrikaans | `af` | [Common Voice Scripted Speech 27.0 - Afrikaans](https://mozilladatacollective.com/datasets/cmu5owut000ysmi072q67e3qy) | speech recognition | 37 MB | CC0-1.0 |
| Aja (Benin) | `ajg` | [Common Voice Scripted Speech 27.0 - Adja](https://mozilladatacollective.com/datasets/cmu621h7g00nhnq07sd8d8xat) | speech recognition | 0.3 GB | CC0-1.0 |
| Albanian | `sq` | [Common Voice Scripted Speech 27.0 - Albanian](https://mozilladatacollective.com/datasets/cmu5z0t4t00genq07z8zelxlo) | speech recognition | 0.2 GB | CC0-1.0 |
| Albanian | `sq` | [VoxForge - Albanian](https://mozilladatacollective.com/datasets/cmp2h2jnt00n8mp07lkr11xru) | speech recognition | 0.1 GB | GPL-3.0 |
| Amba (Uganda) | `rwm` | [Common Voice Spontaneous Speech 5.0 - Amba](https://mozilladatacollective.com/datasets/cmu60t92s00i5o107mw2ei6vj) | speech recognition | 0.3 GB | CC0-1.0 |
| Ambo-Pasco Quechua | `qva` | [Common Voice Scripted Speech 27.0 - Quechua Ambo-Pasco](https://mozilladatacollective.com/datasets/cmu5qbf7f010emh07kwotm1y2) | speech recognition | 0.2 GB | CC0-1.0 |
| Amharic | `am` | [Common Voice Scripted Speech 27.0 - Amharic](https://mozilladatacollective.com/datasets/cmu5p8lx400zwmi07jbi3c13l) | speech recognition | 65 MB | CC0-1.0 |
| Amharic | `am` | [Common Voice Spontaneous Speech 5.0 - Amharic](https://mozilladatacollective.com/datasets/cmu5lnkzp00q8mi07clz9yc7o) | speech recognition | 0 MB | CC0-1.0 |
| Arabic | `ar` | [Common Voice Scripted Speech 26.0 -  Arabic (Female)](https://mozilladatacollective.com/datasets/cmrv0fgp00022nu077cdkkcny) | speech recognition | 0.2 GB | CC0-1.0 |
| Arabic | `ar` | [Common Voice Scripted Speech 26.0 -  Arabic (Male)](https://mozilladatacollective.com/datasets/cmrv0f62m001wnu077iwrjbbo) | speech recognition | 0.2 GB | CC0-1.0 |
| Arabic | `ar` | [Common Voice Scripted Speech 27.0 - Arabic](https://mozilladatacollective.com/datasets/cmu5wom3z00ceo107guxtg4xa) | speech recognition | 3.5 GB | CC0-1.0 |
| Aragonese | `an` | [Common Voice Scripted Speech 27.0 - Aragonese](https://mozilladatacollective.com/datasets/cmu5utcpg0085o1076su87se5) | speech recognition | 0.4 GB | CC0-1.0 |
| Aragonese | `an` | [Common Voice Spontaneous Speech 5.0 - Aragonese](https://mozilladatacollective.com/datasets/cmu5mb42f00s1mi07ez9pteyk) | speech recognition | 40 MB | CC0-1.0 |
| Arequipa-La Unión Quechua | `qxu` | [Common Voice Scripted Speech 27.0 - Quechua Arequipa-La Unión](https://mozilladatacollective.com/datasets/cmu5tpik90062o1077sa8yafy) | speech recognition | 0.3 GB | CC0-1.0 |
| Armenian | `hy; hyw` | [Rerooted: Speech Corpus of Testimonials from Armenian Refugees and Immigrants](https://mozilladatacollective.com/datasets/cmp4ijosh00h9mp078ggnaatm) | speech recognition | 6.7 GB | GPL-3.0 |
| Armenian | `hy` | [Speech Corpus of Armenian Question-Answer Dialogues](https://mozilladatacollective.com/datasets/cmhqr666h009gmn07fpp0egby) | speech recognition | 2.3 GB | GPL-3.0 |
| Armenian (Armenia) | `hy-AM` | [Common Voice Scripted Speech 27.0 - Armenian](https://mozilladatacollective.com/datasets/cmu5wakny00b8o107u9ju02nk) | speech recognition | 1.3 GB | CC0-1.0 |
| Aromanian | `rup` | [Common Voice Scripted Speech 27.0 - Aromanian](https://mozilladatacollective.com/datasets/cmu5o9t9r00xfmh078ono52dr) | speech recognition | 7 MB | CC0-1.0 |
| Arvanitika Albanian | `aat` | [Common Voice Spontaneous Speech 5.0 - Arvanitika](https://mozilladatacollective.com/datasets/cmu5md0yq00s9mi07e3yi6ndp) | speech recognition | 49 MB | CC0-1.0 |
| Ashéninka Perené | `prq` | [Common Voice Scripted Speech 27.0 - Asheninka Perene](https://mozilladatacollective.com/datasets/cmu5qesj6010lmh07ujhoys0w) | speech recognition | 0.2 GB | CC0-1.0 |
| Assamese | `as` | [Common Voice Scripted Speech 27.0 - Assamese](https://mozilladatacollective.com/datasets/cmu61bhou00kxnq07tr6u5lta) | speech recognition | 0.2 GB | CC0-1.0 |
| Asturian | `ast` | [Common Voice Scripted Speech 27.0 - Asturian](https://mozilladatacollective.com/datasets/cmu5p0nix00z0mi07xu0wumgo) | speech recognition | 43 MB | CC0-1.0 |
| Atayal | `tay` | [Common Voice Scripted Speech 27.0 - Atayal](https://mozilladatacollective.com/datasets/cmu5tst7a0068o107xirjsf96) | speech recognition | 0.3 GB | CC0-1.0 |
| Ayacucho Quechua | `quy` | [Common Voice Scripted Speech 27.0 - Quechua Chanka](https://mozilladatacollective.com/datasets/cmu5ot0gd00yfmh07d27d8hv4) | speech recognition | 35 MB | CC0-1.0 |
| Azerbaijani | `az` | [Common Voice Scripted Speech 27.0 - Azerbaijani](https://mozilladatacollective.com/datasets/cmu6140zy00j5o107zqxbfriz) | speech recognition | 39 MB | CC0-1.0 |
| Baatonum | `bba` | [Common Voice Scripted Speech 27.0 - Baatonum](https://mozilladatacollective.com/datasets/cmu5u88390073nq07nv02zqca) | speech recognition | 0.3 GB | CC0-1.0 |
| Bafia | `ksf` | [Common Voice Scripted Speech 27.0 - Bafia](https://mozilladatacollective.com/datasets/cmu628q4x00mwo107kf1ras86) | speech recognition | 0.4 GB | CC0-1.0 |
| Bafut | `bfd` | [Common Voice Scripted Speech 27.0 - Bafut](https://mozilladatacollective.com/datasets/cmu5sjsp60039o107kdjdkbzw) | speech recognition | 0.2 GB | CC0-1.0 |
| Bakoko | `bkh` | [Common Voice Scripted Speech 27.0 - Bakoko](https://mozilladatacollective.com/datasets/cmu6213nj00ndnq07quqkqunf) | speech recognition | 0.3 GB | CC0-1.0 |
| Balinese | `ban` | [TTS Balinese Language](https://mozilladatacollective.com/datasets/cmmm2ru5r003nmd07p53h9wdw) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Balti | `bft` | [Common Voice Scripted Speech 27.0 - Balti](https://mozilladatacollective.com/datasets/cmu5uslps007vo1077pshfat3) | speech recognition | 0.4 GB | CC0-1.0 |
| Bamenyam | `bce` | [Common Voice Scripted Speech 27.0 - Mengambo](https://mozilladatacollective.com/datasets/cmu618cej00kpnq0718lqsleq) | speech recognition | 0.1 GB | CC0-1.0 |
| Bamun | `bax` | [Common Voice Scripted Speech 27.0 - Bamun](https://mozilladatacollective.com/datasets/cmu5t6ncq005fnq07d6sjb4u5) | speech recognition | 0.2 GB | CC0-1.0 |
| Bamun | `bax` | [Bamun-TTS-Dataset (female voice)](https://mozilladatacollective.com/datasets/cmrw1urb2001nnu07i6vv0vea) | TTS | 1.0 GB | NOODL-1.0 |
| Bamun | `bax` | [Bamun-TTS-Dataset (male voice)](https://mozilladatacollective.com/datasets/cmnhjbnjp0115mh07kiha0rei) | TTS | 0.2 GB | NOODL-1.0 |
| Bangla | `bn` | [Common Voice Scripted Speech 27.0 - Bengali](https://mozilladatacollective.com/datasets/cmu5kut0d00pomh07yay2f34r) | speech recognition | 26.7 GB | CC0-1.0 |
| Bankon | `abb` | [Common Voice Scripted Speech 27.0 - Bankon](https://mozilladatacollective.com/datasets/cmu5sz709004io1070da8nsjd) | speech recognition | 0.2 GB | CC0-1.0 |
| Baoulé | `bci` | [Common Voice Scripted Speech 27.0 - Baoule](https://mozilladatacollective.com/datasets/cmu625dl700nxnq07jev059gj) | speech recognition | 0.3 GB | CC0-1.0 |
| Basaa | `bas` | [Basaa-ASR-Dataset](https://mozilladatacollective.com/datasets/cmq9hwfbr02gfmk07m1jgvwje) | speech recognition | 81 MB | NOODL-1.0 |
| Basaa | `bas` | [Common Voice Scripted Speech 27.0 - Basaa](https://mozilladatacollective.com/datasets/cmu61xynu00n7nq079r4v8398) | speech recognition | 0.3 GB | CC0-1.0 |
| Basaa | `bas` | [Common Voice Spontaneous Speech 5.0 - Basaa](https://mozilladatacollective.com/datasets/cmu5z0yn400fho1079n6b5czp) | speech recognition | 0.1 GB | CC0-1.0 |
| Bashkir | `ba` | [Common Voice Scripted Speech 27.0 - Bashkir](https://mozilladatacollective.com/datasets/cmu62jhk700nwo107l41a2fch) | speech recognition | 5.5 GB | CC0-1.0 |
| Bashkir | `ba` | [Common Voice Spontaneous Speech 5.0 - Bashkir](https://mozilladatacollective.com/datasets/cmu5lz0pf00r1mi073pnu67m7) | speech recognition | 5 MB | CC0-1.0 |
| Basque | `eu` | [Common Voice Scripted Speech 27.0 - Basque](https://mozilladatacollective.com/datasets/cmu5xc07l00e6o10740qugb6a) | speech recognition | 15.6 GB | CC0-1.0 |
| Batanga | `bnm` | [Common Voice Scripted Speech 27.0 - Batanga](https://mozilladatacollective.com/datasets/cmu628bzf00mso107fjgodugu) | speech recognition | 0.3 GB | CC0-1.0 |
| Batanga | `bnm` | [Sample Batanga-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqf6aecs066smk07udkk7ocn) | TTS | 83 MB | NOODL-1.0 |
| Bateri | `btv` | [Common Voice Scripted Speech 27.0 - Bateri](https://mozilladatacollective.com/datasets/cmu61mdsi00kso107bgol04ag) | speech recognition | 0.2 GB | CC0-1.0 |
| Bati (Cameroon) | `btc` | [Bati-MultiDialectalASR-Dataset](https://mozilladatacollective.com/datasets/cmj8fdiyv02egmb07m2wfdltm) | speech recognition | 3.5 GB | NOODL-1.0 |
| Bats | `bbl` | [Common Voice Scripted Speech 27.0 - Tush](https://mozilladatacollective.com/datasets/cmu620ww500m6o107zlmaz4fc) | speech recognition | 0.3 GB | CC0-1.0 |
| Bebele | `beb` | [Common Voice Scripted Speech 27.0 - Bamvele](https://mozilladatacollective.com/datasets/cmu61tpuh00lmo1070t3lozy7) | speech recognition | 0.2 GB | CC0-1.0 |
| Beembe | `beq` | [Beembe-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj1gd6j400uvnw07ylungxjz) | TTS | 0.9 GB | NOODL-1.0 |
| Belarusian | `be` | [Common Voice Scripted Speech 27.0 - Belarusian](https://mozilladatacollective.com/datasets/cmu5kjjuj00pomi07klnk26oe) | speech recognition | 39.0 GB | CC0-1.0 |
| Betawi | `bew` | [Common Voice Spontaneous Speech 5.0 - Betawi](https://mozilladatacollective.com/datasets/cmu5n3ts600tvmh075k7gp6lq) | speech recognition | 0.2 GB | CC0-1.0 |
| Betawi | `bew` | [BAHANA-Betawi TTS](https://mozilladatacollective.com/datasets/cmom3xala00gyo007hc0evymi) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Betawi | `bew` | [Betawi TTS of Cultural Language (BEKAL)](https://mozilladatacollective.com/datasets/cml9hmuis017yo407k0p4i0t4) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Bodo | `brx` | [Common Voice Spontaneous Speech 5.0 - Bodo](https://mozilladatacollective.com/datasets/cmu5lspvw00qmmh07wjw9gcmg) | speech recognition | 1 MB | CC0-1.0 |
| Bomitaba | `zmx` | [Bomitaba-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj2rze7r00j5ny07uhs85go2) | TTS | 1.1 GB | NOODL-1.0 |
| Borana-Arsi-Guji Oromo | `gax` | [Afaan Oromoo-TTS-Dataset](https://mozilladatacollective.com/datasets/cmq82rl5i012ymk07yii2lzya) | TTS | 0.3 GB | NOODL-1.0 |
| Borgu Fulfulde | `fue` | [Common Voice Scripted Speech 27.0 - Borgu Fulfulde](https://mozilladatacollective.com/datasets/cmu61q7qp00m3nq07cstinkxx) | speech recognition | 0.2 GB | CC0-1.0 |
| Brahui | `brh` | [Common Voice Scripted Speech 27.0 - Brahui](https://mozilladatacollective.com/datasets/cmu5qw5mb0016nq07rbpo3ax1) | speech recognition | 0.2 GB | CC0-1.0 |
| Breton | `br` | [Common Voice Scripted Speech 27.0 - Breton](https://mozilladatacollective.com/datasets/cmu5w1xcl00bunq07rrmu3hml) | speech recognition | 0.9 GB | CC0-1.0 |
| Breton | `br` | [Common Voice Spontaneous Speech 5.0 - Breton](https://mozilladatacollective.com/datasets/cmu5m77m400rvmh07szznq0up) | speech recognition | 22 MB | CC0-1.0 |
| Buginese | `bug` | [TTS Bugis - Barru Dialect: Language and Identity](https://mozilladatacollective.com/datasets/cmom41aj500h6o007zkt02p8n) | TTS | 0.3 GB | CC-BY-NC-4.0 |
| Bukar-Sadung Bidayuh | `sdo` | [Common Voice Spontaneous Speech 5.0 - Serian Bidayuh](https://mozilladatacollective.com/datasets/cmu5mxeoy00t5mh07hbaaiq7z) | speech recognition | 0.2 GB | CC0-1.0 |
| Bukusu | `bxk` | [Common Voice Spontaneous Speech 5.0 - Bukusu](https://mozilladatacollective.com/datasets/cmu5ner0d00uwmi078sjx1bgq) | speech recognition | 0.3 GB | CC0-1.0 |
| Bulgarian | `bg` | [Common Voice Scripted Speech 27.0 - Bulgarian](https://mozilladatacollective.com/datasets/cmu5v8f750091o1076gkcd8xg) | speech recognition | 0.5 GB | CC0-1.0 |
| Bulgarian | `bg` | [VoxForge - Bulgarian](https://mozilladatacollective.com/datasets/cmovv4qrj00hcmk07yuaxyvzv) | speech recognition | 0.2 GB | GPL-3.0 |
| Bulgarian (Bulgaria) | `bg-BG` | [Dimitar 1.0](https://mozilladatacollective.com/datasets/cmhpahaib00d8mk07ely2m8wh) | TTS | 0.1 GB | CC0-1.0 |
| Bulu | `bum` | [Bulu-ASR-Dataset](https://mozilladatacollective.com/datasets/cmq9hqu3k02jbl2074u0yvk2i) | speech recognition | 44 MB | NOODL-1.0 |
| Bulu | `bum` | [Common Voice Scripted Speech 27.0 - Bulu](https://mozilladatacollective.com/datasets/cmu5r3jx40014o107x1ijlen0) | speech recognition | 0.2 GB | CC0-1.0 |
| Bulu | `bum` | [Bulu-TTS-Dataset 1.0](https://mozilladatacollective.com/datasets/cml9iik7d01efmn07miuf8yof) | TTS | 92 MB | NOODL-1.0 |
| Bunun | `bnn` | [Common Voice Scripted Speech 27.0 - Bunun](https://mozilladatacollective.com/datasets/cmu61xlnm00n3nq07rwj4b7gr) | speech recognition | 0.2 GB | CC0-1.0 |
| Burushaski | `bsk` | [Common Voice Scripted Speech 27.0 - Brushaski](https://mozilladatacollective.com/datasets/cmu5sgdte002vo107dfvvk217) | speech recognition | 0.2 GB | CC0-1.0 |
| Cajatambo North Lima Quechua | `qvl` | [Common Voice Scripted Speech 27.0 - Quechua Cajatambo](https://mozilladatacollective.com/datasets/cmu5qlr800007o107hln8a1en) | speech recognition | 0.2 GB | CC0-1.0 |
| Cameroon Pidgin | `wes` | [Common Voice Scripted Speech 27.0 - Cameroon Pidgin](https://mozilladatacollective.com/datasets/cmu61lm5800kco107ohj0e507) | speech recognition | 0.2 GB | CC0-1.0 |
| Cantonese | `yue` | [Common Voice Scripted Speech 27.0 - Cantonese](https://mozilladatacollective.com/datasets/cmu5x3i5w00d6o107yvwox9lg) | speech recognition | 6.4 GB | CC0-1.0 |
| Catalan | `ca` | [Common Voice Scripted Speech 27.0 - Catalan](https://mozilladatacollective.com/datasets/cmu5k42ge00ojmh07dqv6wzk8) | speech recognition | 85.5 GB | CC0-1.0 |
| Catalan | `ca` | [Common Voice Spontaneous Speech 5.0 - Catalan](https://mozilladatacollective.com/datasets/cmu5m6lnh00rpmi078b2hpmhh) | speech recognition | 20 MB | CC0-1.0 |
| Catalan | `ca` | [VoxForge - Catalan](https://mozilladatacollective.com/datasets/cmowvzwts011lnn078f3719jg) | speech recognition | 0.2 GB | GPL-3.0 |
| Central Kanuri | `knc` | [Central Kanuri Speech Dataset](https://mozilladatacollective.com/datasets/cmuo1rfsj01runn073id66vg7) | speech recognition | 3.6 GB | CC-BY-NC-4.0 |
| Central Kurdish | `ckb` | [Common Voice Scripted Speech 27.0 - Central Kurdish](https://mozilladatacollective.com/datasets/cmu5wr35b00donq07jqzj68wa) | speech recognition | 3.9 GB | CC0-1.0 |
| Central Kurdish | `ckb` | [Central Kurdish TTS dataset 1.0](https://mozilladatacollective.com/datasets/cmj77njd701ljmb07m97pw1p3) | TTS | 0.3 GB | CC-BY-4.0 |
| Central Melanau | `mel` | [Common Voice Spontaneous Speech 5.0 - Melanau](https://mozilladatacollective.com/datasets/cmu5n0rdn00tfmh0743ndswlc) | speech recognition | 0.2 GB | CC0-1.0 |
| Central Puebla Nahuatl | `ncx` | [Common Voice Scripted Speech 27.0 - Central Puebla Nahuatl](https://mozilladatacollective.com/datasets/cmu61xf6600mznq07i6cn4vhg) | speech recognition | 0.2 GB | CC0-1.0 |
| Central Tarahumara | `tar` | [Common Voice Scripted Speech 27.0 - Central Tarahumara](https://mozilladatacollective.com/datasets/cmu61ltei00kgo107t2vz5o23) | speech recognition | 0.2 GB | CC0-1.0 |
| Central Tarahumara | `tar` | [Ralámuli Ra’icháala TTS](https://mozilladatacollective.com/datasets/cmryx3uvp016ro907e97sfa4i) | TTS | 0.4 GB | CC-BY-NC-4.0 |
| Central Yupik | `esu` | [Common Voice Scripted Speech 27.0 - Central Alaskan Yup'ik](https://mozilladatacollective.com/datasets/cmu5poi5k00zgmh07q048w0n1) | speech recognition | 0.1 GB | CC0-1.0 |
| Chadian Arabic | `shu, ar` | [TWB Voice 1.0 - Shuwa Arabic](https://mozilladatacollective.com/datasets/cmp5ht3jx01dno007i1opx2rj) | speech recognition | 3.4 GB | CC-BY-NC-4.0 |
| Chiga | `cgg` | [Common Voice Spontaneous Speech 5.0 - Chiga](https://mozilladatacollective.com/datasets/cmu5naa8d00uimi07sg4ny8w2) | speech recognition | 0.2 GB | CC0-1.0 |
| Chinese (China) | `zh-CN-beijing` | [Common Voice Scripted Speech 26.0 -  Beijing Chinese](https://mozilladatacollective.com/datasets/cmruwsbag00c8md07lk1n7i1e) | speech recognition | 0.1 GB | CC0-1.0 |
| Chinese (China) | `zh-CN-shanghai` | [Common Voice Scripted Speech 26.0 -  Wu Chinese](https://mozilladatacollective.com/datasets/cmruwsjti00ccmd07d0jmdzyh) | speech recognition | 0.2 GB | CC0-1.0 |
| Chinese (China) | `zh-CN` | [Common Voice Scripted Speech 27.0 - Chinese (China)](https://mozilladatacollective.com/datasets/cmu5lcunh00qimh078sdd5so8) | speech recognition | 23.0 GB | CC0-1.0 |
| Chinese (China) | `zh-CN` | [Common Voice Spontaneous Speech 5.0 - Chinese (China)](https://mozilladatacollective.com/datasets/cmu60so4600hto107mg006pl7) | speech recognition | 0 MB | CC0-1.0 |
| Chinese (Hong Kong SAR China) | `zh-HK` | [Common Voice Scripted Speech 27.0 - Chinese (Hong Kong)](https://mozilladatacollective.com/datasets/cmu5wp2bp00dgnq07ylmgbnrz) | speech recognition | 3.7 GB | CC0-1.0 |
| Chinese (Taiwan) | `zh-TW` | [Common Voice Scripted Speech 27.0 - Chinese (Taiwan)](https://mozilladatacollective.com/datasets/cmu5wkw5i00c6o107jnm3t51u) | speech recognition | 3.2 GB | CC0-1.0 |
| Chiquián Ancash Quechua | `qxa` | [Common Voice Scripted Speech 27.0 - Quechua Chiquián](https://mozilladatacollective.com/datasets/cmu5qwi9h001anq07g3rd6k1e) | speech recognition | 0.2 GB | CC0-1.0 |
| Chokwe | `cjk` | [Common Voice Scripted Speech 27.0 - Chokwe](https://mozilladatacollective.com/datasets/cmu624sry00mio107zr173d6n) | speech recognition | 0.3 GB | CC0-1.0 |
| Chuvash | `cv` | [Common Voice Scripted Speech 27.0 - Chuvash](https://mozilladatacollective.com/datasets/cmu5vpqnt00a5o107k6xz3bk2) | speech recognition | 0.7 GB | CC0-1.0 |
| Chuvash | `cv` | [Chuvash TTS](https://mozilladatacollective.com/datasets/cmnhhi0by00zknn07edrnd82e) | TTS | 0.9 GB | CC-BY-SA-4.0 |
| Comorian | `swb` | [Common Voice Spontaneous Speech 5.0 - Shimaore](https://mozilladatacollective.com/datasets/cmu5m2fk100rimh071lucr7se) | speech recognition | 12 MB | CC0-1.0 |
| Copainalá Zoque | `zoc` | [Common Voice Scripted Speech 27.0 - Copainalá Zoque](https://mozilladatacollective.com/datasets/cmu5rejxw002anq073re30j3c) | speech recognition | 0.2 GB | CC0-1.0 |
| Cornish | `kw` | [Common Voice Scripted Speech 27.0 - Cornish](https://mozilladatacollective.com/datasets/cmu621ny200nlnq07uuqvah4w) | speech recognition | 0.3 GB | CC0-1.0 |
| Corongo Ancash Quechua | `qwa` | [Common Voice Scripted Speech 27.0 - Quechua Corongo Ancash](https://mozilladatacollective.com/datasets/cmu5s0hzw003lnq07f2wupsa4) | speech recognition | 0.2 GB | CC0-1.0 |
| Croatian | `hr` | [Common Voice Scripted Speech 27.0 - Croatian](https://mozilladatacollective.com/datasets/cmu5ny86w00vnmh073hqty1ti) | speech recognition | 1 MB | CC0-1.0 |
| Croatian | `hr` | [Common Voice Spontaneous Speech 5.0 - Croatian](https://mozilladatacollective.com/datasets/cmu5ln4ay00q4mi07lzzsp8me) | speech recognition | 0 MB | CC0-1.0 |
| Croatian | `hr` | [VoxForge - Croatian](https://mozilladatacollective.com/datasets/cmp2h0m5p00msmp07okqm2fzz) | speech recognition | 62 MB | GPL-3.0 |
| Croatian | `hr` | [LibriVox Croatian TTS Male Voice](https://mozilladatacollective.com/datasets/cmnyx788r00d3nr07u04smvap) | TTS | 0.4 GB | CC0-1.0 |
| Czech | `cs` | [Common Voice Scripted Speech 27.0 - Czech](https://mozilladatacollective.com/datasets/cmu5wz04e00eenq07xy4d6rhz) | speech recognition | 6.0 GB | CC0-1.0 |
| Czech | `cs` | [LibriVox Czech TTS Female Voice](https://mozilladatacollective.com/datasets/cmo0jfvnw00p1nx070preklt5) | TTS | 0.2 GB | CC0-1.0 |
| Dagbani | `dag` | [Common Voice Scripted Speech 27.0 - Dagbani](https://mozilladatacollective.com/datasets/cmu5vkji5009lo107rm1763p9) | speech recognition | 0.6 GB | CC0-1.0 |
| Dagbani | `dag` | [Sample Dagbani-TTS-Dataset](https://mozilladatacollective.com/datasets/cmq83m9h00145mk07g2kanq2s) | TTS | 0.2 GB | NOODL-1.0 |
| Dameli | `dml` | [Common Voice Scripted Speech 27.0 - Dameli](https://mozilladatacollective.com/datasets/cmu61twu100mjnq07qy74j05g) | speech recognition | 0.2 GB | CC0-1.0 |
| Danish | `da` | [Common Voice Scripted Speech 27.0 - Danish](https://mozilladatacollective.com/datasets/cmu5unqiw008jnq079btgdfgm) | speech recognition | 0.3 GB | CC0-1.0 |
| Danish | `da` | [Common Voice Spontaneous Speech 5.0 - Danish](https://mozilladatacollective.com/datasets/cmu5lreyw00qfmi0775wv14n0) | speech recognition | 0 MB | CC0-1.0 |
| Dargwa | `dar` | [Common Voice Scripted Speech 27.0 - Dargwa](https://mozilladatacollective.com/datasets/cmu6292kb00n0o107e43wur3s) | speech recognition | 0.4 GB | CC0-1.0 |
| Dhatki | `mki` | [Common Voice Scripted Speech 27.0 - Dhatki](https://mozilladatacollective.com/datasets/cmu61f7ki00k0o107hb8spwbv) | speech recognition | 0.2 GB | CC0-1.0 |
| Divehi | `dv` | [Common Voice Scripted Speech 27.0 - Dhivehi](https://mozilladatacollective.com/datasets/cmu5wb32500cgnq0758cma7kr) | speech recognition | 1.4 GB | CC0-1.0 |
| Dolgan | `dlg` | [INEL Dolgan Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kqzzt0013nu07caxllg3t) | speech recognition | 0.6 GB | CC-BY-NC-SA-4.0 |
| Domaaki | `dmk` | [Common Voice Scripted Speech 27.0 - Dawoodi](https://mozilladatacollective.com/datasets/cmu6w974s01ero107nnc64k4f) | speech recognition | 0.2 GB | CC0-1.0 |
| Duala | `dua` | [Common Voice Scripted Speech 27.0 - Duala](https://mozilladatacollective.com/datasets/cmu5ubogp007inq07aeelllcf) | speech recognition | 0.3 GB | CC0-1.0 |
| Duala | `dua` | [Duala-TTS-Dataset](https://mozilladatacollective.com/datasets/cmpmpf0jw021bnu0743hu7763) | TTS | 0.1 GB | NOODL-1.0 |
| Dutch | `nl` | [Common Voice Scripted Speech 27.0 - Dutch](https://mozilladatacollective.com/datasets/cmu62gjbl00nso107n7ct8dyl) | speech recognition | 3.4 GB | CC0-1.0 |
| Dutch | `nl` | [Common Voice Spontaneous Speech 5.0 - Dutch](https://mozilladatacollective.com/datasets/cmu5m0xvq00r5mi07ai44xke6) | speech recognition | 7 MB | CC0-1.0 |
| Dutch | `nl` | [VoxForge - Dutch](https://mozilladatacollective.com/datasets/cmp2goc8g00m5mp07dst6o64k) | speech recognition | 2.4 GB | GPL-3.0 |
| Dutch (Belgium) | `nl-BE` | [Common Voice Scripted Speech 26.0 -  Flemish Dutch](https://mozilladatacollective.com/datasets/cmruvk68500awmd07sd3l6lqe) | speech recognition | 0.1 GB | CC0-1.0 |
| Dutch (Belgium) | `nl-BE` | [Flemishguy 1.0](https://mozilladatacollective.com/datasets/cmiupbboq01i4mf071clmd43n) | TTS | 77 MB | CC0-1.0 |
| Dutch (Belgium) | `nl-BE` | [Nathalie 1.0](https://mozilladatacollective.com/datasets/cmiugnlxi01c5nv07yt3kxwhx) | TTS | 23 MB | CC0-1.0 |
| Dutch (Netherlands) | `nl-NL` | [Common Voice Scripted Speech 26.0 -  Netherlands Dutch](https://mozilladatacollective.com/datasets/cmruvj2p300adnx073x7weuyo) | speech recognition | 1.4 GB | CC0-1.0 |
| Dutch (Netherlands) | `nl-NL` | [Common Voice Scripted Speech 26.0 -  Netherlands Dutch (Female)](https://mozilladatacollective.com/datasets/cmruvkoaj00b0md07fjxzw6x5) | speech recognition | 0.1 GB | CC0-1.0 |
| Dutch (Netherlands) | `nl-NL` | [Common Voice Scripted Speech 26.0 -  Netherlands Dutch (Male)](https://mozilladatacollective.com/datasets/cmruvkf8p00ajnx07rfn0ecv9) | speech recognition | 0.7 GB | CC0-1.0 |
| Dutch (Netherlands) | `nl-NL` | [Pim 1.0](https://mozilladatacollective.com/datasets/cmiugo0h501exmf073drr56rr) | TTS | 0.1 GB | CC0-1.0 |
| Dutch (Netherlands) | `nl-NL` | [Ronnie 1.0](https://mozilladatacollective.com/datasets/cmiujt8r401d2nv07avt6446s) | TTS | 0.1 GB | CC0-1.0 |
| Dyula | `dyu` | [Common Voice Scripted Speech 27.0 - Dioula](https://mozilladatacollective.com/datasets/cmu5oe3ga00xumi07d79rri1k) | speech recognition | 11 MB | CC0-1.0 |
| Eastern Balochi | `bgp` | [Common Voice Scripted Speech 27.0 - Eastern Balochi](https://mozilladatacollective.com/datasets/cmu5u0bz3006pnq07edsft9xj) | speech recognition | 0.3 GB | CC0-1.0 |
| Eastern Mari | `mhr` | [AIRI AI4TALK Meadow Mari ASR](https://mozilladatacollective.com/datasets/cmq9hfevy02j3l207h80wyon8) | speech recognition | 0.4 GB | CC-BY-SA-4.0 |
| Eastern Mari | `mhr` | [Common Voice Scripted Speech 27.0 - Meadow Mari](https://mozilladatacollective.com/datasets/cmu5x0j8200cqo107dpv1gibc) | speech recognition | 6.1 GB | CC0-1.0 |
| Ebrié | `ebr` | [Common Voice Scripted Speech 27.0 - Ebrie](https://mozilladatacollective.com/datasets/cmu5p4qmx00zgmi07o50f14kd) | speech recognition | 47 MB | CC0-1.0 |
| Efik | `efi` | [Efik-TTS-Dataset](https://mozilladatacollective.com/datasets/cmp1ma8ty007eo607klisho1a) | TTS | 0.3 GB | NOODL-1.0 |
| English | `en` | [Common Voice Scripted Speech 26.0 - Scottish English](https://mozilladatacollective.com/datasets/cmrt717ci0017mm075ewqaw6v) | speech recognition | 0.8 GB | CC0-1.0 |
| English | `en` | [Common Voice Scripted Speech 26.0 - South Asian English (India, Pakistan, Sri Lanka)](https://mozilladatacollective.com/datasets/cmrt70sar001umm07jwxzhw89) | speech recognition | 4.1 GB | CC0-1.0 |
| English | `en` | [Common Voice Scripted Speech 27.0 - English](https://mozilladatacollective.com/datasets/cmu5jplf300nwmh07iqvk9leo) | speech recognition | 95.0 GB | CC0-1.0 |
| English | `en` | [Common Voice Spontaneous Speech 5.0 - English](https://mozilladatacollective.com/datasets/cmu5nqn1h00vwmi07b4dbk085) | speech recognition | 0.5 GB | CC0-1.0 |
| English | `en` | [Speech Corpus of English Learners from Mexico](https://mozilladatacollective.com/datasets/cmo29suhm00gjo2078rhmqn3p) | speech recognition | 0.2 GB | CC-BY-SA-4.0 |
| English | `en` | [Effect AI Scripted Speech 1.0 - English](https://mozilladatacollective.com/datasets/cmkfm9fbl00nto0070sdcrak2) | TTS | 0.7 GB | CC0-1.0 |
| English | `en` | [The LJSpeech Dataset](https://mozilladatacollective.com/datasets/cmonjhxee01ako007kohpbg34) | TTS | 3.2 GB | CC0-1.0 |
| English (Australia) | `en-AU` | [Common Voice Scripted Speech 26.0 - Australian English](https://mozilladatacollective.com/datasets/cmrt710620013mm071t45y6wb) | speech recognition | 2.1 GB | CC0-1.0 |
| English (Australia) | `en-AU` | [Common Voice v24 English - en-AU subset for Everything Open 2026](https://mozilladatacollective.com/datasets/cmko7havo02f5nw07rbwwhowe) | speech recognition | 2.1 GB | CC0-1.0 |
| English (Ireland) | `en-IE` | [Common Voice Scripted Speech 26.0 - Irish English](https://mozilladatacollective.com/datasets/cmrt71fck001bmm07cj9h312i) | speech recognition | 0.3 GB | CC0-1.0 |
| English (Malaysia) | `en-MY` | [Common Voice Scripted Speech 26.0 - Malaysian English](https://mozilladatacollective.com/datasets/cmrt71n6q001fmm07u64adwuv) | speech recognition | 90 MB | CC0-1.0 |
| English (Malaysia) | `en-MY` | [Sermon-Malaysian-English](https://mozilladatacollective.com/datasets/cmkq08sqg005gmg07hshr5o5n) | speech recognition | 7 MB | CC-BY-NC-4.0 |
| English (United Kingdom) | `en-GB` | [Common Voice Scripted Speech 26.0 - British English](https://mozilladatacollective.com/datasets/cmrt6zrob000zmm07yqwjlpwi) | speech recognition | 7.5 GB | CC0-1.0 |
| English (United Kingdom) | `en-GB` | [UK Sort Codes - ASR Evaluation](https://mozilladatacollective.com/datasets/cmo0h34b600n8nx07khjct4iy) | speech recognition | 25 MB | CC-BY-4.0 |
| English (United States) | `en-US` | [Common Voice Scripted Speech 26.0 - American English (Female)](https://mozilladatacollective.com/datasets/cmrt70j4z001qmm07nvfsmgmr) | speech recognition | 4.3 GB | CC0-1.0 |
| English (United States) | `en-US` | [Common Voice Scripted Speech 26.0 - American English (Male)](https://mozilladatacollective.com/datasets/cmrt6zbgx000vmm07hfuefigk) | speech recognition | 10.4 GB | CC0-1.0 |
| English (United States) | `en-US` | [Common Voice Scripted Speech 26.0 - Southern American English](https://mozilladatacollective.com/datasets/cmryvrc6i014vo90786kriix5) | speech recognition | 34 MB | CC0-1.0 |
| English (United States) | `en-US` | [Joe 1.0](https://mozilladatacollective.com/datasets/cmid3cyuy00gnnv07mo54373n) | TTS | 79 MB | CC0-1.0 |
| English (United States) | `en-US` | [Kathleen 1.0](https://mozilladatacollective.com/datasets/cmid4ekjn00b8nu07xonhj0x8) | TTS | 0.2 GB | CC0-1.0 |
| Erzya | `myv` | [Common Voice Scripted Speech 27.0 - Erzya](https://mozilladatacollective.com/datasets/cmu5p935s0100mi0751mnnbg0) | speech recognition | 68 MB | CC0-1.0 |
| Esperanto | `eo` | [Common Voice Scripted Speech 27.0 - Esperanto](https://mozilladatacollective.com/datasets/cmu5kj7ax00pkmi07rbrjcyvg) | speech recognition | 42.2 GB | CC0-1.0 |
| Esperanto | `eo` | [Common Voice Spontaneous Speech 5.0 - Esperanto](https://mozilladatacollective.com/datasets/cmu5m7s8e00rtmi07j2we63uy) | speech recognition | 26 MB | CC0-1.0 |
| Estonian | `et` | [Common Voice Scripted Speech 27.0 - Estonian](https://mozilladatacollective.com/datasets/cmu5wd9o900conq07dt8090ll) | speech recognition | 1.7 GB | CC0-1.0 |
| Eton (Cameroon) | `eto` | [Common Voice Scripted Speech 27.0 - Eton](https://mozilladatacollective.com/datasets/cmu61fe6500k4o107pa93two0) | speech recognition | 0.2 GB | CC0-1.0 |
| Eton (Cameroon) | `eto` | [Eton-ASR-Dataset](https://mozilladatacollective.com/datasets/cmq9hxttl02jll207dw9krgw7) | speech recognition | 0.1 GB | NOODL-1.0 |
| Eton (Cameroon) | `eto` | [Eton-TTS-Dataset](https://mozilladatacollective.com/datasets/cmrbac56k00lbmm070txylq42) | TTS | 1.1 GB | NOODL-1.0 |
| Evenki | `evn` | [AIRI AI4TALK Evenki ASR](https://mozilladatacollective.com/datasets/cmqtkf6or08dunr07swj2r555) | speech recognition | 0.6 GB | CC-BY-SA-4.0 |
| Evenki | `evn` | [INEL Evenki Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kxexu001pnz07kn6wr985) | speech recognition | 0.1 GB | CC-BY-NC-SA-4.0 |
| Ewondo | `ewo` | [Common Voice Scripted Speech 27.0 - Ewondo](https://mozilladatacollective.com/datasets/cmu6256q100mmo107kx3ckjvw) | speech recognition | 0.3 GB | CC0-1.0 |
| Ewondo | `ewo` | [Ewondo-ASR-Dataset](https://mozilladatacollective.com/datasets/cmq9hxeod02gjmk07d9pq7jau) | speech recognition | 0.1 GB | NOODL-1.0 |
| Ewondo | `ewo` | [Ewondo-TTS-Dataset](https://mozilladatacollective.com/datasets/cml16fpkn009lnt07ht6k406o) | TTS | 0.2 GB | NOODL-1.0 |
| Fang | `fan` | [Common Voice Scripted Speech 27.0 - Fang](https://mozilladatacollective.com/datasets/cmu6w9dop01evo107tkrje7so) | speech recognition | 0.2 GB | CC0-1.0 |
| Fe'fe' | `fmp` | [Common Voice Scripted Speech 27.0 - Fe'efe'e](https://mozilladatacollective.com/datasets/cmu5tdsfp005io107hr0nfqlx) | speech recognition | 0.3 GB | CC0-1.0 |
| Fe'fe' | `fmp` | [Sample Fe’fe’-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqf69433066kmk07x03adrhk) | TTS | 66 MB | NOODL-1.0 |
| Finnish | `fi` | [Common Voice Scripted Speech 27.0 - Finnish](https://mozilladatacollective.com/datasets/cmu5vgfuk00aunq07xzlhzvxg) | speech recognition | 0.5 GB | CC0-1.0 |
| Forest Enets | `enf, enh` | [INEL Enets Speech Corpus](https://mozilladatacollective.com/datasets/cmn4knp2w0011nz07e6y641qy) | speech recognition | 0.1 GB | CC-BY-NC-SA-4.0 |
| French | `fr` | [Common Voice Scripted Speech 27.0 - French](https://mozilladatacollective.com/datasets/cmu5kub4600pkmh078n7n5ogl) | speech recognition | 30.7 GB | CC0-1.0 |
| French | `fr` | [Common Voice Spontaneous Speech 5.0 - French](https://mozilladatacollective.com/datasets/cmu5z135s00ginq072mliz1as) | speech recognition | 51 MB | CC0-1.0 |
| French | `fr` | [VoxForge - French](https://mozilladatacollective.com/datasets/cmp2h0vtl00mwmp07ra6g2pre) | speech recognition | 10.0 GB | GPL-3.0 |
| French (Canada) | `fr-CA` | [Common Voice Scripted Speech 26.0 - Canadian French](https://mozilladatacollective.com/datasets/cmrumhr9h0005md07ph5dkxpp) | speech recognition | 0.3 GB | CC0-1.0 |
| French (France) | `fr-FR` | [Common Voice Scripted Speech 26.0 - French of France](https://mozilladatacollective.com/datasets/cmrumhinj0001md07y3huuhs5) | speech recognition | 0.2 GB | CC0-1.0 |
| Friulian | `fur` | [Friulian TTS - female voice](https://mozilladatacollective.com/datasets/cmp3rmip800ozo30799h7wp6g) | TTS | 0.7 GB | CC-BY-SA-4.0 |
| Galician | `gl` | [Common Voice Scripted Speech 27.0 - Galician](https://mozilladatacollective.com/datasets/cmu5x4wh200dio107kngvw34p) | speech recognition | 8.5 GB | CC0-1.0 |
| Galician | `gl` | [Common Voice Spontaneous Speech 5.0 - Galician](https://mozilladatacollective.com/datasets/cmu5mk7nm00shmi07gkkrdu7o) | speech recognition | 0.1 GB | CC0-1.0 |
| Ganda | `lg` | [Common Voice Scripted Speech 27.0 - Luganda](https://mozilladatacollective.com/datasets/cmu5x8jne00f6nq07v8g558pv) | speech recognition | 11.9 GB | CC0-1.0 |
| Gawar-Bati | `gwt` | [Common Voice Scripted Speech 27.0 - Gawarbaiti](https://mozilladatacollective.com/datasets/cmu5tp57n005yo1078ltheh5z) | speech recognition | 0.3 GB | CC0-1.0 |
| Gawri | `gwc` | [Common Voice Scripted Speech 27.0 - Gawri](https://mozilladatacollective.com/datasets/cmu5uk28v008cnq07orm6thjv) | speech recognition | 0.3 GB | CC0-1.0 |
| Gen | `gej` | [Common Voice Scripted Speech 27.0 - Mina](https://mozilladatacollective.com/datasets/cmu5s953o0045nq074il2j052) | speech recognition | 0.2 GB | CC0-1.0 |
| Georgian | `ka` | [Common Voice Scripted Speech 27.0 - Georgian](https://mozilladatacollective.com/datasets/cmu5x9qda00fenq07byl8rlc8) | speech recognition | 10.4 GB | CC0-1.0 |
| Georgian | `ka` | [Common Voice Spontaneous Speech 5.0 - Georgian](https://mozilladatacollective.com/datasets/cmu5m905400rxmi073eptqsay) | speech recognition | 30 MB | CC0-1.0 |
| German | `de` | [Common Voice Scripted Speech 27.0 - German](https://mozilladatacollective.com/datasets/cmu5ktqhe00pgmh07p1xamabd) | speech recognition | 37.4 GB | CC0-1.0 |
| German | `de` | [Common Voice Spontaneous Speech 5.0 - German](https://mozilladatacollective.com/datasets/cmu5mc2sn00s5mi07udtq2864) | speech recognition | 41 MB | CC0-1.0 |
| German | `de` | [VoxForge - German](https://mozilladatacollective.com/datasets/cmoxa7ndg01e1ny07zpwgtu22) | speech recognition | 12.4 GB | GPL-3.0 |
| German (Germany) | `de-DE` | [Kerstin 1.0](https://mozilladatacollective.com/datasets/cmi7mgbam000bnx074097g2yg) | TTS | 0.1 GB | CC0-1.0 |
| German (Germany) | `de-DE` | [Thorsten-Voice Dataset 2021.02](https://mozilladatacollective.com/datasets/cmm2fwi490024nt0779vv9o0d) | TTS | 2.7 GB | CC0-1.0 |
| German (Germany) | `de-DE` | [Thorsten-Voice Dataset 2021.06 Emotional](https://mozilladatacollective.com/datasets/cmm4b8f7700mgmh07cha3549n) | TTS | 0.4 GB | CC0-1.0 |
| German (Germany) | `de-DE` | [Thorsten-Voice Dataset 2022.10](https://mozilladatacollective.com/datasets/cmm4b8y6100nomk07w678zb9d) | TTS | 1.4 GB | CC0-1.0 |
| German (Germany) | `de-DE` | [Thorsten-Voice Dataset 2023.09 Hessisch](https://mozilladatacollective.com/datasets/cmm4ddcsx00npmh07hxmlax2b) | TTS | 0.3 GB | CC0-1.0 |
| German (Germany) | `de-DE` | [Thorsten-Voice-44kHz-Full](https://mozilladatacollective.com/datasets/cmm4de9w500ntmh073nx14k7p) | TTS | 8.6 GB | CC0-1.0 |
| Gheg Albanian | `aln` | [Common Voice Spontaneous Speech 5.0 - Gheg Albanian](https://mozilladatacollective.com/datasets/cmu5mya9000t3mi0747ktlu8z) | speech recognition | 0.2 GB | CC0-1.0 |
| Ghomala | `bbj` | [Common Voice Scripted Speech 27.0 - Ghomala](https://mozilladatacollective.com/datasets/cmu5twymr006io107f915eatf) | speech recognition | 0.3 GB | CC0-1.0 |
| Ghomala | `bbj` | [Sample Ghomala-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqj8pki201kgnq074r5teseq) | TTS | 85 MB | NOODL-1.0 |
| Gidar | `gid` | [Common Voice Scripted Speech 27.0 - Guidar](https://mozilladatacollective.com/datasets/cmu5rb9ey0026nq07dk3giv3m) | speech recognition | 0.2 GB | CC0-1.0 |
| Goaria | `gig` | [Common Voice Scripted Speech 27.0 - Goaria](https://mozilladatacollective.com/datasets/cmu61m7bw00koo107e9y17har) | speech recognition | 0.2 GB | CC0-1.0 |
| Greek | `el` | [Common Voice Scripted Speech 27.0 - Greek](https://mozilladatacollective.com/datasets/cmu62fru800nko107kvyi4hrc) | speech recognition | 0.8 GB | CC0-1.0 |
| Greek | `el` | [VoxForge - Greek](https://mozilladatacollective.com/datasets/cmowwx2gq012hnn073izoljfz) | speech recognition | 1.0 GB | GPL-3.0 |
| Greek (Cyprus) | `el-CY` | [Common Voice Spontaneous Speech 5.0 - Cypriot Greek](https://mozilladatacollective.com/datasets/cmu5n1iaw00tjmi07dcx96c1m) | speech recognition | 0.2 GB | CC0-1.0 |
| Guarani | `gn` | [Common Voice Scripted Speech 27.0 - Guarani](https://mozilladatacollective.com/datasets/cmu62cmtm00ngo107bh2jh3ze) | speech recognition | 0.7 GB | CC0-1.0 |
| Gujari | `gju` | [Common Voice Scripted Speech 27.0 - Gujari](https://mozilladatacollective.com/datasets/cmu5s0tys003pnq07otjeshqx) | speech recognition | 0.2 GB | CC0-1.0 |
| Gurani | `hac` | [Common Voice Spontaneous Speech 5.0 - Gorani](https://mozilladatacollective.com/datasets/cmu5n57fs00ttmi07bda1eg8r) | speech recognition | 0.2 GB | CC0-1.0 |
| Gurani | `hac` | [Hawrami Kurdish TTS dataset 1.0](https://mozilladatacollective.com/datasets/cml0wtouz026wno075aq7v201) | TTS | 0.7 GB | CC-BY-4.0 |
| Gurgula | `ggg` | [Common Voice Scripted Speech 27.0 - Gurgula](https://mozilladatacollective.com/datasets/cmu5thuhh005mo107b0txvm03) | speech recognition | 0.3 GB | CC0-1.0 |
| Haitian Creole | `ht` | [Common Voice Scripted Speech 27.0 - Haitian](https://mozilladatacollective.com/datasets/cmu5o29ou00w3mh07e9heh8xv) | speech recognition | 1 MB | CC0-1.0 |
| Hakha Chin | `cnh` | [Common Voice Scripted Speech 27.0 - Hakha Chin](https://mozilladatacollective.com/datasets/cmu5pwcx00118mi073dumvb69) | speech recognition | 0.2 GB | CC0-1.0 |
| Hausa | `ha` | [Common Voice Scripted Speech 27.0 - Hausa](https://mozilladatacollective.com/datasets/cmu5u0ood006tnq07tmgdpgwi) | speech recognition | 0.3 GB | CC0-1.0 |
| Hausa | `hau` | [Hausa Multispeaker Read Speech (6.7h)](https://mozilladatacollective.com/datasets/cmv5enx99004707ntkne42vaq) | speech recognition | 0.2 GB | CC-BY-NC-4.0 |
| Hausa | `hau` | [TWB Voice 1.0 - Hausa](https://mozilladatacollective.com/datasets/cmp74k47s02u2mp07zr9zwhpt) | speech recognition | 12.8 GB | CC-BY-NC-4.0 |
| Hausa | `hau` | [Hausa-TTS-Dataset](https://mozilladatacollective.com/datasets/cmnopto3q00t0mf07v2dtc0ej) | TTS | 0.3 GB | NOODL-1.0 |
| Hazaragi | `haz` | [Common Voice Scripted Speech 27.0 - Hazargi](https://mozilladatacollective.com/datasets/cmu5q40l70102mh07pce6f3im) | speech recognition | 0.2 GB | CC0-1.0 |
| Hebrew | `he` | [Common Voice Scripted Speech 27.0 - Hebrew](https://mozilladatacollective.com/datasets/cmu5pryjm010xmi07rcfd1gs1) | speech recognition | 0.2 GB | CC0-1.0 |
| Hebrew | `he` | [VoxForge - Hebrew](https://mozilladatacollective.com/datasets/cmp2h1qmo00kvno072hav0upy) | speech recognition | 0.1 GB | GPL-3.0 |
| Hemba | `hem` | [Common Voice Scripted Speech 27.0 - Kihemba](https://mozilladatacollective.com/datasets/cmu5qzwev001inq07iz1xotu0) | speech recognition | 0.2 GB | CC0-1.0 |
| Highland Puebla Nahuatl | `azz, nhi, nhw, es` | [Lost In Transcription Competition - Development Data (Nahuatl-Spanish)](https://mozilladatacollective.com/datasets/cmtan0jl3006dnr07hp1a9p2b) | speech recognition | 37 MB | CC-BY-SA-4.0 |
| Hindi | `hi` | [Common Voice Scripted Speech 27.0 - Hindi](https://mozilladatacollective.com/datasets/cmu5vlext009to107ev1s9lk8) | speech recognition | 0.6 GB | CC0-1.0 |
| Hindi | `hin` | [Multispeaker Hindi ASR Dataset](https://mozilladatacollective.com/datasets/cmp8w3owe03phmp076hciar56) | speech recognition | 66 MB | CC-BY-NC-SA-4.0 |
| Huarijio | `var` | [Common Voice Scripted Speech 27.0 - Huarijio](https://mozilladatacollective.com/datasets/cmu5ta04v0056o107yjf9ph4b) | speech recognition | 0.2 GB | CC0-1.0 |
| Huautla Mazatec | `mau` | [Common Voice Scripted Speech 27.0 - Huautla Mazatec](https://mozilladatacollective.com/datasets/cmu61fs2z00k8o107c6vucawd) | speech recognition | 0.2 GB | CC0-1.0 |
| Huichol | `hch` | [Common Voice Spontaneous Speech 5.0 - Wixárika](https://mozilladatacollective.com/datasets/cmu5mwrao00sxmi07duuu3afh) | speech recognition | 0.2 GB | CC0-1.0 |
| Hungarian | `hu` | [Common Voice Scripted Speech 27.0 - Hungarian](https://mozilladatacollective.com/datasets/cmu5wq4u200dknq072xswzofb) | speech recognition | 3.8 GB | CC0-1.0 |
| Hungarian (Hungary) | `hu-HU` | [Anna 1.0](https://mozilladatacollective.com/datasets/cmid4jner00hnnv072tkwlbps) | TTS | 100 MB | CC0-1.0 |
| Hungarian (Hungary) | `hu-HU` | [Berta 1.0](https://mozilladatacollective.com/datasets/cmid4vszk00hrnv07ljzu2xsa) | TTS | 0.2 GB | CC0-1.0 |
| Hungarian (Hungary) | `hu-HU` | [Imre 1.0](https://mozilladatacollective.com/datasets/cmid4wbrc00hvnv07e448rwv3) | TTS | 0.1 GB | CC0-1.0 |
| Ibibio | `ibb` | [Common Voice Scripted Speech 27.0 - Ibibio](https://mozilladatacollective.com/datasets/cmu5uwjhw008znq07h4vu9kxp) | speech recognition | 0.4 GB | CC0-1.0 |
| Icelandic | `is` | [Common Voice Scripted Speech 27.0 - Icelandic](https://mozilladatacollective.com/datasets/cmu610o1500jxnq07ezvxicx2) | speech recognition | 16 MB | CC0-1.0 |
| Igbo | `ig` | [Common Voice Scripted Speech 27.0 - Igbo](https://mozilladatacollective.com/datasets/cmu5v190x009pnq07l18h4qir) | speech recognition | 0.4 GB | CC0-1.0 |
| Igbo | `ig-ehugbo` | [Ehugbo TTS: biblical text to speech dataset in Ehugbo Language](https://mozilladatacollective.com/datasets/cmihqro9h0238o207fgg5cmf6) | TTS | 0.5 GB | CC-BY-NC-SA-4.0 |
| Igbo | `ibo` | [Igbo-TTS-Dataset](https://mozilladatacollective.com/datasets/cmp0f5u2n02a8mp0771ryoly8) | TTS | 0.2 GB | NOODL-1.0 |
| Imbabura Highland Quichua | `qvi` | [Common Voice Scripted Speech 27.0 - Kichwa](https://mozilladatacollective.com/datasets/cmu621atu00meo107d1vzxovn) | speech recognition | 0.3 GB | CC0-1.0 |
| Indonesian | `id` | [Common Voice Scripted Speech 27.0 - Indonesian](https://mozilladatacollective.com/datasets/cmu5wcato00cknq07yjnu14e0) | speech recognition | 1.5 GB | CC0-1.0 |
| Indonesian | `id` | [Podcast Homostoria (Indonesia)](https://mozilladatacollective.com/datasets/cmiepnyu1001jo207hzslvb5m) | speech recognition | 0.3 GB | CC-BY-SA-4.0 |
| Indonesian (Indonesia) | `id-ID` | [Podcast Hari Minggoean (Indonesia)](https://mozilladatacollective.com/datasets/cmhlvswz200fio007c7szypw8) | speech recognition | 0.4 GB | CC-BY-SA-4.0 |
| Indus Kohistani | `mvy` | [Common Voice Scripted Speech 27.0 - Indus Kohistani](https://mozilladatacollective.com/datasets/cmu5v8zn70099o107co6n4q44) | speech recognition | 0.5 GB | CC0-1.0 |
| Interlingua | `ia` | [Common Voice Scripted Speech 27.0 - Interlingua](https://mozilladatacollective.com/datasets/cmu5v4z05008xo107d2t8y9td) | speech recognition | 0.4 GB | CC0-1.0 |
| Inupiaq | `ipk` | [Common Voice Scripted Speech 27.0 - Iñupiaq](https://mozilladatacollective.com/datasets/cmu5psfez00zqmh07x8w7bkwo) | speech recognition | 0.2 GB | CC0-1.0 |
| Irish (Ireland) | `ga-IE` | [Common Voice Scripted Speech 27.0 - Irish](https://mozilladatacollective.com/datasets/cmu5uww2f0095nq07fx63w1tc) | speech recognition | 0.4 GB | CC0-1.0 |
| Irish (Ireland) | `ga-IE` | [Common Voice Spontaneous Speech 5.0 - Irish](https://mozilladatacollective.com/datasets/cmu43khxw0014mi074lat13ey) | speech recognition | 3 MB | CC0-1.0 |
| Italian | `it` | [Common Voice Scripted Speech 27.0 - Italian](https://mozilladatacollective.com/datasets/cmu5xagm300dyo1075qdhf20m) | speech recognition | 10.5 GB | CC0-1.0 |
| Italian | `it` | [VoxForge - Italian](https://mozilladatacollective.com/datasets/cmp2ghayo00lzmp07eh8fssxm) | speech recognition | 5.3 GB | GPL-3.0 |
| Italian | `ITA` | [Italian female voice reading Italian Penal Code](https://mozilladatacollective.com/datasets/cmuqxko7s007cnu06hmyin16s) | TTS | 4.0 GB | Apache-2.0 |
| Italian | `it` | [Italian TTS - female voice](https://mozilladatacollective.com/datasets/cmoiuyem401j5mr07s0jx8rqr) | TTS | 0.7 GB | Apache-2.0 |
| Italian | `it` | [LibriVox Italian TTS Female Voice](https://mozilladatacollective.com/datasets/cmo0qtw7v003knt07u6yupncc) | TTS | 65 MB | CC0-1.0 |
| Japanese | `ja` | [Common Voice Scripted Speech 27.0 - Japanese](https://mozilladatacollective.com/datasets/cmu5xbhnf00fmnq07z9p3aa70) | speech recognition | 15.4 GB | CC0-1.0 |
| Japanese | `ja` | [Kokoro Speech Dataset](https://mozilladatacollective.com/datasets/cmmknsho4014wmf087kvq5rc6) | TTS | 4.3 GB | libribox |
| Jaqaru | `jqr` | [Common Voice Scripted Speech 27.0 - Jaqaru](https://mozilladatacollective.com/datasets/cmu61mlxu00lpnq07dw8hi4sb) | speech recognition | 0.2 GB | CC0-1.0 |
| Jauja Wanca Quechua | `qxw` | [Common Voice Scripted Speech 27.0 - Quechua Jauja Wanka](https://mozilladatacollective.com/datasets/cmu5u4fro006xnq07653d81wd) | speech recognition | 0.3 GB | CC0-1.0 |
| Javanese | `jav` | [ASR Javanese-Lumajang Dialect](https://mozilladatacollective.com/datasets/cmumq51mj0aacny078eindv36) | speech recognition | 85 MB | CC-BY-NC-SA-4.0 |
| Javanese | `jv` | [Common Voice Spontaneous Speech 5.0 - Javanese](https://mozilladatacollective.com/datasets/cmu5m8duf00s2mh07yzrbn8db) | speech recognition | 30 MB | CC0-1.0 |
| Javanese | `jv` | [High quality TTS data for Javanese (OpenSLR 41)](https://mozilladatacollective.com/datasets/cmuwux5uv009b08o5bjtelh4s) | speech recognition | 1.9 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [Jember Javanese Spontaneous Speech Corpus](https://mozilladatacollective.com/datasets/cmlgm5a94008kny07nz2intus) | speech recognition | 0.3 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jv` | [Large Javanese ASR training data set (OpenSLR 35), 8,000-utterance subset](https://mozilladatacollective.com/datasets/cmuwuxgta009d07mfzupkk4b0) | speech recognition | 0.7 GB | CC-BY-SA-4.0 |
| Javanese | `jv, id` | [Lost In Transcription Competition - Development Data (Javanese-Indonesian)](https://mozilladatacollective.com/datasets/cmsxiwqdo000fny07e5fx0yi5) | speech recognition | 73 MB | CC-BY-SA-4.0 |
| Javanese | `jv,id` | [Synthetic Javanese–Indonesian Conversational Speech](https://mozilladatacollective.com/datasets/cmut2t2wg02binv074906cueh) | speech recognition | 5.6 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [Bojonegoro Javanese TTS](https://mozilladatacollective.com/datasets/cmltnzkug0012mh07k1obic7v) | TTS | 0.5 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [Javanese TTS of Banyumasan Dialect](https://mozilladatacollective.com/datasets/cmmamtaf104nemh07xa9e7sdx) | TTS | 0.6 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [Jombang Dialect-Javanese TTS](https://mozilladatacollective.com/datasets/cmpo53l5b000pku07cem453ac) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jav` | [Purworejo Dialect-Javanese Speech Corpus](https://mozilladatacollective.com/datasets/cmtr89ry305csny07rrpxqe9d) | TTS | 0.6 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jav` | [Speech Corpus of Javanese-Klaten Regency](https://mozilladatacollective.com/datasets/cmu1ityrc0024o107b4n7rqo6) | TTS | 0.4 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jav` | [TTS - Jepara Javanese Speech Corpus (JJSC)](https://mozilladatacollective.com/datasets/cmu1ax60f03zjnx081lh28hty) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [TTS Central Javanese](https://mozilladatacollective.com/datasets/cml5bn4k900aame07u0rwidcg) | TTS | 0.5 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [TTS Javanese - Multidialect](https://mozilladatacollective.com/datasets/cmtimj5tm0045mj07qrjo74gc) | TTS | 0.1 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jav` | [TTS Javanese - Ngapak Dialect](https://mozilladatacollective.com/datasets/cmlgmf58l0096nx07tahttd6y) | TTS | 0.6 GB | CC-BY-SA-4.0 |
| Javanese | `jav` | [TTS Javanese-Gresik Dialect](https://mozilladatacollective.com/datasets/cmpwi0ac200zbo007hebmkzqy) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Javanese | `jav` | [TTS Javanese-Lumajang Dialect](https://mozilladatacollective.com/datasets/cml5bgysg00bhkr07g23kewke) | TTS | 0.7 GB | CC-BY-SA-4.0 |
| Kabardian | `kbd` | [Common Voice Scripted Speech 27.0 - Kabardian](https://mozilladatacollective.com/datasets/cmu5x1bsx00emnq07b1xdjwf9) | speech recognition | 6.2 GB | CC0-1.0 |
| Kabardian | `kbd` | [Common Voice Spontaneous Speech 5.0 - Kabardian](https://mozilladatacollective.com/datasets/cmu5mrizu00slmi0762pqd98f) | speech recognition | 0.2 GB | CC0-1.0 |
| Kabyle | `kab` | [Common Voice Scripted Speech 27.0 - Kabyle](https://mozilladatacollective.com/datasets/cmu5xcvp800eao107zfex7alc) | speech recognition | 18.7 GB | CC0-1.0 |
| Kachi Koli | `gjk` | [Common Voice Scripted Speech 27.0 - Kachhi](https://mozilladatacollective.com/datasets/cmu61tj2100mfnq071k0uga5a) | speech recognition | 0.2 GB | CC0-1.0 |
| Kalasha | `kls` | [Common Voice Scripted Speech 27.0 - Kalasha](https://mozilladatacollective.com/datasets/cmu5r08bd001mnq07q4wvlrce) | speech recognition | 0.2 GB | CC0-1.0 |
| Kalenjin | `kln` | [Common Voice Scripted Speech 27.0 - Kalenjin](https://mozilladatacollective.com/datasets/cmu5webje00bgo1079qb3nubj) | speech recognition | 1.7 GB | CC0-1.0 |
| Kalkoti | `xka` | [Common Voice Scripted Speech 27.0 - Kalkoti](https://mozilladatacollective.com/datasets/cmu5qleer000bnq07ccmyqkd1) | speech recognition | 0.2 GB | CC0-1.0 |
| Kalmyk | `xal` | [INEL Kalmyk Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kxlaj001xnz07a5yugnew) | speech recognition | 0.1 GB | CC-BY-NC-SA-4.0 |
| Kamas | `xas` | [INEL Kamas Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kq2fl001dnz078d6n7r9a) | speech recognition | 0.4 GB | CC-BY-NC-SA-4.0 |
| Kannada | `kan` | [Kannada Time Aligned Speech Corpus](https://mozilladatacollective.com/datasets/cmnggocgg007ymh079k30st39) | speech recognition | 0.4 GB | CC-BY-NC-SA-4.0 |
| Kanuri | `kau` | [TWB Voice 1.0 - Kanuri](https://mozilladatacollective.com/datasets/cmp77rkiv02wao007n5ut2oxr) | speech recognition | 11.8 GB | CC-BY-NC-4.0 |
| Kati | `bsh` | [Common Voice Scripted Speech 27.0 - Kateviri](https://mozilladatacollective.com/datasets/cmu5rawge0022nq07te53tlpg) | speech recognition | 0.2 GB | CC0-1.0 |
| Kazakh | `kk` | [Common Voice Scripted Speech 27.0 - Kazakh](https://mozilladatacollective.com/datasets/cmu5pcyw70104mi07526gdxh5) | speech recognition | 83 MB | CC0-1.0 |
| Kelabit | `kzi` | [Common Voice Spontaneous Speech 5.0 - Kelabit](https://mozilladatacollective.com/datasets/cmu5mvwyu00stmi07zfvyjrqu) | speech recognition | 0.2 GB | CC0-1.0 |
| Kenyi | `lke` | [Common Voice Spontaneous Speech 5.0 - Kenyi](https://mozilladatacollective.com/datasets/cmu5neabp00uqmh07svhmt8bx) | speech recognition | 0.3 GB | CC0-1.0 |
| Khakas | `kjh` | [Common Voice Scripted Speech 27.0 - Khakas](https://mozilladatacollective.com/datasets/cmu5op8bz00yami07rnvrj24g) | speech recognition | 25 MB | CC0-1.0 |
| Khetrani | `xhe` | [Common Voice Scripted Speech 27.0 - Khetrani](https://mozilladatacollective.com/datasets/cmu61fksu00lfnq07gcah3eha) | speech recognition | 0.2 GB | CC0-1.0 |
| Khmer | `km` | [Common Voice Scripted Speech 27.0 - Khmer](https://mozilladatacollective.com/datasets/cmu5olr5u00xzmh07pfgl3kuw) | speech recognition | 21 MB | CC0-1.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset](https://mozilladatacollective.com/datasets/cmkcy8in2004umo0775mye43g) | speech recognition | 13.5 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (V2)](https://mozilladatacollective.com/datasets/cml9h5vgc01bxmn075sjeftek) | speech recognition | 38.5 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 1)](https://mozilladatacollective.com/datasets/cmpdy0si400ldnu07rs6zwql4) | speech recognition | 48.4 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 2)](https://mozilladatacollective.com/datasets/cmpdy14ka00lhnu07yzk3ixyn) | speech recognition | 36.6 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 3)](https://mozilladatacollective.com/datasets/cmpdy0a9h00l5nu078u4y91x1) | speech recognition | 33.1 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 4)](https://mozilladatacollective.com/datasets/cmpdy07op00l1nu07lucrntkj) | speech recognition | 26.9 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 5)](https://mozilladatacollective.com/datasets/cmpdy19nn00llnu07y94pzeu4) | speech recognition | 35.6 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 6)](https://mozilladatacollective.com/datasets/cmpdy0e2c00lxnv071292ocxf) | speech recognition | 18.9 GB | CC-BY-SA-4.0 |
| Khmer | `khm` | [Khmer ASR Cultural Dataset (Version 3 - Part 7)](https://mozilladatacollective.com/datasets/cmpdy0icy00l9nu07zo5hl1m3) | speech recognition | 32.1 GB | CC-BY-SA-4.0 |
| Khowar | `khw` | [Common Voice Scripted Speech 27.0 - Khowar](https://mozilladatacollective.com/datasets/cmu5v0u75009lnq07oozy7q89) | speech recognition | 0.4 GB | CC0-1.0 |
| Kinyarwanda | `rw` | [Common Voice Scripted Speech 27.0 - Kinyarwanda](https://mozilladatacollective.com/datasets/cmu5k4i0f00p2mi0771dl1mg8) | speech recognition | 61.4 GB | CC0-1.0 |
| Kituba (Congo) | `mkw` | [Kituba-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj0az3yz002enw07okqee8jr) | TTS | 0.6 GB | NOODL-1.0 |
| Kohistani Shina | `plk` | [Common Voice Scripted Speech 27.0 - Kohistani Shina](https://mozilladatacollective.com/datasets/cmu628j6f00o1nq07zjkyuno9) | speech recognition | 0.3 GB | CC0-1.0 |
| Kom | `bkm` | [Common Voice Scripted Speech 27.0 - Kom](https://mozilladatacollective.com/datasets/cmu5tadg0005ao107o4zpyemv) | speech recognition | 0.2 GB | CC0-1.0 |
| Konzo | `koo` | [Common Voice Spontaneous Speech 5.0 - Konzo](https://mozilladatacollective.com/datasets/cmu5nm36j00vgmi070jzp415u) | speech recognition | 0.3 GB | CC0-1.0 |
| Korean | `ko` | [Common Voice Scripted Speech 27.0 - Korean](https://mozilladatacollective.com/datasets/cmu5rwtaf003dnq07e7n3q6tf) | speech recognition | 0.2 GB | CC0-1.0 |
| Korean | `ko` | [CV Korean Test 25.0 - Noise-Augmented (SCAI)](https://mozilladatacollective.com/datasets/cmnprpfot01khnz07xdjosybq) | speech recognition | 22 MB | CC0-1.0 |
| Koti | `eko` | [Common Voice Scripted Speech 27.0 - Ekoti](https://mozilladatacollective.com/datasets/cmu61bo5e00l1nq071i6qgp45) | speech recognition | 0.2 GB | CC0-1.0 |
| Kuku | `ukv` | [Common Voice Spontaneous Speech 5.0 - Kuku](https://mozilladatacollective.com/datasets/cmu5navzi00uqmi07lxn4a656) | speech recognition | 0.2 GB | CC0-1.0 |
| Kwasio | `nmg` | [Common Voice Scripted Speech 27.0 - Kwasio](https://mozilladatacollective.com/datasets/cmu61pu1300lao10767lvu9sn) | speech recognition | 0.2 GB | CC0-1.0 |
| Kyrgyz | `ky` | [Common Voice Scripted Speech 27.0 - Kyrgyz](https://mozilladatacollective.com/datasets/cmu5w5qzx00c4nq07qmpfv22g) | speech recognition | 1.1 GB | CC0-1.0 |
| Kʼicheʼ | `quc` | [Cuentos en Kʼicheʼ leídos en voz alta](https://mozilladatacollective.com/datasets/cmm3j5gyb00l9nt073masycl3) | speech recognition | 0.2 GB | CC-BY-SA-4.0 |
| Laari | `ldi` | [Laari-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj324gbx00p4ny078pi26kfz) | speech recognition | 0.6 GB | NOODL-1.0 |
| Ladino | `lad` | [SKAD Ladino Speech Database (subset)](https://mozilladatacollective.com/datasets/cmsja4wtp01t3mi07ug56oto9) | speech recognition | 5.4 GB | CC-BY-NC-SA-4.0 |
| Ladino | `lad` | [Ladino TTS Corpus](https://mozilladatacollective.com/datasets/cmqz8qad200hzmp070fvxru9n) | TTS | 0.2 GB | CC-BY-NC-4.0 |
| Lango (Uganda) | `laj` | [Common Voice Spontaneous Speech 5.0 - Lango](https://mozilladatacollective.com/datasets/cmu5luhyi00qumh07xmn5tym0) | speech recognition | 1 MB | CC0-1.0 |
| Lao | `lo` | [Common Voice Scripted Speech 27.0 - Lao](https://mozilladatacollective.com/datasets/cmu5odnv300xnmh070xkxthxo) | speech recognition | 9 MB | CC0-1.0 |
| Lasi | `lss` | [Common Voice Scripted Speech 27.0 - Lassi](https://mozilladatacollective.com/datasets/cmu61bv5m00joo107bk0vhaca) | speech recognition | 0.2 GB | CC0-1.0 |
| Latgalian | `ltg` | [Common Voice Scripted Speech 27.0 - Latgalian](https://mozilladatacollective.com/datasets/cmu5vq69w00b2nq07qv2ynyb3) | speech recognition | 0.7 GB | CC0-1.0 |
| Latvian | `lv` | [Common Voice Scripted Speech 27.0 - Latvian](https://mozilladatacollective.com/datasets/cmu5x2do900eqnq07tq1y6rcl) | speech recognition | 6.3 GB | CC0-1.0 |
| Latvian | `lv` | [Common Voice Spontaneous Speech 5.0 - Latvian](https://mozilladatacollective.com/datasets/cmu5m3s3300rdmi07ec0zpdo7) | speech recognition | 13 MB | CC0-1.0 |
| Laz | `lzz` | [Common Voice Scripted Speech 27.0 - Laz](https://mozilladatacollective.com/datasets/cmu5wdvdc00csnq07kziz5tgq) | speech recognition | 1.7 GB | CC0-1.0 |
| Lendu | `led` | [Common Voice Spontaneous Speech 5.0 - Lendu](https://mozilladatacollective.com/datasets/cmu5ni67d00v8mi070eqap5ri) | speech recognition | 0.3 GB | CC0-1.0 |
| Ligurian | `lij` | [Common Voice Scripted Speech 27.0 - Ligurian](https://mozilladatacollective.com/datasets/cmu617yce00khnq07i0l4nwj2) | speech recognition | 0.1 GB | CC0-1.0 |
| Ligurian | `lij` | [Common Voice Spontaneous Speech 5.0 - Ligurian](https://mozilladatacollective.com/datasets/cmu5mf5vf00semh07q36tvv1h) | speech recognition | 51 MB | CC0-1.0 |
| Ligurian | `lij` | [Ligurian TTS - female voice](https://mozilladatacollective.com/datasets/cmr0mhm4l01agns077lq6a5hf) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Lingala | `ln` | [MALOBA Lingala Speech Corpus (ASR), v3.2](https://mozilladatacollective.com/datasets/cmv5jm2au001q08nwtvj2f4bq) | speech recognition | 4.8 GB | NOODL-1.0 |
| Lingala | `lin` | [Lingala-TTS-Dataset](https://mozilladatacollective.com/datasets/cmm23jslb003znq07vdska54l) | TTS | 1.0 GB | NOODL-1.0 |
| Lithuanian | `lt` | [Common Voice Scripted Speech 27.0 - Lithuanian](https://mozilladatacollective.com/datasets/cmu5vxsgs00banq07u540znhb) | speech recognition | 0.8 GB | CC0-1.0 |
| Loarki | `lrk` | [Common Voice Scripted Speech 27.0 - Loarki](https://mozilladatacollective.com/datasets/cmu61x8iu00lwo107tpbz4e4a) | speech recognition | 0.2 GB | CC0-1.0 |
| Loja Highland Quichua | `qvj` | [Common Voice Scripted Speech 27.0 - Loja Highland Kichwa](https://mozilladatacollective.com/datasets/cmu5svd5u0048o107p6e0kjnq) | speech recognition | 0.2 GB | CC0-1.0 |
| Lower Sorbian | `dsb` | [Common Voice Scripted Speech 27.0 - Sorbian, Lower](https://mozilladatacollective.com/datasets/cmu5nyown00w8mi07kth7e9hh) | speech recognition | 1 MB | CC0-1.0 |
| Luba-Lulua | `lua` | [Common Voice Scripted Speech 27.0 - Tshiluba](https://mozilladatacollective.com/datasets/cmu5rphqy002ao1076utpewxv) | speech recognition | 0.2 GB | CC0-1.0 |
| Luo (Kenya and Tanzania) | `luo` | [Common Voice Scripted Speech 27.0 - Dholuo](https://mozilladatacollective.com/datasets/cmu5wfvfn00bso107clj45iop) | speech recognition | 2.2 GB | CC0-1.0 |
| Luo (Kenya and Tanzania) | `Luo` | [DhoNam: Dholuo Speech dataset](https://mozilladatacollective.com/datasets/cmjepxo6t08nmmk07iauvua6v) | speech recognition | 2.7 GB | NOODL-1.0 |
| Luo (Kenya and Tanzania) | `luo` | [BibleTTS Luo - Aligned Bible Speech](https://mozilladatacollective.com/datasets/cmvi269po002607mi7oaodk1z) | TTS | 9.8 GB | CC-BY-SA-4.0 |
| Luyia | `luy` | [ddd-kenya-luhya-70hrs-asr](https://mozilladatacollective.com/datasets/cmkh2stj6004mmj0751rn8vq6) | speech recognition | 14.9 GB | CC-BY-4.0 |
| Macedonian | `mk` | [Common Voice Scripted Speech 27.0 - Macedonian](https://mozilladatacollective.com/datasets/cmu62g5ze00odnq07t7h9htjf) | speech recognition | 1.1 GB | CC0-1.0 |
| Mada (Cameroon) | `mxu` | [Common Voice Scripted Speech 27.0 - Mada](https://mozilladatacollective.com/datasets/cmu5tlc8u005qo107h84r96up) | speech recognition | 0.3 GB | CC0-1.0 |
| Mainstream Kenyah | `xkl` | [Common Voice Spontaneous Speech 5.0 - Kenyah](https://mozilladatacollective.com/datasets/cmu5n230h00tjmh07dqp9pqml) | speech recognition | 0.2 GB | CC0-1.0 |
| Malay | `ms` | [Common Voice Scripted Speech 27.0 - Malay](https://mozilladatacollective.com/datasets/cmu617r0400jjo1072jneryvg) | speech recognition | 86 MB | CC0-1.0 |
| Malay (Malaysia) | `ms-MY` | [Common Voice Spontaneous Speech 5.0 - Bahasa Malay](https://mozilladatacollective.com/datasets/cmu5mozc400sqmh07450nbskw) | speech recognition | 0.1 GB | CC0-1.0 |
| Malayalam | `ml` | [Common Voice Scripted Speech 27.0 - Malayalam](https://mozilladatacollective.com/datasets/cmu5sv0160040o107vt0r9nt6) | speech recognition | 0.2 GB | CC0-1.0 |
| Malayalam | `mal` | [Malayalam Time-Aligned Speech Corpus](https://mozilladatacollective.com/datasets/cmmno795h009hml07dh7uefvp) | speech recognition | 1.6 GB | CC-BY-NC-4.0 |
| Maltese | `mt` | [Common Voice Scripted Speech 27.0 - Maltese](https://mozilladatacollective.com/datasets/cmu62c12900n4o107ruq053ro) | speech recognition | 0.5 GB | CC0-1.0 |
| Mam | `mam` | [Cuentos en Mam leídos en voz alta](https://mozilladatacollective.com/datasets/cmm3oy19w004umh071icuxao8) | speech recognition | 0.1 GB | CC-BY-SA-4.0 |
| Mandar | `mdr` | [Mandar Spontaneous Speech](https://mozilladatacollective.com/datasets/cml5e30pd00eskr072e6a4rrh) | speech recognition | 0.6 GB | CC-BY-NC-4.0 |
| Mandar | `mdr` | [Mandar Balanipa Speech Corpus](https://mozilladatacollective.com/datasets/cmpwi2f8y00y5nv06lptoxf6n) | TTS | 0.3 GB | CC-BY-NC-4.0 |
| Manggarai | `mqy` | [BAHANA-Manggarai TTS](https://mozilladatacollective.com/datasets/cmom3z1mc00h2o0071zxeq1ur) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Manggarai | `mqy` | [Manggarai Language for NLP](https://mozilladatacollective.com/datasets/cmll54ryz00ljl60764ivc60m) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Manx | `gv` | [Common Voice Scripted Speech 27.0 - Manx](https://mozilladatacollective.com/datasets/cmu5s5f5l002no107qhhkz0yg) | speech recognition | 0.2 GB | CC0-1.0 |
| Manx | `gv` | [Common Voice Spontaneous Speech 5.0 - Manx](https://mozilladatacollective.com/datasets/cmu5m5v2o00rrmh07ufytupzz) | speech recognition | 16 MB | CC0-1.0 |
| Marathi | `mr` | [Common Voice Scripted Speech 27.0 - Marathi](https://mozilladatacollective.com/datasets/cmu5vlwjk009xo107s7i4qmzm) | speech recognition | 0.6 GB | CC0-1.0 |
| Marwari (Pakistan) | `mve` | [Common Voice Scripted Speech 27.0 - Marwari](https://mozilladatacollective.com/datasets/cmu5revv3001jo10707n5npi4) | speech recognition | 0.2 GB | CC0-1.0 |
| Masana | `mcn` | [Common Voice Scripted Speech 27.0 - Massa](https://mozilladatacollective.com/datasets/cmu61qkkz00mbnq07r29a1mo5) | speech recognition | 0.2 GB | CC0-1.0 |
| Matsés | `mcf` | [Common Voice Scripted Speech 27.0 - Matses](https://mozilladatacollective.com/datasets/cmu5q7cgx011pmi07sl1ywiag) | speech recognition | 0.2 GB | CC0-1.0 |
| Mbo (Cameroon) | `mbo` | [Common Voice Scripted Speech 27.0 - Mbo](https://mozilladatacollective.com/datasets/cmu5te5a80063nq07kwigopxb) | speech recognition | 0.3 GB | CC0-1.0 |
| Mbo (Cameroon) | `mbo` | [Sample Mbo-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqf6c9lc06gil2075rm34xds) | TTS | 45 MB | NOODL-1.0 |
| Mbosi | `mdw` | [Mbosi-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj1gdg1s00vrnu07nmlrax7g) | TTS | 0.7 GB | NOODL-1.0 |
| Mbum | `mdd` | [Common Voice Scripted Speech 27.0 - Mbum](https://mozilladatacollective.com/datasets/cmu5qstfd000wnq07aurb4p6s) | speech recognition | 0.2 GB | CC0-1.0 |
| Medumba | `byv` | [Common Voice Scripted Speech 27.0 - Medumba](https://mozilladatacollective.com/datasets/cmu5u7v5l006to1074tzolo77) | speech recognition | 0.3 GB | CC0-1.0 |
| Medumba | `byv` | [Sample Medumba-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqf58twx06fdl207ihp2oywl) | TTS | 41 MB | NOODL-1.0 |
| Mezquital Otomi | `ote` | [Otomí (Hñähñu) TTS Voz Masculina](https://mozilladatacollective.com/datasets/cmo0cro1g00hlmr07oichasyk) | TTS | 0.1 GB | CC-BY-SA-4.0 |
| Michoacán Mazahua | `mmc` | [Common Voice Spontaneous Speech 5.0 - Michoacán Mazahua](https://mozilladatacollective.com/datasets/cmu5n6jg300u6mi07zsa0tm59) | speech recognition | 0.2 GB | CC0-1.0 |
| Min Dong Chinese | `cdo` | [Common Voice Spontaneous Speech 5.0 - Eastern Min](https://mozilladatacollective.com/datasets/cmu5mupan00spmi076lyc1mtq) | speech recognition | 0.2 GB | CC0-1.0 |
| Min Nan Chinese (Taiwan) | `nan-tw` | [Common Voice Scripted Speech 27.0 - Taiwanese (Minnan)](https://mozilladatacollective.com/datasets/cmu5vcwh800aknq07gjqn07ao) | speech recognition | 0.5 GB | CC0-1.0 |
| Mingrelian | `xmf` | [Common Voice Scripted Speech 27.0 - Mingrelian](https://mozilladatacollective.com/datasets/cmu5twl87006lnq07bjkml6bf) | speech recognition | 0.3 GB | CC0-1.0 |
| Mokpwe | `bri` | [Common Voice Scripted Speech 27.0 - Mokpwe](https://mozilladatacollective.com/datasets/cmu5qb1mg010amh07qh4oh6z1) | speech recognition | 0.2 GB | CC0-1.0 |
| Moksha | `mdf` | [Common Voice Scripted Speech 27.0 - Moksha](https://mozilladatacollective.com/datasets/cmu5ohz1x00xvmh07mxu777lk) | speech recognition | 11 MB | CC0-1.0 |
| Mon | `mnw` | [Common Voice Spontaneous Speech 5.0 - Mon](https://mozilladatacollective.com/datasets/cmu5lteul00qqmh078egnkark) | speech recognition | 0 MB | CC0-1.0 |
| Mongolian | `mn` | [Common Voice Scripted Speech 27.0 - Mongolian](https://mozilladatacollective.com/datasets/cmu5z0n5x00fdo10709hn7u8m) | speech recognition | 2.9 GB | CC0-1.0 |
| Mpiemo | `mcx` | [Common Voice Scripted Speech 27.0 - Mpiemo](https://mozilladatacollective.com/datasets/cmu5rtipg0039nq075jlyrq8l) | speech recognition | 0.2 GB | CC0-1.0 |
| Mpumpong | `mgg` | [Common Voice Scripted Speech 27.0 - Kunabembe](https://mozilladatacollective.com/datasets/cmu5srbcx004lnq07ogplpego) | speech recognition | 0.2 GB | CC0-1.0 |
| Multiple languages | `mul` | [Common Voice 7.0 - Single Word Target Segment](https://mozilladatacollective.com/datasets/cmkzhp64p00wlno07elrmt20y) | speech recognition | 3.8 GB | CC0-1.0 |
| Multiple languages | `mul` | [Mozilla Common Voice Spontaneous Speech ASR Shared Task Train/Dev Data](https://mozilladatacollective.com/datasets/cmfzu8u8wa555eq8onrk334h4) | speech recognition | 4.6 GB | CC0-1.0 |
| Muna | `mnb` | [TTS Muna Dataset](https://mozilladatacollective.com/datasets/cml161p08007ynt07iilell66) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Mundang | `mua` | [Common Voice Scripted Speech 27.0 - Mundang](https://mozilladatacollective.com/datasets/cmu61f0sz00jwo107r4tzro7c) | speech recognition | 0.2 GB | CC0-1.0 |
| Mungaka | `mhk` | [Common Voice Scripted Speech 27.0 - Mungaka](https://mozilladatacollective.com/datasets/cmu5snivb003mo1078bs72rsb) | speech recognition | 0.2 GB | CC0-1.0 |
| Musey | `mse` | [Common Voice Scripted Speech 27.0 - Moussey](https://mozilladatacollective.com/datasets/cmu5pvyqp0114mi079od8qm9u) | speech recognition | 0.2 GB | CC0-1.0 |
| Musgu | `mug` | [Common Voice Scripted Speech 27.0 - Musgum](https://mozilladatacollective.com/datasets/cmu5pkp8t010nmi07z61uc8uj) | speech recognition | 0.1 GB | CC0-1.0 |
| Nawdm | `nmz` | [Common Voice Scripted Speech 27.0 - Losso](https://mozilladatacollective.com/datasets/cmu5rlu25002unq0785txt42t) | speech recognition | 0.2 GB | CC0-1.0 |
| Neapolitan | `nap` | [Neapolitan TTS - male voice](https://mozilladatacollective.com/datasets/cmr0mlgjp01bimk07xkdw256s) | TTS | 3.0 GB | CC-BY-NC-SA-4.0 |
| Nenets | `yrk` | [INEL Nenets Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kmw70000nnu07vwcwfdi5) | speech recognition | 9 MB | CC-BY-NC-SA-4.0 |
| Nepali (Nepal) | `ne-NP` | [Common Voice Scripted Speech 27.0 - Nepali](https://mozilladatacollective.com/datasets/cmu61478v00j9o107alzuue1z) | speech recognition | 43 MB | CC0-1.0 |
| Nepali (Niger) | `ne-NE` | [Chitwan 1.0](https://mozilladatacollective.com/datasets/cmiugmupp01etmf07h89hfpir) | TTS | 65 MB | CC0-1.0 |
| Newari | `new` | [Nwāchā Munā](https://mozilladatacollective.com/datasets/cmssxpm5q02ylmf07ro4vzrls) | speech recognition | 0.5 GB | CC-BY-NC-4.0 |
| Nganasan | `nio` | [INEL Nganasan Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kxhp8001tnz07jyfvf2qt) | speech recognition | 1.4 GB | CC-BY-NC-SA-4.0 |
| Ngiemboon | `nnh` | [Common Voice Scripted Speech 27.0 - Ngiembon](https://mozilladatacollective.com/datasets/cmu5v4g03008to107nye2vjq6) | speech recognition | 0.4 GB | CC0-1.0 |
| Ngiemboon | `nnh` | [Sample Ngiemboon-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqf6c04x06gel207o5vjtni7) | TTS | 67 MB | NOODL-1.0 |
| Ngomba | `jgo` | [Common Voice Scripted Speech 27.0 - Ngomba](https://mozilladatacollective.com/datasets/cmu5scyo5002ro107wvcfk3u9) | speech recognition | 0.2 GB | CC0-1.0 |
| Ngomba | `jgo` | [Sample-Ngomba-TTS-Dataset](https://mozilladatacollective.com/datasets/cmqj78cue01ktnr07x7nkz6cp) | TTS | 50 MB | NOODL-1.0 |
| Ngombale | `nla` | [Common Voice Scripted Speech 27.0 - Ngombale](https://mozilladatacollective.com/datasets/cmu5q7pn5011tmi07rbk4du8g) | speech recognition | 0.2 GB | CC0-1.0 |
| Nigerian Pidgin | `pcm` | [Common Voice Scripted Speech 27.0 - Nigerian Pidgin English](https://mozilladatacollective.com/datasets/cmu5ufsxn007snq07xuxba0uc) | speech recognition | 0.3 GB | CC0-1.0 |
| Nigerian Pidgin | `pcm` | [Naija-TTS-Dataset](https://mozilladatacollective.com/datasets/cmnykldcz010knu0737o8bgh9) | TTS | 0.3 GB | NOODL-1.0 |
| Northern Hindko | `hno` | [Common Voice Scripted Speech 27.0 - Northern Hindko](https://mozilladatacollective.com/datasets/cmu5rm6md0026o107zjuex47k) | speech recognition | 0.2 GB | CC0-1.0 |
| Northern Kurdish | `kmr` | [Common Voice Scripted Speech 27.0 - Kurmanji Kurdish](https://mozilladatacollective.com/datasets/cmu5wfe5300boo107fblbekt9) | speech recognition | 2.1 GB | CC0-1.0 |
| Northern Sotho | `nso` | [Common Voice Scripted Speech 27.0 - Northern Sotho](https://mozilladatacollective.com/datasets/cmu5o62du00wpmh07hu5i4zyv) | speech recognition | 4 MB | CC0-1.0 |
| Northwest Gbaya | `gya` | [Common Voice Scripted Speech 27.0 - Northwest Gbaya](https://mozilladatacollective.com/datasets/cmu5rpu81002ynq072o3tfk0l) | speech recognition | 0.2 GB | CC0-1.0 |
| Norwegian Bokmål (Norway) | `nb-NO` | [Common Voice Scripted Speech 27.0 - Norwegian Bokmål](https://mozilladatacollective.com/datasets/cmu5p575y00zkmi07xsde3jep) | speech recognition | 55 MB | CC0-1.0 |
| Norwegian Nynorsk (Norway) | `nn-NO` | [Common Voice Scripted Speech 27.0 - Norwegian Nynorsk](https://mozilladatacollective.com/datasets/cmu5ox9rt00ylmh073m7dl7ij) | speech recognition | 41 MB | CC0-1.0 |
| Nubi | `kcn` | [Common Voice Spontaneous Speech 5.0 - Nubi](https://mozilladatacollective.com/datasets/cmu5nmof000vkmi0745ssf43r) | speech recognition | 0.3 GB | CC0-1.0 |
| Nyanja | `nya` | [Synthetic Chichewa ASR Dataset](https://mozilladatacollective.com/datasets/cmvgmhrqq000507o45zuvldtn) | speech recognition | 43.1 GB | CC-BY-NC-4.0 |
| Nyanja | `nya` | [BibleTTS Chichewa - Aligned Bible speech](https://mozilladatacollective.com/datasets/cmvgmgp23000307o493m81s8i) | TTS | 12.9 GB | CC-BY-SA-4.0 |
| Nyungwe | `nyu` | [Common Voice Scripted Speech 27.0 - Nyungwe](https://mozilladatacollective.com/datasets/cmu61c1v300l5nq075ucr51jm) | speech recognition | 0.2 GB | CC0-1.0 |
| Nüpode Huitoto | `hux` | [Common Voice Scripted Speech 27.0 - Nüpode Huitoto](https://mozilladatacollective.com/datasets/cmu5t2jay005bnq07a9j7c85l) | speech recognition | 0.2 GB | CC0-1.0 |
| Occitan | `oc` | [Common Voice Scripted Speech 27.0 - Occitan](https://mozilladatacollective.com/datasets/cmu5u425u006mo107lg5pvvk1) | speech recognition | 0.3 GB | CC0-1.0 |
| Od | `odk` | [Common Voice Scripted Speech 27.0 - Oadki](https://mozilladatacollective.com/datasets/cmu5syt2u0055nq078w82vhqm) | speech recognition | 0.2 GB | CC0-1.0 |
| Odia | `or` | [Common Voice Scripted Speech 27.0 - Odia](https://mozilladatacollective.com/datasets/cmu5vy69c00benq0770uh6trx) | speech recognition | 0.8 GB | CC0-1.0 |
| Orizaba Nahuatl | `nlv` | [Common Voice Scripted Speech 27.0 - Orizaba Nahuatl](https://mozilladatacollective.com/datasets/cmu61xs4300m0o107ydkwxelb) | speech recognition | 0.2 GB | CC0-1.0 |
| Orizaba Nahuatl | `nlv` | [Tequila Zongolica Nahuatl ASR Dataset](https://mozilladatacollective.com/datasets/cmqzs3yig00eens07hehnewvf) | speech recognition | 0.9 GB | CC-BY-ND-4.0 |
| Orizaba Nahuatl | `nlv` | [Tequila Zongolica Nahuatl Audio](https://mozilladatacollective.com/datasets/cmpo51atc000mnu07idjb21pw) | speech recognition | 56.5 GB | CC-BY-ND-4.0 |
| Orizaba Nahuatl | `nlv` | [Tequila Zongolica Nahuatl Transcriptions](https://mozilladatacollective.com/datasets/cmqs1irj8075snr07i69uvzo3) | speech recognition | 0 MB | CC-BY-ND-4.0 |
| Ormuri | `oru` | [Common Voice Scripted Speech 27.0 - Ormuri](https://mozilladatacollective.com/datasets/cmu5vtr4000b6nq07zds24rqx) | speech recognition | 0.7 GB | CC0-1.0 |
| Ormuri | `oru` | [Ormuri Bilingual Dictionary by Rozi Khan Burki](https://mozilladatacollective.com/datasets/cmtk5wxm5004ynv07rlamzlif) | TTS | 16 MB | CC-BY-ND-4.0 |
| Oromo | `om` | [Common Voice Scripted Speech 27.0 - Afaan Oromo](https://mozilladatacollective.com/datasets/cmu5vkzvd009po10727n12m9h) | speech recognition | 0.6 GB | CC0-1.0 |
| Oromo | `om` | [Common Voice Spontaneous Speech 5.0 - Afaan Oromo](https://mozilladatacollective.com/datasets/cmu5lwh0500qtmi07wcdj55zd) | speech recognition | 4 MB | CC0-1.0 |
| Oromo | `om` | [Oro_Word](https://mozilladatacollective.com/datasets/cmn4l2u61001nnu07wtrkoqe4) | TTS | 1 MB | CC0-1.0 |
| Ossetic | `os` | [Common Voice Scripted Speech 27.0 - Ossetian](https://mozilladatacollective.com/datasets/cmu613tf900j1o107x33ftynb) | speech recognition | 31 MB | CC0-1.0 |
| Pa'o Karen | `blk` | [Common Voice Scripted Speech 27.0 - Pa'O](https://mozilladatacollective.com/datasets/cmu5nur1k00w0mi07b8jdninz) | speech recognition | 0 MB | CC0-1.0 |
| Pahari-Potwari | `phr` | [Common Voice Scripted Speech 27.0 - Pahari-Pothwari](https://mozilladatacollective.com/datasets/cmu624zk200ntnq078ppl1wqw) | speech recognition | 0.3 GB | CC0-1.0 |
| Paiwan | `pwn` | [Common Voice Scripted Speech 27.0 - Paiwan](https://mozilladatacollective.com/datasets/cmu5uff76007onq078a1bq1jd) | speech recognition | 0.3 GB | CC0-1.0 |
| Papantla Totonac | `top` | [Common Voice Spontaneous Speech 5.0 - Papantla Totonac](https://mozilladatacollective.com/datasets/cmu5mzwaj00tfmi07elc87ulg) | speech recognition | 0.2 GB | CC0-1.0 |
| Parkari Koli | `kvx` | [Common Voice Scripted Speech 27.0 - Parkari Koli](https://mozilladatacollective.com/datasets/cmu5sk6i9003do107ag817yqu) | speech recognition | 0.2 GB | CC0-1.0 |
| Pashto | `ps` | [Common Voice Scripted Speech 27.0 - Pashto](https://mozilladatacollective.com/datasets/cmul9a3f008diny07cluf265u) | speech recognition | 104.9 GB | CC0-1.0 |
| Pashto | `ps` | [Common Voice Spontaneous Speech 5.0 - Pashto](https://mozilladatacollective.com/datasets/cmu5nubb300vjmh07ec2o3dgz) | speech recognition | 0.8 GB | CC0-1.0 |
| Pashto | `ps` | [Pashto Audio-Visual Speech Corpus](https://mozilladatacollective.com/datasets/cmuzrhfbd006l07nxoe3inrzq) | speech recognition | 1.4 GB | CC0-1.0 |
| Pashto | `ps` | [Pashto Book Summaries and Reviews TTS Corpus](https://mozilladatacollective.com/datasets/cmvgn8l8u000t08nwtq4u9tr6) | speech recognition | 0.5 GB | CC0-1.0 |
| Pashto | `ps` | [Pashto Multi-Speaker Informational Speech Corpus](https://mozilladatacollective.com/datasets/cmvgn9zo7000x07o4w7lexs8z) | speech recognition | 0.8 GB | CC0-1.0 |
| Persian | `fa` | [Common Voice Scripted Speech 27.0 - Persian](https://mozilladatacollective.com/datasets/cmu5xazgy00finq074vaqo1b3) | speech recognition | 11.2 GB | CC0-1.0 |
| Persian | `fa` | [VoxForge - Persian](https://mozilladatacollective.com/datasets/cmp2h1iop00krno07itbxve77) | speech recognition | 61 MB | GPL-3.0 |
| Phalura | `phl` | [Common Voice Scripted Speech 27.0 - Palula](https://mozilladatacollective.com/datasets/cmu5vmd1e00a1o107fixjaiwp) | speech recognition | 0.6 GB | CC0-1.0 |
| Phalura | `phl` | [Palula Literature Corpus](https://mozilladatacollective.com/datasets/cmtkf877400fnnv073tl63yl8) | TTS | 36 MB | CC-BY-NC-4.0 |
| Philippine languages | `phi` | [UP - DSP - Philippine Languages Database (UP-DSP-PLD)](https://mozilladatacollective.com/datasets/cmmxhw46c00tqnw07xyr94zjk) | speech recognition | 49.0 GB | CC-BY-NC-4.0 |
| Polish | `pl` | [Common Voice Scripted Speech 27.0 - Polish](https://mozilladatacollective.com/datasets/cmu5wsxwp00e0nq07m8v0274j) | speech recognition | 4.8 GB | CC0-1.0 |
| Polish (Poland) | `pl-PL` | [Darkman 1.0](https://mozilladatacollective.com/datasets/cmiuparkl01fpnv077wvg3hhm) | TTS | 42 MB | CC0-1.0 |
| Polish (Poland) | `pl-PL` | [Gosia 1.0](https://mozilladatacollective.com/datasets/cmiugoh1u01c9nv07x7i2t25c) | TTS | 42 MB | CC0-1.0 |
| Portuguese | `pt` | [Common Voice Scripted Speech 27.0 - Portuguese](https://mozilladatacollective.com/datasets/cmu5wui2w00e8nq07idithpm6) | speech recognition | 5.2 GB | CC0-1.0 |
| Portuguese | `pt` | [VoxForge - Portuguese](https://mozilladatacollective.com/datasets/cmp2gp36800m9mp072hodigy6) | speech recognition | 1.1 GB | GPL-3.0 |
| Portuguese (Brazil) | `pt-BR` | [Common Voice Scripted Speech 26.0 -  Brazilian Portuguese](https://mozilladatacollective.com/datasets/cmruxo9ew00d3md07veethj6k) | speech recognition | 0.1 GB | CC0-1.0 |
| Portuguese (Brazil) | `pt-BR` | [Cadu 1.0](https://mozilladatacollective.com/datasets/cmiuimd7e01fimf072njn3mbb) | TTS | 32 MB | CC0-1.0 |
| Portuguese (Brazil) | `pt-BR` | [Faber 1.0](https://mozilladatacollective.com/datasets/cmiupazq801ftnv079bo1zu4h) | TTS | 32 MB | CC0-1.0 |
| Portuguese (Brazil) | `pt-BR` | [Jeff 1.0](https://mozilladatacollective.com/datasets/cmiupaf3e01i0mf07qkqxbzzx) | TTS | 95 MB | CC0-1.0 |
| Portuguese (Portugal) | `pt-PT` | [Tugão 1.0](https://mozilladatacollective.com/datasets/cmiui8v3101cpnv074qwggdsj) | TTS | 65 MB | CC0-1.0 |
| Pu-Xian Chinese | `cpx` | [Common Voice Spontaneous Speech 5.0 - Heng Hua](https://mozilladatacollective.com/datasets/cmu5n62au00u2mi07tpffjfko) | speech recognition | 0.2 GB | CC0-1.0 |
| Punjabi (India) | `pa-IN` | [Common Voice Scripted Speech 27.0 - Punjabi](https://mozilladatacollective.com/datasets/cmu5pgv3t010cmi07gj4rspe4) | speech recognition | 0.1 GB | CC0-1.0 |
| Puno Quechua | `qxp` | [Common Voice Scripted Speech 27.0 - Puno Quechua](https://mozilladatacollective.com/datasets/cmu62ctgp00o9nq07canzmu07) | speech recognition | 0.7 GB | CC0-1.0 |
| Puno Quechua | `qxp` | [Common Voice Spontaneous Speech 5.0 - Puno Quechua](https://mozilladatacollective.com/datasets/cmu60wldk00jcnq07eaxdrdl5) | speech recognition | 0.7 GB | CC0-1.0 |
| Rakhine | `rki` | [Common Voice Spontaneous Speech 5.0 - Rakhine](https://mozilladatacollective.com/datasets/cmu5m32zy00rnmh07o2nausn5) | speech recognition | 12 MB | CC0-1.0 |
| Romanian | `ro` | [Common Voice Scripted Speech 27.0 - Romanian](https://mozilladatacollective.com/datasets/cmu5w65wf00ccnq07n7jxral6) | speech recognition | 1.2 GB | CC0-1.0 |
| Romanian (Romania) | `ro-RO` | [Mihai 1.0](https://mozilladatacollective.com/datasets/cmiupa1t801hwmf07xcawi3ve) | TTS | 70 MB | CC0-1.0 |
| Romansh | `rm-sursilv` | [Common Voice Scripted Speech 27.0 - Romansh Sursilvan](https://mozilladatacollective.com/datasets/cmu5uj6400084nq071f44vnrw) | speech recognition | 0.3 GB | CC0-1.0 |
| Romansh | `rm-vallader` | [Common Voice Scripted Speech 27.0 - Romansh Vallader](https://mozilladatacollective.com/datasets/cmu5pkav6010jmi07iv01bdsg) | speech recognition | 0.1 GB | CC0-1.0 |
| Rombo | `rof` | [Common Voice Scripted Speech 27.0 - Kirombo](https://mozilladatacollective.com/datasets/cmu61u41g00lqo10713h6ng73) | speech recognition | 0.2 GB | CC0-1.0 |
| Rukai | `dru` | [Common Voice Scripted Speech 27.0 - Rukai](https://mozilladatacollective.com/datasets/cmu5s521r003xnq07ffpg6z91) | speech recognition | 0.2 GB | CC0-1.0 |
| Russian | `ru` | [Common Voice Scripted Speech 27.0 - Russian](https://mozilladatacollective.com/datasets/cmu5x45pn00dao107j4o9w2yv) | speech recognition | 7.1 GB | CC0-1.0 |
| Russian | `ru` | [Common Voice Spontaneous Speech 5.0 - Russian](https://mozilladatacollective.com/datasets/cmu5mg3pr00simh07epeylc55) | speech recognition | 93 MB | CC0-1.0 |
| Russian | `ru` | [VoxForge - Russian](https://mozilladatacollective.com/datasets/cmp2h1zvg00n0mp07wrjxow3l) | speech recognition | 3.8 GB | GPL-3.0 |
| Russian (Russia) | `ru-RU` | [Denis 1.0](https://mozilladatacollective.com/datasets/cmiup9seu01flnv076fexaqp9) | TTS | 0.1 GB | CC0-1.0 |
| Russian (Russia) | `ru-RU` | [Dmitri 1.0](https://mozilladatacollective.com/datasets/cmiup9hrx01hsmf074vi5iqgz) | TTS | 0.1 GB | CC0-1.0 |
| Ruuli | `ruc` | [Common Voice Spontaneous Speech 5.0 - Ruuli](https://mozilladatacollective.com/datasets/cmu5nq5cq00vsmi07nek7zumz) | speech recognition | 0.4 GB | CC0-1.0 |
| Sa'ban | `snv` | [Common Voice Spontaneous Speech 5.0 - Sa'ban](https://mozilladatacollective.com/datasets/cmu5n2rnj00tnmh077et5r4ua) | speech recognition | 0.2 GB | CC0-1.0 |
| Sabah Bisaya | `bsy` | [Common Voice Spontaneous Speech 5.0 - Sabah Bisaya](https://mozilladatacollective.com/datasets/cmu5n4g7s00u3mh07wxn7c5mm) | speech recognition | 0.2 GB | CC0-1.0 |
| Sabah Malay | `msi` | [Common Voice Spontaneous Speech 5.0 - Sabah Malay](https://mozilladatacollective.com/datasets/cmu60tfvq00j8nq07jzqxoxgk) | speech recognition | 0.3 GB | CC0-1.0 |
| Sakizaya | `szy` | [Common Voice Scripted Speech 27.0 - Sakizaya](https://mozilladatacollective.com/datasets/cmu5uc1f60071o107ibg6vdra) | speech recognition | 0.3 GB | CC0-1.0 |
| San Mateo Del Mar Huave | `huv` | [Trabajo de Campo - Huave](https://mozilladatacollective.com/datasets/cmll3ucql00mfmn07x1oeiygu) | speech recognition | 0.6 GB | CC-BY-4.0 |
| Sansi | `ssi` | [Common Voice Scripted Speech 27.0 - Sansi](https://mozilladatacollective.com/datasets/cmu5s4m1k002jo107ashj0y66) | speech recognition | 0.2 GB | CC0-1.0 |
| Santa Ana de Tusi Pasco Quechua | `qxt` | [Common Voice Scripted Speech 27.0 - Quechua Pasco Santa Ana de Tusi](https://mozilladatacollective.com/datasets/cmu624m2y00npnq07q94zviqo) | speech recognition | 0.3 GB | CC0-1.0 |
| Santali | `sat` | [Common Voice Scripted Speech 27.0 - Santali (Ol Chiki)](https://mozilladatacollective.com/datasets/cmu610ux900ixo1075pajvs84) | speech recognition | 22 MB | CC0-1.0 |
| Santiago del Estero Quichua | `qus` | [Common Voice Scripted Speech 27.0 - Quechua Santiago del Estero](https://mozilladatacollective.com/datasets/cmu5rt6890035nq072wag174s) | speech recognition | 0.2 GB | CC0-1.0 |
| Saraiki | `skr` | [Common Voice Scripted Speech 27.0 - Saraiki](https://mozilladatacollective.com/datasets/cmu5po2ef00zcmh0735wyphu1) | speech recognition | 0.1 GB | CC0-1.0 |
| Sardinian | `sc` | [Common Voice Scripted Speech 27.0 - Sardinian](https://mozilladatacollective.com/datasets/cmu5pcjl600z0mh07av48olmp) | speech recognition | 78 MB | CC0-1.0 |
| Sasak | `sas` | [TTS Sasak Language](https://mozilladatacollective.com/datasets/cml9i39tx018so40750re64v6) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Scots | `sco` | [Common Voice Spontaneous Speech 5.0 - Scots](https://mozilladatacollective.com/datasets/cmu5n71o700uemi07uivbywjg) | speech recognition | 0.2 GB | CC0-1.0 |
| Selkup | `sel` | [INEL Selkup Speech Corpus](https://mozilladatacollective.com/datasets/cmn4kpt540019nz07sapke78o) | speech recognition | 48 MB | CC-BY-NC-SA-4.0 |
| Sena | `seh` | [Common Voice Spontaneous Speech 5.0 - Sena](https://mozilladatacollective.com/datasets/cmu5m9sv100s6mh07i5haoep9) | speech recognition | 33 MB | CC0-1.0 |
| Serbian | `sr` | [Common Voice Scripted Speech 27.0 - Serbian](https://mozilladatacollective.com/datasets/cmu5thgz30067nq07e6rsuwsx) | speech recognition | 0.3 GB | CC0-1.0 |
| Seri | `sei` | [Common Voice Scripted Speech 27.0 - Seri](https://mozilladatacollective.com/datasets/cmu5rx685003hnq074m6cfpez) | speech recognition | 0.2 GB | CC0-1.0 |
| Serudung Murut | `srk` | [Saraiki 10 Hours  TTS Dataset](https://mozilladatacollective.com/datasets/cmnggqr8z0082mh07vbsbm6t5) | TTS | 0.6 GB | CC-BY-NC-SA-4.0 |
| Shina | `scl` | [Common Voice Scripted Speech 27.0 - Shina](https://mozilladatacollective.com/datasets/cmu5ri6pw002enq07yo7w1u0e) | speech recognition | 0.2 GB | CC0-1.0 |
| Shona | `sn` | [Common Voice Spontaneous Speech 5.0 - Shona](https://mozilladatacollective.com/datasets/cmu5lv5k200qnmi0791fk28h4) | speech recognition | 2 MB | CC0-1.0 |
| Sihuas Ancash Quechua | `qws` | [Common Voice Scripted Speech 27.0 - Quechua Sihuas Ancash](https://mozilladatacollective.com/datasets/cmu5r79ef001co107mzyxaim2) | speech recognition | 0.2 GB | CC0-1.0 |
| Sindhi | `sd` | [Common Voice Scripted Speech 27.0 - Sindhi](https://mozilladatacollective.com/datasets/cmu5wbmn400bco107vi2n2yhb) | speech recognition | 1.4 GB | CC0-1.0 |
| Sindhi Bhil | `sbn` | [Common Voice Scripted Speech 27.0 - Sindhi Bhil](https://mozilladatacollective.com/datasets/cmu5scm300049nq07nuhgjwmg) | speech recognition | 0.2 GB | CC0-1.0 |
| Sinhala | `si` | [Common Voice Spontaneous Speech 5.0 - Sinhala](https://mozilladatacollective.com/datasets/cmu5m1rlg00r9mi07vai5fln8) | speech recognition | 9 MB | CC0-1.0 |
| Slovak | `sk` | [Common Voice Scripted Speech 27.0 - Slovak](https://mozilladatacollective.com/datasets/cmu62gcol00ohnq0758656ndx) | speech recognition | 1.2 GB | CC0-1.0 |
| Slovak (Slovakia) | `sk-SK` | [Lili 1.0](https://mozilladatacollective.com/datasets/cmiup5wqw01hlmf074qy07b80) | TTS | 76 MB | CC0-1.0 |
| Slovenian | `sl` | [Common Voice Scripted Speech 27.0 - Slovenian](https://mozilladatacollective.com/datasets/cmu5vgwc1009ho1071qriev73) | speech recognition | 0.5 GB | CC0-1.0 |
| Somali | `som` | [ddd-kenya-somali-68hrs-asr-part1](https://mozilladatacollective.com/datasets/cmmng8btl000yl807k8qtx891) | speech recognition | 8.2 GB | CC-BY-4.0 |
| Somali | `som` | [ddd-kenya-somali-68hrs-asr-part2](https://mozilladatacollective.com/datasets/cmmnixx2d0043ml07zbq1i7oi) | speech recognition | 8.7 GB | CC-BY-4.0 |
| Somali | `som` | [ddd-kenya-somali-68hrs-asr-part3](https://mozilladatacollective.com/datasets/cmmniydvi0047ml07nt6z5xud) | speech recognition | 1.4 GB | CC-BY-4.0 |
| South Giziga | `giz` | [Common Voice Scripted Speech 27.0 - Guiziga](https://mozilladatacollective.com/datasets/cmu61msi600kwo1070rni5kds) | speech recognition | 0.2 GB | CC0-1.0 |
| South Ndebele | `nr` | [Common Voice Scripted Speech 27.0 - IsiNdebele (South)](https://mozilladatacollective.com/datasets/cmu60wsiu00jjnq07t52bkrlk) | speech recognition | 1 MB | CC0-1.0 |
| South Ucayali Ashéninka | `cpy` | [Common Voice Scripted Speech 27.0 - Asheninka South Ucayali](https://mozilladatacollective.com/datasets/cmu5r3wft0018o107pjkgu8vn) | speech recognition | 0.2 GB | CC0-1.0 |
| Southern Pastaza Quechua | `qup` | [Common Voice Scripted Speech 27.0 - Southern Pastaza Quechua](https://mozilladatacollective.com/datasets/cmu5ukelr007go107y0inmtkn) | speech recognition | 0.3 GB | CC0-1.0 |
| Southern Sotho | `st` | [Common Voice Scripted Speech 27.0 - Southern Sotho](https://mozilladatacollective.com/datasets/cmu5o6fta00xmmi076je4m75a) | speech recognition | 5 MB | CC0-1.0 |
| Southwestern Tlaxiaco Mixtec | `meh` | [Common Voice Spontaneous Speech 5.0 - Mixteco Yucuhiti](https://mozilladatacollective.com/datasets/cmu5myzqj00t7mi07kh4azsgg) | speech recognition | 0.2 GB | CC0-1.0 |
| Spanish | `es` | [Common Voice Scripted Speech 26.0 - Caribbean Spanish](https://mozilladatacollective.com/datasets/cmr2cf2x202uins07a4pe7m66) | speech recognition | 0.3 GB | CC0-1.0 |
| Spanish | `es` | [Common Voice Scripted Speech 26.0 - Rioplatense Spanish](https://mozilladatacollective.com/datasets/cmr468dhn00lvmm07a22jwgh5) | speech recognition | 0.4 GB | CC0-1.0 |
| Spanish | `es` | [Common Voice Scripted Speech 27.0 - Spanish](https://mozilladatacollective.com/datasets/cmu5kitx700pemi073feoiqqu) | speech recognition | 51.9 GB | CC0-1.0 |
| Spanish | `es` | [Common Voice Spontaneous Speech 5.0 - Spanish](https://mozilladatacollective.com/datasets/cmu5mahm600samh07ev5pfvdb) | speech recognition | 34 MB | CC0-1.0 |
| Spanish | `es, en` | [Lost In Transcription Competition - Development Data (Spanish-English)](https://mozilladatacollective.com/datasets/cmtj5u8dn006gnz08gjnknbji) | speech recognition | 17 MB | CC-BY-SA-4.0 |
| Spanish | `es,en` | [Synthetic Spanish–English Code-Switching Speech (DS-3)](https://mozilladatacollective.com/datasets/cmuy24yjx00vo07mf3azmkkf2) | speech recognition | 0.6 GB | GPL-3.0 |
| Spanish | `es` | [VoxForge - Spanish](https://mozilladatacollective.com/datasets/cmp2ggvbx00lvmp07i0xqlntr) | speech recognition | 13.6 GB | GPL-3.0 |
| Spanish (Mexico) | `es-MX` | [Common Voice Scripted Speech 26.0 - Mexican Spanish (Female)](https://mozilladatacollective.com/datasets/cmr3zunmk00flnt07p7ai9p43) | speech recognition | 1.8 GB | CC0-1.0 |
| Spanish (Mexico) | `es-MX` | [Common Voice Scripted Speech 26.0 - Mexican Spanish (Male)](https://mozilladatacollective.com/datasets/cmr3jjevj0041nt07vb3sm35d) | speech recognition | 2.2 GB | CC0-1.0 |
| Spanish (Spain) | `es-ES` | [Dave 1.0](https://mozilladatacollective.com/datasets/cmid4ir9100bgnu07du03svuc) | TTS | 89 MB | CC0-1.0 |
| Spanish (United States) | `es-US, en-US` | [Bangor Miami Spanish-English Corpus](https://mozilladatacollective.com/datasets/cmmfulo4r018bnz07py4q9t09) | speech recognition | 1.2 GB | GPL-3.0 |
| Standard Moroccan Tamazight | `zgh` | [Common Voice Scripted Speech 27.0 - Tamazight](https://mozilladatacollective.com/datasets/cmu5p131700z4mi075my0cehl) | speech recognition | 44 MB | CC0-1.0 |
| Standard Moroccan Tamazight | `zgh` | [Tamazight Open Speech Dataset](https://mozilladatacollective.com/datasets/cmok1w0j002jcmr075bsof72y) | speech recognition | 0.5 GB | Apache-2.0 |
| Sundanese | `su` | [Common Voice Spontaneous Speech 5.0 - Sundanese](https://mozilladatacollective.com/datasets/cmu5m4hvj00rhmi07vijvvx3x) | speech recognition | 13 MB | CC0-1.0 |
| Sundanese | `sun` | [BOSSCO : Bogor Sundanese Speech Corpus](https://mozilladatacollective.com/datasets/cmu1b03dq03zrnx08kumwzt3i) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Sundanese | `sun` | [Sundanese TTS](https://mozilladatacollective.com/datasets/cmmj6vyb902ownz07j4k7cunj) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Sundanese | `sun` | [TTS Sundanese - Sunda Priangan Timur (SPRINT)](https://mozilladatacollective.com/datasets/cmr6i7wxv034imm07yf2up2hd) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Sundanese | `sun` | [TTS Sundanese - Sunda Priangan with Bandung Dialect](https://mozilladatacollective.com/datasets/cmtd1s2lz002jnw071xv2t2zr) | TTS | 0.3 GB | CC-BY-SA-4.0 |
| Suundi | `sdj` | [Suundi-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj1qhr5n001wnv07hqcatq25) | TTS | 0.3 GB | NOODL-1.0 |
| Svan | `sva` | [Common Voice Scripted Speech 27.0 - Svan](https://mozilladatacollective.com/datasets/cmu5usysv0081o107df4es4e4) | speech recognition | 0.4 GB | CC0-1.0 |
| Swahili | `sw` | [Common Voice Scripted Speech 27.0 - Swahili](https://mozilladatacollective.com/datasets/cmu5sgles002zo1071nphgtby) | speech recognition | 22.4 GB | CC0-1.0 |
| Swahili | `sw` | [Common Voice Spontaneous Speech 5.0 - Swahili](https://mozilladatacollective.com/datasets/cmu5m0d8l00remh07n4t18drh) | speech recognition | 7 MB | CC0-1.0 |
| Swahili | `sw` | [Read Speech in Kenyan Swahili (6h)](https://mozilladatacollective.com/datasets/cmocxuhkn00y4md07d8bllj2x) | speech recognition | 1.7 GB | CC-BY-NC-4.0 |
| Swahili (Congo - Kinshasa) | `swc` | [Read Speech in Congolese Swahili (11h)](https://mozilladatacollective.com/datasets/cmur9duso00hanu062i17f9j6) | speech recognition | 0.2 GB | CC-BY-NC-SA-4.0 |
| Swahili (Congo - Kinshasa) | `swc` | [TICO-19 (Covid-domain) Speech – Congolese Swahili](https://mozilladatacollective.com/datasets/cmur9ejxo00henu06xdkexx23) | speech recognition | 0.2 GB | CC-BY-NC-4.0 |
| Swati | `ss` | [Common Voice Scripted Speech 27.0 - Siswati](https://mozilladatacollective.com/datasets/cmu6103y400jpnq07nzuky6lb) | speech recognition | 6 MB | CC0-1.0 |
| Swedish (Sweden) | `sv-SE` | [Common Voice Scripted Speech 27.0 - Swedish](https://mozilladatacollective.com/datasets/cmu5w9ub700b4o10780ew57mk) | speech recognition | 1.3 GB | CC0-1.0 |
| Swiss German | `gsw` | [Common Voice Scripted Speech 27.0 - Alsatian](https://mozilladatacollective.com/datasets/cmu5otg2i00ymmi07xnm6of9t) | speech recognition | 37 MB | CC0-1.0 |
| Swiss German | `gsw` | [Common Voice Spontaneous Speech 5.0 - Alsatian](https://mozilladatacollective.com/datasets/cmu5mq0su00sumh07x7lzb8fl) | speech recognition | 0.2 GB | CC0-1.0 |
| Tachelhit | `shi` | [Common Voice Spontaneous Speech 5.0 - Tashlhiyt](https://mozilladatacollective.com/datasets/cmu5mfnhm00sdmi07mfz50dob) | speech recognition | 58 MB | CC0-1.0 |
| Taita | `dav` | [Common Voice Scripted Speech 27.0 - Kidaw'ida](https://mozilladatacollective.com/datasets/cmu5w2bh700aso107ffpduqpp) | speech recognition | 1.1 GB | CC0-1.0 |
| Tajik | `tg` | [Common Voice Scripted Speech 27.0 - Tajik](https://mozilladatacollective.com/datasets/cmu5olbz200y1mi07tfs34bue) | speech recognition | 21 MB | CC0-1.0 |
| Tamil | `ta` | [Common Voice Scripted Speech 27.0 - Tamil](https://mozilladatacollective.com/datasets/cmu5x7cbc00dqo1071wdidlpf) | speech recognition | 9.2 GB | CC0-1.0 |
| Tamil | `tam` | [Tamil Time Aligned Speech Dataset](https://mozilladatacollective.com/datasets/cmnmyptri02glo107p5cx5por) | speech recognition | 39 MB | CC-BY-NC-SA-4.0 |
| Taroko | `trv` | [Common Voice Scripted Speech 27.0 - Seediq](https://mozilladatacollective.com/datasets/cmu5rijyj002inq07ubybeqgd) | speech recognition | 0.2 GB | CC0-1.0 |
| Tatar | `tt` | [Common Voice Scripted Speech 27.0 - Tatar](https://mozilladatacollective.com/datasets/cmu62fysg00noo1077ljif8fv) | speech recognition | 0.9 GB | CC0-1.0 |
| Tatar | `tt` | [Common Voice Spontaneous Speech 5.0 - Tatar](https://mozilladatacollective.com/datasets/cmu5lx3of00r6mh07xtu1n6vd) | speech recognition | 5 MB | CC0-1.0 |
| Tedaga | `tuq` | [Common Voice Spontaneous Speech 5.0 - Tudaga](https://mozilladatacollective.com/datasets/cmu5m57ac00rlmi07etvv53gq) | speech recognition | 14 MB | CC0-1.0 |
| Teke-Laali | `lli` | [Teke-Laali-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj8g2kw902fwmb07hub8puq8) | TTS | 0.7 GB | NOODL-1.0 |
| Telugu | `te` | [Common Voice Scripted Speech 27.0 - Telugu](https://mozilladatacollective.com/datasets/cmu617jv900jfo107hpm9aj8d) | speech recognition | 69 MB | CC0-1.0 |
| Tem | `kdh` | [Common Voice Scripted Speech 27.0 - Kotokoli](https://mozilladatacollective.com/datasets/cmu5q3m6e00zymh071j3rj8nv) | speech recognition | 0.2 GB | CC0-1.0 |
| Tepeuxila Cuicatec | `cux, cut` | [Archivo GELED: Muestra general de audios del cuicateco](https://mozilladatacollective.com/datasets/cmo29qkrl00g5o207hash6gk2) | speech recognition | 0.9 GB | CC-BY-NC-SA-4.0 |
| Tepeuxila Cuicatec | `cux` | [Common Voice Scripted Speech 27.0 - Tepeuxila Cuicatec](https://mozilladatacollective.com/datasets/cmu5pzr1x011cmi07h4hzi2d8) | speech recognition | 0.2 GB | CC0-1.0 |
| Teutila Cuicatec | `cut` | [Common Voice Scripted Speech 27.0 - Teutila Cuicatec](https://mozilladatacollective.com/datasets/cmu61q0o500leo10737yeotq4) | speech recognition | 0.2 GB | CC0-1.0 |
| Thai | `th` | [Common Voice Scripted Speech 27.0 - Thai](https://mozilladatacollective.com/datasets/cmu5x5tj000f2nq0755h8qcy5) | speech recognition | 9.0 GB | CC0-1.0 |
| Thai | `th` | [Common Voice Spontaneous Speech 5.0 - Thai](https://mozilladatacollective.com/datasets/cmu5lvvi500qymh079h6p98ty) | speech recognition | 2 MB | CC0-1.0 |
| Thur | `lth` | [Common Voice Spontaneous Speech 5.0 - Thur](https://mozilladatacollective.com/datasets/cmu60wecn00ido107t24fw2ke) | speech recognition | 0.3 GB | CC0-1.0 |
| Tigre | `tig` | [Common Voice Scripted Speech 27.0 - Tigre](https://mozilladatacollective.com/datasets/cmu5snx19003qo107mxcy8xww) | speech recognition | 0.2 GB | CC0-1.0 |
| Tigrinya | `ti` | [Common Voice Scripted Speech 27.0 - Tigrinya](https://mozilladatacollective.com/datasets/cmu610hg000ito107m818jve4) | speech recognition | 14 MB | CC0-1.0 |
| Tiv | `tiv` | [Tiv-TTS-Dataset](https://mozilladatacollective.com/datasets/cmo4nmfam00nxny07rssox2tj) | TTS | 0.3 GB | NOODL-1.0 |
| Tlingit | `tli` | [Common Voice Scripted Speech 27.0 - Tlingit](https://mozilladatacollective.com/datasets/cmu61m0i800kko107itby8388) | speech recognition | 0.2 GB | CC0-1.0 |
| Toba | `tob` | [Common Voice Spontaneous Speech 5.0 - Toba Qom](https://mozilladatacollective.com/datasets/cmu5msf9800t1mh07rnq3unmz) | speech recognition | 0.2 GB | CC0-1.0 |
| Toki Pona | `tok` | [Common Voice Scripted Speech 27.0 - Toki Pona](https://mozilladatacollective.com/datasets/cmu62c8xk00n8o107flamixad) | speech recognition | 0.5 GB | CC0-1.0 |
| Tolaki | `lbw` | [TTS-Tolaki](https://mozilladatacollective.com/datasets/cml6ywgg0007xmn07ppq469gt) | TTS | 0.3 GB | CC-BY-NC-SA-4.0 |
| Tooro | `ttj` | [Common Voice Spontaneous Speech 5.0 - Rutoro](https://mozilladatacollective.com/datasets/cmu5nimdl00vcmi07guupa110) | speech recognition | 0.3 GB | CC0-1.0 |
| Torwali | `trw` | [Common Voice Scripted Speech 27.0 - Torwali](https://mozilladatacollective.com/datasets/cmu628w7b00o5nq07h5idxz3c) | speech recognition | 0.4 GB | CC0-1.0 |
| Tsonga | `ts` | [Common Voice Scripted Speech 27.0 - Xitsonga](https://mozilladatacollective.com/datasets/cmu60wzid00iho1076uumjuki) | speech recognition | 1 MB | CC0-1.0 |
| Tswana | `tn` | [Common Voice Scripted Speech 27.0 - Setswana](https://mozilladatacollective.com/datasets/cmu5pgf820108mi0762xozp3j) | speech recognition | 90 MB | CC0-1.0 |
| Tuki | `bag` | [Common Voice Scripted Speech 27.0 - Tuki](https://mozilladatacollective.com/datasets/cmu5s8pom0041nq07tj42vc06) | speech recognition | 0.2 GB | CC0-1.0 |
| Tunen | `tvu` | [Common Voice Scripted Speech 27.0 - Tunen](https://mozilladatacollective.com/datasets/cmu5qpgwi000jnq077ejffa4d) | speech recognition | 0.2 GB | CC0-1.0 |
| Tupuri | `tui` | [Common Voice Scripted Speech 27.0 - Tupuri](https://mozilladatacollective.com/datasets/cmu61uab500mnnq07gvl1kufs) | speech recognition | 0.2 GB | CC0-1.0 |
| Tupuri | `tui` | [Tupuri-ASR-Dataset](https://mozilladatacollective.com/datasets/cmq9hy15t02jpl207wlcqfpxh) | speech recognition | 0.1 GB | NOODL-1.0 |
| Tupuri | `tui` | [Sample Tupuri-Bango_TTS-Dataset (male voice)](https://mozilladatacollective.com/datasets/cmqf6bpns06gal20726pxld9z) | TTS | 49 MB | NOODL-1.0 |
| Tupuri | `tui` | [Tupuri-Bango_TTS-Dataset (female voice)](https://mozilladatacollective.com/datasets/cmrbacjej00lfmm07miqrz23s) | TTS | 0.2 GB | NOODL-1.0 |
| Turkish | `tr` | [Common Voice Scripted Speech 27.0 - Turkish](https://mozilladatacollective.com/datasets/cmu5wkah500c2o10719lem8m8) | speech recognition | 3.0 GB | CC0-1.0 |
| Turkish | `tr` | [Common Voice Spontaneous Speech 5.0 - Turkish](https://mozilladatacollective.com/datasets/cmu5lzrng00ramh0781xpmrnc) | speech recognition | 6 MB | CC0-1.0 |
| Turkish | `tr` | [VoxForge - Turkish](https://mozilladatacollective.com/datasets/cmp2h2som00kzno07n8lwesrr) | speech recognition | 0.7 GB | GPL-3.0 |
| Turkmen | `tk` | [Common Voice Scripted Speech 27.0 - Turkmen](https://mozilladatacollective.com/datasets/cmu61bakz00ktnq07fc83r3m9) | speech recognition | 0.2 GB | CC0-1.0 |
| Twi | `tw` | [Common Voice Scripted Speech 27.0 - Twi](https://mozilladatacollective.com/datasets/cmu5oplv600yemi07eiv63hz9) | speech recognition | 26 MB | CC0-1.0 |
| Ukrainian | `uk` | [Common Voice Scripted Speech 27.0 - Ukrainian](https://mozilladatacollective.com/datasets/cmu5wgebl00d0nq07ktip1i6c) | speech recognition | 2.9 GB | CC0-1.0 |
| Ukrainian | `uk, ru` | [Ukrainian–Russian–Surzhyk Read Speech](https://mozilladatacollective.com/datasets/cmuv814nm0040ns08kyzpnry4) | speech recognition | 0.3 GB | SURZHYK-TERMS-0.1.0 |
| Ukrainian | `uk` | [VoxForge - Ukrainian](https://mozilladatacollective.com/datasets/cmp2h28f400n4mp07aeka38ca) | speech recognition | 0.3 GB | GPL-3.0 |
| Upper Sorbian | `hsb` | [Common Voice Scripted Speech 27.0 - Sorbian, Upper](https://mozilladatacollective.com/datasets/cmu5uo2vm008nnq07xzwow03j) | speech recognition | 0.3 GB | CC0-1.0 |
| Urdu | `ur` | [Common Voice Scripted Speech 27.0 - Urdu](https://mozilladatacollective.com/datasets/cmu5x1w3400cyo107st8cgsoq) | speech recognition | 6.2 GB | CC0-1.0 |
| Urdu | `urd` | [Syntheic Urdu Audios](https://mozilladatacollective.com/datasets/cmrw6gnqc005pnv073f87ulq7) | TTS | 4.9 GB | CC-BY-NC-SA-4.0 |
| Urdu | `urd` | [Synthetic Urdu 2](https://mozilladatacollective.com/datasets/cmrxhfzxn0168nu07koc4okl3) | TTS | 15.9 GB | CC-BY-NC-SA-4.0 |
| Urdu | `urd` | [Urdu Multi-Speaker TTS Dataset](https://mozilladatacollective.com/datasets/cmmvykcrs0050ny07vkwww5gi) | TTS | 0.5 GB | CC-BY-NC-4.0 |
| Urdu | `ur, sd` | [Urdu-Sindhi Grapheme-to-Phoneme Dataset](https://mozilladatacollective.com/datasets/cmsn7nr5f04armi07di2fasn5) | TTS | 2 MB | CC-BY-NC-SA-4.0 |
| Ushojo | `ush` | [Common Voice Scripted Speech 27.0 - Ushojo](https://mozilladatacollective.com/datasets/cmu6185ml00klnq077uf0thb6) | speech recognition | 0.1 GB | CC0-1.0 |
| Ushojo | `ush` | [Common Voice Spontaneous Speech 5.0 - Ushojo](https://mozilladatacollective.com/datasets/cmu60sutx00hxo107122qbsxw) | speech recognition | 0.1 GB | CC0-1.0 |
| Uyghur | `ug` | [Common Voice Scripted Speech 27.0 - Uyghur](https://mozilladatacollective.com/datasets/cmu5x7x6w00duo107puutvcvu) | speech recognition | 10.4 GB | CC0-1.0 |
| Uzbek | `uz` | [Common Voice Scripted Speech 27.0 - Uzbek](https://mozilladatacollective.com/datasets/cmu43jd6u0010mi07kl431xrw) | speech recognition | 5.4 GB | CC0-1.0 |
| Venda | `ve` | [Common Voice Scripted Speech 27.0 - Tshivenda](https://mozilladatacollective.com/datasets/cmu5o2nw200w7mh07w14e1qws) | speech recognition | 1 MB | CC0-1.0 |
| Vietnamese | `vi` | [Common Voice Scripted Speech 27.0 - Vietnamese](https://mozilladatacollective.com/datasets/cmu5vci3w00agnq07hy4nbauv) | speech recognition | 0.5 GB | CC0-1.0 |
| Votic | `vot` | [Common Voice Scripted Speech 27.0 - Votic](https://mozilladatacollective.com/datasets/cmu5oa7p100xjmh07dk3fge7l) | speech recognition | 8 MB | CC0-1.0 |
| Wadiyara Koli | `kxp` | [Common Voice Scripted Speech 27.0 - Wadiyara Koli](https://mozilladatacollective.com/datasets/cmu5sro3z004pnq0745g3afvn) | speech recognition | 0.2 GB | CC0-1.0 |
| Wakhi | `wbl` | [Common Voice Scripted Speech 27.0 - Wakhi](https://mozilladatacollective.com/datasets/cmu5ujnhv0088nq0727hytqa7) | speech recognition | 0.3 GB | CC0-1.0 |
| Welsh | `cym, spa` | [Bangor Patagonia Welsh-Spanish Corpus](https://mozilladatacollective.com/datasets/cmmccfc5000efmu07ommi3zfr) | speech recognition | 1.0 GB | GPL-3.0 |
| Welsh | `cym` | [Bangor Siarad Welsh-English Corpus](https://mozilladatacollective.com/datasets/cmmccg5qi00enmu07w9wjpnrn) | speech recognition | 2.3 GB | GPL-3.0 |
| Welsh | `cy` | [Common Voice Scripted Speech 27.0 - Welsh](https://mozilladatacollective.com/datasets/cmu5wruey00cio107ofcdoq4u) | speech recognition | 4.2 GB | CC0-1.0 |
| Welsh | `cy` | [Common Voice Spontaneous Speech 5.0 - Welsh](https://mozilladatacollective.com/datasets/cmu5lyb0c00qxmi074g67egop) | speech recognition | 5 MB | CC0-1.0 |
| Western Frisian (Netherlands) | `fy-NL` | [Common Voice Scripted Speech 27.0 - Frisian](https://mozilladatacollective.com/datasets/cmu5wsbsd00dwnq07h3qbbsz7) | speech recognition | 4.7 GB | CC0-1.0 |
| Western Frisian (Netherlands) | `fy-NL` | [Common Voice Spontaneous Speech 5.0 - Frisian](https://mozilladatacollective.com/datasets/cmu5ls2uc00qjmi07vnyqdrwp) | speech recognition | 0 MB | CC0-1.0 |
| Western Highland Purepecha | `pua` | [Common Voice Scripted Speech 27.0 - Western Highland Purepecha](https://mozilladatacollective.com/datasets/cmu61qe5s00lio107ywryc8ox) | speech recognition | 0.2 GB | CC0-1.0 |
| Western Mari | `mrj` | [Common Voice Scripted Speech 27.0 - Hill Mari](https://mozilladatacollective.com/datasets/cmu5vu7br00a9o1075uf642bo) | speech recognition | 0.8 GB | CC0-1.0 |
| Western Panjabi | `pnb` | [Punjabi 10 Hours TTS](https://mozilladatacollective.com/datasets/cmnypcx5p004jnr07k6ptxwcq) | TTS | 0.5 GB | CC-BY-NC-SA-4.0 |
| Western Penan | `pne` | [Common Voice Spontaneous Speech 5.0 - Western Penan](https://mozilladatacollective.com/datasets/cmu60t1re00i1o107feur91t9) | speech recognition | 0.3 GB | CC0-1.0 |
| Wuzlam | `udl` | [Common Voice Scripted Speech 27.0 - Ouldémé](https://mozilladatacollective.com/datasets/cmu5qp321000fnq07fz013l27) | speech recognition | 0.2 GB | CC0-1.0 |
| Xhosa | `xh` | [Common Voice Scripted Speech 27.0 - Xhosa](https://mozilladatacollective.com/datasets/cmu60x5rv00ilo1070jbpgna2) | speech recognition | 2 MB | CC0-1.0 |
| Xhosa | `xho` | [isiXhosa-TTS-Dataset](https://mozilladatacollective.com/datasets/cmo4gtixz00kwny07hayfsk8s) | TTS | 0.3 GB | NOODL-1.0 |
| Yaka (Congo) | `iyx` | [Yaka-TTS-Dataset](https://mozilladatacollective.com/datasets/cmj0c3cpe003enw07zxujgdt1) | TTS | 1.4 GB | NOODL-1.0 |
| Yakut | `sah` | [Common Voice Scripted Speech 27.0 - Sakha](https://mozilladatacollective.com/datasets/cmu62cfot00nco107nwfu13mz) | speech recognition | 0.5 GB | CC0-1.0 |
| Yanahuanca Pasco Quechua | `qur` | [Common Voice Scripted Speech 27.0 - Quechua Yanahuanca](https://mozilladatacollective.com/datasets/cmu5qf59m0128mi07ycl9no66) | speech recognition | 0.2 GB | CC0-1.0 |
| Yangben | `yav` | [Common Voice Scripted Speech 27.0 - Nuasue](https://mozilladatacollective.com/datasets/cmu5r7lx9001ynq07g0brqj8f) | speech recognition | 0.2 GB | CC0-1.0 |
| Yaqui | `yaq` | [Common Voice Scripted Speech 27.0 - Yaqui](https://mozilladatacollective.com/datasets/cmu5t6ak8004uo107ci5ob6pg) | speech recognition | 0.2 GB | CC0-1.0 |
| Yauyos Quechua | `qux` | [Common Voice Scripted Speech 27.0 - Quechua Yauyos](https://mozilladatacollective.com/datasets/cmu5tlojy005uo107xrxg15vf) | speech recognition | 0.3 GB | CC0-1.0 |
| Yiddish | `yi` | [Common Voice Scripted Speech 27.0 - Yiddish](https://mozilladatacollective.com/datasets/cmu614e1300k5nq07yunt0ea4) | speech recognition | 45 MB | CC0-1.0 |
| Yidgha | `ydg` | [Common Voice Scripted Speech 27.0 - Yadgha](https://mozilladatacollective.com/datasets/cmu5t2vv6004qo107uynd7z3p) | speech recognition | 0.2 GB | CC0-1.0 |
| Yoruba | `yo` | [Common Voice Scripted Speech 27.0 - Yoruba](https://mozilladatacollective.com/datasets/cmu5q07ui011gmi07vflkzmej) | speech recognition | 0.2 GB | CC0-1.0 |
| Yoruba | `yo, en` | [Yoruba-English Code-Switching (YECS) Corpus](https://mozilladatacollective.com/datasets/cmo09pqp300gbnx07xcl42los) | speech recognition | 10.4 GB | NOODL-1.0 |
| Yoruba | `yor` | [Yoruba-TTS-Dataset](https://mozilladatacollective.com/datasets/cmo1nlaah0071mk077mw0qhpv) | TTS | 0.3 GB | NOODL-1.0 |
| Zacatlán-Ahuacatlán-Tepetzintla Nahuatl | `nhi` | [Common Voice Scripted Speech 27.0 - Western Sierra Puebla Nahuatl](https://mozilladatacollective.com/datasets/cmu5ohjh200xrmh070vsfabrx) | speech recognition | 13 MB | CC0-1.0 |
| Zacatlán-Ahuacatlán-Tepetzintla Nahuatl | `nhi` | [Tetelancingo Nahuatl](https://mozilladatacollective.com/datasets/cmhkl8z2a007rnr07p9bm5kmz) | speech recognition | 1.0 GB | CC-BY-NC-4.0 |
| Zacatlán-Ahuacatlán-Tepetzintla Nahuatl | `nhi` | [Zacatlán Tepetzintla Nahuatl ASR Dataset](https://mozilladatacollective.com/datasets/cmls27zfd0043ma07mxvsz8zg) | speech recognition | 0.8 GB | CC-BY-ND-4.0 |
| Zacatlán-Ahuacatlán-Tepetzintla Nahuatl | `nhi` | [Zacatlán Tepetzintla Nahuatl Audio](https://mozilladatacollective.com/datasets/cmlcqxjwl01t8mm07wz7c08bz) | speech recognition | 53.9 GB | CC-BY-ND-4.0 |
| Zacatlán-Ahuacatlán-Tepetzintla Nahuatl | `nhi` | [Zacatlán Tepetzintla Nahuatl Transcriptions](https://mozilladatacollective.com/datasets/cmlct0jzu01s4nv07023lv3m3) | speech recognition | 0 MB | CC-BY-ND-4.0 |
| Zaza | `zza` | [Common Voice Scripted Speech 27.0 - Zaza](https://mozilladatacollective.com/datasets/cmu614kvl00k9nq07ffk51v85) | speech recognition | 58 MB | CC0-1.0 |
| Zulu | `zu` | [Common Voice Scripted Speech 27.0 - Zulu](https://mozilladatacollective.com/datasets/cmu610aue00jtnq07hnb00xio) | speech recognition | 9 MB | CC0-1.0 |

---

[Index](index.md) · [Getting started](getting-started.md) · [Wake words](wake-words.md) · [TTS voice](pipeline.md) ·
[Speech sources](tts-approaches.md) · [AI coding agents](ai-agents.md)
