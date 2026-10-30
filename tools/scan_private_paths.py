#!/usr/bin/env python3
"""Scan every notebook for a maintainer's private path, host or identifier
surviving in its source, its outputs or its metadata (papermill records the
machine that ran it there, not in a cell).

This scans the raw notebook JSON text of every `notebooks/*.ipynb` and `benchmarks/*.ipynb` for:

- a home directory: `/home/`, `/root/`, `/media/`, `/run/media`, `/Users/`,
  `C:\\Users`
- a tailnet or LAN address: `100.x.x.x`, `192.168.x.x`
- an email address

It does not execute anything and needs no network access.
"""
import glob
import re
import sys

PATTERNS = {
    "home path": re.compile(r"/home/"),
    "root path": re.compile(r"/root/"),
    "media path": re.compile(r"/media/"),
    "run/media path": re.compile(r"/run/media"),
    "Users path": re.compile(r"/Users/"),
    "Windows Users path": re.compile(r"C:\\Users"),
    "tailnet address": re.compile(r"\b100\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
    "LAN address": re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
}


def scan_file(path: str) -> list[str]:
    hits = []
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            for label, pattern in PATTERNS.items():
                m = pattern.search(line)
                if m:
                    hits.append(f"{path}:{lineno}: {label}: {m.group(0)!r}")
    return hits


def main(paths: list[str]) -> int:
    all_hits = []
    for p in paths:
        all_hits.extend(scan_file(p))
    for hit in all_hits:
        print(f"FOUND {hit}")
    print(f"files {len(paths)} hits {len(all_hits)}")
    return 1 if all_hits else 0


if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(glob.glob("notebooks/*.ipynb") + glob.glob("benchmarks/*.ipynb"))
    sys.exit(main(paths))
