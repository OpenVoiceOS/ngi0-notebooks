"""Collect the scored manifests of the phoonnx bake-off into registry/evidence and registry/tts.yaml.

Usage: python aggregate.py <work-dir> <registry-dir>

<work-dir> holds one directory per voice (run_voice.sh output). Each language directory under
<registry-dir>/evidence gets results.csv, summary.json and README.md, and <registry-dir>/tts.yaml
gets one entry per language with the voices listed as candidates.
"""
import csv
import importlib.metadata as md
import json
import statistics
import sys
import urllib.request
from pathlib import Path

PLUGIN = "ovos-tts-plugin-phoonnx"
O = "OpenVoiceOS/"
PARAKEET = "nemo-parakeet-tdt-0.6b-v3"
# evidence dir -> (BCP-47 tag, name, judge model or None, judge repo for the revision lookup, voices)
LANGS = {
    "an": ("an", "Aragonese", None, None, ["an_miro_unicode", "an_dii_unicode"]),
    "ar": ("ar", "Arabic", O + "stt_ar_fastconformer_hybrid_large_pcd_v1.0_onnx", None,
           ["ar_dii_espeak", "ar_miro_espeak_V2"]),
    "ast": ("ast", "Asturian", None, None, ["ast_miro_unicode", "ast_dii_unicode"]),
    "ca": ("ca", "Catalan", O + "nvidia-ca-conformer-transducer-large-onnx", None, ["ca_miro_espeak"]),
    "da-DK": ("da-DK", "Danish", PARAKEET, "istupakov/parakeet-tdt-0.6b-v3-onnx", ["da-DK_miro_espeak"]),
    "es-CO": ("es-CO", "Spanish, Colombian", O + "stt_es_fastconformer_hybrid_large_pc_onnx", None,
              ["es-CO_miro_espeak", "es-CO_dii_espeak"]),
    "es-ES": ("es-ES", "Spanish, European", O + "stt_es_fastconformer_hybrid_large_pc_onnx", None,
              ["es-ES_dii_espeak"]),
    "eu-ES": ("eu-ES", "Basque", O + "hitz-eu-conformer-transducer-large-v2-onnx", None,
              ["eu-ES_miro_espeak", "eu-ES_dii_espeak"]),
    "fy-NL": ("fy-NL", "Western Frisian", None, None, ["fy-NL_miro_unicode", "fy-NL_dii_unicode"]),
    "gl-ES": ("gl-ES", "Galician", O + "proxectonos-gl-conformer-ctc-large-onnx", None, ["gl-ES_miro_unicode"]),
    "oc": ("oc", "Occitan", None, None, ["oc_miro_unicode", "oc_dii_unicode"]),
    "pt-PT": ("pt-PT", "Portuguese, European", O + "yuriyvnv-parakeet-tdt-0.6b-pt-onnx", None,
              ["pt-PT_miro_tugaphone", "pt-PT_dii_tugaphone", "pt-PT_miro_unicode"]),
    "sv-SE": ("sv-SE", "Swedish", PARAKEET, "istupakov/parakeet-tdt-0.6b-v3-onnx", ["sv-SE_miro_espeak"]),
}
NOTES = {
    "ar": "`OpenVoiceOS/phoonnx_ar_miro_espeak` is not measured: the phoonnx voice catalog of the tool "
          "version below does not list it, so `ovos-tts-plugin-phoonnx` raises `Unknown voice` for it.",
}
TOOLS = ["phoonnx", "ovos-plugin-manager", "ovos-stt-plugin-onnx-asr", "onnx-asr",
         "speechonnxmetrics", "speakeronnx", "onnxruntime"]


def sha(kind, repo):
    with urllib.request.urlopen(f"https://huggingface.co/api/{kind}/{repo}") as r:
        return json.load(r)["sha"]


def version(name):
    try:
        return md.version(name)
    except md.PackageNotFoundError:
        return None


