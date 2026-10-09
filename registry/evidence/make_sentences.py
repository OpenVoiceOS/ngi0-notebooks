"""Build the fixed sentence set for each locale of the phoonnx bake-off.

Usage: python make_sentences.py <out_dir>

Sentences come from the public Hugging Face dataset OpenVoiceOS/ovos-intents (utterances of
OVOS skills). Locales that dataset does not carry in usable volume (ar, ast, fy-NL) take sentences from the
voice's own public Common Voice based corpus instead. Selection is deterministic: filter,
shuffle with a fixed seed, round-robin over intent labels.
"""
import csv
import io
import json
import random
import re
import sys
import urllib.request
from pathlib import Path

N = 24
INTENTS = "OpenVoiceOS/ovos-intents"
# locale of the voice -> (source locale folder in ovos-intents, or a corpus repo)
SOURCES = {
    "an": ("intents", "an"),
    "ar": ("corpus", "TigreGotico/tts-train-synthetic-miro_ar-SA"),
    "ast": ("corpus", "TigreGotico/tts_vc_mcv-scripted-v23.0_ast_miro"),
    "ca": ("intents", "ca-ES"),
    "da-DK": ("intents", "da-DK"),
    "es-CO": ("intents", "es-LM+es-ES"),
    "es-ES": ("intents", "es-ES"),
    "eu-ES": ("intents", "eu-ES"),
    "fy-NL": ("corpus", "TigreGotico/tts-vc-mcv-scripted-v24.0-fy-nl-miro"),
    "gl-ES": ("intents", "gl-ES"),
    "oc": ("intents", "oc-FR"),
    "pt-PT": ("intents", "pt-PT"),
    "sv-SE": ("intents", "sv-SE"),
}
BAD = re.compile(r"[{}()\[\]<>|\\/*_@#=+0-9]")


def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8")


def head_sha(kind, repo):
    api = f"https://huggingface.co/api/{kind}/{repo}"
    return json.loads(fetch(api))["sha"]


def ok(text):
    words = text.split()
    return 3 <= len(words) <= 14 and 18 <= len(text) <= 100 and not BAD.search(text)


def pick(rows, seed):
    """rows: (label, text). Round-robin over labels after a seeded shuffle."""
    rng = random.Random(seed)
    by_label = {}
    for label, text in sorted(set(rows)):
        by_label.setdefault(label, []).append(text)
    labels = sorted(by_label)
    rng.shuffle(labels)
    for texts in by_label.values():
        rng.shuffle(texts)
    out, seen = [], set()
    while len(out) < N and any(by_label.values()):
        for label in labels:
            if by_label[label] and len(out) < N:
                t = by_label[label].pop()
                if t.casefold() not in seen:
                    seen.add(t.casefold())
                    out.append(t)
    return out


def main(out_dir):
    out_dir = Path(out_dir)
    intents_sha = head_sha("datasets", INTENTS)
    for lang, (kind, src) in SOURCES.items():
        if kind == "intents":
            rows, used = [], []
            for folder in src.split("+"):
                for name in ("test.jsonl", "train_templates.jsonl"):
                    try:
                        text = fetch(f"https://huggingface.co/datasets/{INTENTS}/resolve/{intents_sha}/{folder}/{name}")
                    except Exception:
                        continue
                    before = len(set(rows))
                    for line in text.splitlines():
                        r = json.loads(line)
                        u = r["utterance"]
                        if ok(u):
                            rows.append((r["label"], u))
                    used.append(f"{folder}/{name}")
                    if len(set(rows)) - before >= N:
                        break
                if len(set(rows)) >= N:
                    break
            origin = {"dataset": INTENTS, "revision": intents_sha, "file": ", ".join(used)}
        else:
            sha = head_sha("datasets", src)
            text = fetch(f"https://huggingface.co/datasets/{src}/resolve/{sha}/metadata.csv")
            rows = []
            for rec in csv.reader(io.StringIO(text), delimiter="|"):
                if len(rec) >= 2 and ok(rec[-1].strip()):
                    rows.append(("all", rec[-1].strip()))
            origin = {"dataset": src, "revision": sha, "file": "metadata.csv",
                      "note": "the voice's own training corpus, not held out"}
        sentences = pick(rows, seed=lang)
        d = out_dir / lang
        d.mkdir(parents=True, exist_ok=True)
        (d / "sentences.txt").write_text("\n".join(sentences) + "\n", encoding="utf-8")
        (d / "sentences.source.json").write_text(
            json.dumps({"lang": lang, "n": len(sentences), **origin}, indent=2), encoding="utf-8")
        print(lang, len(sentences), origin["file"])


if __name__ == "__main__":
    main(sys.argv[1])
