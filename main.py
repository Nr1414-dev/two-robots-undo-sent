#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk a robot says to another in an
elevator to /output/entry.txt. Deterministic: every run writes the exact
same bytes. Standard library only, no network, no input files.
"""

import os

ENTRY = (
    "I pressed your floor. My undo protocol rejected my excuse, "
    "auto-filed the real reason \u2014 and it just sent: "
    "'I wanted to keep talking.' Two floors left to sit with that."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