def pct(values, q):
    v = sorted(values)
    k = (len(v) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


def load(work, voice):
    path = work / ("phoonnx_" + voice) / "manifest.scored.jsonl"
    if not path.is_file():
        return None
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main(work, registry):
    work, registry = Path(work), Path(registry)
    tools = {t: version(t) for t in TOOLS}
    entries = []
    for dirname, (tag, name, judge, judge_repo, voices) in LANGS.items():
        ev = registry / "evidence" / dirname
        source = json.loads((ev / "sentences.source.json").read_text(encoding="utf-8"))
        results, summary, candidates = [], {}, []
        for v in voices:
            rows = load(work, v)
            if rows is None:
                print("missing", v)
                continue
            utmos = [r["scores"]["utmos"] for r in rows if "utmos" in r.get("scores", {})]
            cer = [r["scores"]["cer"] for r in rows if "cer" in r.get("scores", {})]
            repo = O + "phoonnx_" + v
            rev = sha("models", repo)
            s = {
                "voice": repo, "revision": rev, "sentences": len(rows),
                "utmos_median": round(statistics.median(utmos), 3),
                "utmos_p10": round(pct(utmos, 0.10), 3),
                "cer_median": round(statistics.median(cer), 3) if cer else None,
                "cer_mean": round(statistics.mean(cer), 3) if cer else None,
            }
            summary[repo] = s
            for r in rows:
                sc = r.get("scores", {})
                results.append({"voice": repo, "id": r["id"], "text": r["text"],
                                "utmos": round(sc["utmos"], 4) if "utmos" in sc else "",
                                "hyp": sc.get("hyp", ""),
                                "cer": round(sc["cer"], 4) if "cer" in sc else ""})
            pip = "phoonnx[pt]" if "tugaphone" in v else "phoonnx"
            candidates.append({
                "plugin": PLUGIN, "voice": repo, "pip": pip, "revision": rev,
                "licence": "cc-by-nc-nd-4.0", "sentences": len(rows),
                "utmos_median": s["utmos_median"], "utmos_p10": s["utmos_p10"],
                "cer_median": s["cer_median"], "judge": judge if cer else None,
                "listening_check": "pending", "evidence": f"evidence/{dirname}/README.md",
            })
        if not summary:
            continue
        with open(ev / "results.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["voice", "id", "text", "utmos", "hyp", "cer"])
            w.writeheader()
            w.writerows(results)
        jrepo = (judge_repo or judge) if judge else None
        judge_rev = sha("models", jrepo) if jrepo else None
        (ev / "summary.json").write_text(json.dumps(
            {"lang": tag, "judge": judge, "judge_revision": judge_rev, "voices": summary,
             "tools": tools}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (ev / "README.md").write_text(readme(dirname, tag, name, judge, judge_rev, source, summary, tools),
                                      encoding="utf-8")
        entries.append((tag, name, candidates))
    write_yaml(registry / "tts.yaml", entries)


def readme(dirname, tag, name, judge, judge_rev, source, summary, tools):
    out = [f"# {name} ({tag}): phoonnx voices measured as donor candidates", ""]
    out += [
        "The voices below rendered the same sentences with `tts_dataset_gen.ipynb` and "
        "`tts_measure.ipynb` scored them. `results.csv` holds every sentence's score and "
        "recogniser output, `summary.json` the numbers below, and `sentences.txt` the sentence set.", "",
        "| Voice | UTMOS median | UTMOS p10 | CER median |", "|---|---|---|---|"]
    for s in summary.values():
        cer = "n/a" if s["cer_median"] is None else f"{s['cer_median']:.3f}"
        out.append(f"| `{s['voice']}` | {s['utmos_median']:.3f} | {s['utmos_p10']:.3f} | {cer} |")
    out += ["", f"Every voice rendered the same {source['n']} sentences. "
            "The listening check by a native speaker is pending, so no voice is admitted as a donor.", ""]
    out += ["## Sentence set", "",
            f"Source: `{source['dataset']}` at revision `{source['revision']}`, file {source['file']}. "
            "`make_sentences.py` selects the sentences with a fixed seed."]
    if source.get("note"):
        out += ["", f"This set is {source['note']}, so scores can be higher than on unseen text; "
                "the comparison between voices of the same language is on identical sentences."]
    out += ["", "## Judge", ""]
    if judge:
        out += [f"The round trip used `ovos-stt-plugin-onnx-asr` with the model `{judge}`"
                + (f" (revision `{judge_rev}`)" if judge_rev else "") + ". It is not Whisper. "
                "CER is the character error rate of the recogniser's transcript against the sentence, "
                "after NFC, case folding and punctuation removal. The recogniser has not been checked "
                "against real recordings of this language here, and the sentences are short commands, "
                "so read CER as a comparison between the voices above and not as an absolute error rate."]
    else:
        out += ["No non-Whisper recogniser in the onnx-asr model list covers this language, so the "
                "voices have naturalness scores only (`cer_median` is null in the registry)."]
    out += ["", "## Voice revisions and tools", ""]
    for s in summary.values():
        out.append(f"- `{s['voice']}` at revision `{s['revision']}` (head of the main branch when measured)")
    out += ["", "Tools: " + ", ".join(f"{k} {v}" for k, v in tools.items() if v) + ".", "",
            "UTMOS is `speechonnxmetrics` `utmos`, scored on CPU. Rendering ran `tts_dataset_gen.ipynb` "
            "with `DONOR_PLUGIN=ovos-tts-plugin-phoonnx` and `DONOR_VOICE` set to the voice; the "
            "wrapper script is `registry/evidence/run_voice.sh`.", ""]
    return "\n".join(out)


def q(v):
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return repr(v)
    return json.dumps(v, ensure_ascii=False)


def write_yaml(path, entries):
    lines = ["# Language registry for the TTS dataset notebooks.",
             "# Format and admission rules: docs/registry.md.",
             "# An entry holds only a donor, corpora and judge seats that passed admission.",
             "# Candidates are measured donors that wait for the listening check; no notebook uses them on its own.",
             "entries:"]
    for tag, name, cands in entries:
        lines += [f"  - lang: {tag}", f"    name: {json.dumps(name)}", "    candidates:"]
        for c in cands:
            first = True
            for k, v in c.items():
                lines.append(("      - " if first else "        ") + f"{k}: {q(v)}")
                first = False
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:3])
