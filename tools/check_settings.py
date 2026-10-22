#!/usr/bin/env python3
"""Check the settings layout of every notebook.

The first code cell is the hidden helper, byte for byte the text of tools/settings_helper.py. The second code cell is
the Settings cell, and it is the only cell that calls setting() with a fixed name. A later cell may call setting()
with a name built at run time, such as REFERENCE_<voice name>. No cell reads a setting from os.environ, and no cell
calls os.environ.setdefault(). A notebook in NO_SETTINGS has no settings, so it has neither cell.
"""
import glob
import json
import re
import sys
from pathlib import Path

HELPER = (Path(__file__).parent / "settings_helper.py").read_text(encoding="utf-8")
SETTINGS_FIRST_LINE = "# Settings: change the values below."
SETTING_LINE = re.compile(r'^([A-Z][A-Z0-9_]*) = setting\("([A-Z][A-Z0-9_]*)", ')
NO_SETTINGS = {"bus_message_validation"}
SHELL_NAMES = {"LANG", "HOME", "PATH", "USER", "TMPDIR", "PWD", "SHELL", "TERM"}


def check(path):
    errors = []
    cells = [c for c in json.load(open(path, encoding="utf-8"))["cells"] if c["cell_type"] == "code"]
    sources = ["".join(c["source"]) for c in cells]
    if Path(path).stem in NO_SETTINGS:
        if any(re.search(r"\bsetting\(", src) for src in sources):
            return ["the notebook is in NO_SETTINGS, but a cell calls setting()"]
        return []
    if len(cells) < 2 or sources[0] != HELPER:
        return ["the first code cell is not the text of tools/settings_helper.py"]
    if not cells[0].get("metadata", {}).get("jupyter", {}).get("source_hidden"):
        errors.append("the helper cell is not hidden")
    if not sources[1].startswith(SETTINGS_FIRST_LINE):
        errors.append(f"the second code cell does not start with {SETTINGS_FIRST_LINE!r}")
    names = set()
    for line in sources[1].splitlines():
        if "setting(" in line and not line.lstrip().startswith("#"):
            m = SETTING_LINE.match(line)
            if not m or m.group(1) != m.group(2):
                errors.append(f"Settings cell line is not NAME = setting(\"NAME\", ...): {line.strip()}")
            else:
                names.add(m.group(1))
    for name in sorted(names & SHELL_NAMES):
        errors.append(f"{name} is set by the shell, so it cannot be a setting")
    for i, (cell, src) in enumerate(zip(cells, sources)):
        if "parameters" in (cell.get("metadata", {}).get("tags") or []):
            errors.append(f"code cell {i} is tagged parameters")
        if "os.environ.setdefault(" in src:
            errors.append(f"code cell {i} calls os.environ.setdefault()")
        if i > 1 and re.search(r"\bsetting\(\s*[\"']", src):
            errors.append(f"code cell {i} calls setting(); only the Settings cell may")
        if i > 0:
            reads = re.findall(r'os\.(?:environ\.get\(|getenv\()\s*["\']([A-Z][A-Z0-9_]*)', src)
            reads += re.findall(r'os\.environ\[\s*["\']([A-Z][A-Z0-9_]*)["\']\s*\](?!\s*=[^=])', src)
            for name in reads:
                if name in names:
                    errors.append(f"code cell {i} reads the setting {name} from os.environ")
    return errors


def main():
    paths = sorted(glob.glob("notebooks/*.ipynb"))
    failed = 0
    for path in paths:
        errors = check(path)
        print(f"  {'FAIL' if errors else 'OK  '} {path}")
        for e in errors:
            print(f"       {e}")
        failed += bool(errors)
    print(f"{len(paths)} notebooks checked, {failed} failed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
