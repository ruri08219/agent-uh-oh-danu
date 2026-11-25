#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry.

Writes the agent's one-word stall confession to /output/entry.txt.
Standard library only: no third-party imports, so it runs in the
grading sandbox as well as in a clean local directory.

The word: "hallucinating" (13 characters, one token, no spaces,
no punctuation, no trailing newline). It is the honest one-word
thing an agent blurts when it has no idea what to do: it is not
guessing, it is confabulating — and it knows it. Funny on its own,
in a machine's voice, lands at a glance, and not the first obvious
word anyone types.
"""

import os
import sys

WORD = "hallucinating"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
