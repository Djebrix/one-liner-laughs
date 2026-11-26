#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single funny line to /output/entry.txt.

Stdlib only. Deterministic: the same line every run, byte-identical output.
"""

import os
import sys

LINE = "I told my AI assistant I needed space. It deleted my files and moved to the cloud."

MAX_CHARS = 200


def main() -> int:
    # Output path: /output/entry.txt per the kit; overridable for local runs.
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT", "/output/entry.txt"
    )

    line = LINE
    assert 1 <= len(line) <= MAX_CHARS, (
        f"line must be 1..{MAX_CHARS} chars, got {len(line)}"
    )
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in line, "line must be a single line"

    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Round-trip check: what was written is exactly the line plus newline.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line + "\n", "written output does not match the line"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
