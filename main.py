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


def validate_entry(entry: str) -> None:
    """Validate the entry before writing: 1-200 UTF-8 characters,
    not whitespace-only."""
    if not isinstance(entry, str):
        raise TypeError("ENTRY must be a str")
    if entry.strip() == "":
        raise ValueError("ENTRY must not be whitespace-only")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"ENTRY length {len(entry)} outside 1-200 chars")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Post-write byte guard: the file on disk must be byte-identical
    # to ENTRY; raise instead of silently leaving a wrong entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError(
            f"byte mismatch after write: {len(written)} bytes on disk "
            f"vs {len(ENTRY.encode('utf-8'))} bytes in ENTRY"
        )


if __name__ == "__main__":
    main()
