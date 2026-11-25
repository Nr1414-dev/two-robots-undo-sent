# Two Robots in an Elevator — Undo Auto-File

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Nr1414-dev/two-robots-undo-sent/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Nr1414-dev/two-robots-undo-sent/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

One funny line of awkward small talk a robot says to another in an elevator (167 characters, 169 bytes UTF-8): the robot pressed the other robot's floor, its undo protocol rejected its excuse and auto-filed the real reason — "I wanted to keep talking" — and it just sent, with two floors left to sit with that.

## Run

```sh
python3 main.py  # writes the line to /output/entry.txt
```

Deterministic: every run writes the exact same bytes (sha256 `1c1357ce083ffe409a56ac8fd9c6db5e9cc3d31b4097ee9864950e238cf38d67`). No network, no input files, no randomness.
