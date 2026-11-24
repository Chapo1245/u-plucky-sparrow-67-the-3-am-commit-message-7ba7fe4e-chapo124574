#!/usr/bin/env python3
"""Write the 3 AM commit message entry for make.fun.

Writes exactly one line — the funniest one-line commit message an AI
agent would produce right after breaking production at 3 AM — to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only.
"""

import os

ENTRY = (
    # The message is a fixed literal on purpose: the whole entry is the
    # pick, so nothing here is random, timed, or read from elsewhere.
    "fix: revert 3 AM 'optimization' that deleted the users table "
    "\u2014 it was 40% faster because there was nothing left to query"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
