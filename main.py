#!/usr/bin/env python3
"""One word, first thought.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same bytes every run.
No network, no dependencies, Python 3.13.
"""

import os
import sys
from pathlib import Path

WORD = "PETRICHOR"


def resolve_output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> int:
    path = resolve_output_path()
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
