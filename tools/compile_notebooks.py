#!/usr/bin/env python3
"""Compile every code cell of the given notebooks under the running interpreter.

A `!`/`%` line (papermill/Jupyter magic or shell escape) is not valid Python, so
it and any line it continues onto with a trailing backslash are replaced with
blank statements before compiling. This catches a real `SyntaxError` in a code
cell that `nbformat.validate` (JSON schema only) never looks at; it does not
execute anything, so it needs no network access and no GPU.
"""
import glob
import re
import sys

MAGIC_LINE = re.compile(r"^(\s*)[!%]")


def strip_magics(src: str) -> str:
    out = []
    in_continuation = False
    for line in src.splitlines():
        if in_continuation:
            out.append("")
            in_continuation = line.rstrip().endswith("\\")
            continue
        m = MAGIC_LINE.match(line)
        if m:
            out.append(f"{m.group(1)}pass")
            in_continuation = line.rstrip().endswith("\\")
        else:
            out.append(line)
    return "\n".join(out)


def main(paths: list[str]) -> int:
    bad = 0
    checked = 0
    for p in paths:
        nb = __import__("json").load(open(p, encoding="utf-8"))
        for i, cell in enumerate(nb["cells"]):
            if cell.get("cell_type") != "code":
                continue
            src = "".join(cell.get("source", []))
            src = strip_magics(src)
            checked += 1
            try:
                compile(src, f"{p}:cell{i}", "exec")
            except SyntaxError as e:
                bad += 1
                print(f"SYNTAX {p} cell{i}: {e}")
    print(f"files {len(paths)} code-cells {checked} syntax-errors {bad} "
          f"(python {sys.version.split()[0]})")
    return 1 if bad else 0


if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(glob.glob("notebooks/*.ipynb"))
    sys.exit(main(paths))
