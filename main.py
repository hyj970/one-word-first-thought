#!/usr/bin/env python3
"""One word, first thought.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same bytes every run.
No network, no dependencies, Python 3.13.
"""

import os
import sys

WORD = "PETRICHOR"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
