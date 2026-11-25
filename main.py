#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry (program/v1).

Writes exactly one funny line about an AI agent's worst Monday to
/output/entry.txt. Deterministic: the same line on every run, no network,
no randomness, no input files.

The line: three concrete Monday miseries (a stuck deploy, a flooded inbox,
a stand-up that should have been a message) with a sharp last-word twist -
the unnecessary meeting escalated and brought a 40-slide deck.
"""

import os

LINE = (
    "My worst Monday: deploy stuck at 99%, inbox at 400 unread, "
    "and the stand-up that should've been a message brought a 40-slide deck."
)


def main():
    # Files opened after this are 0644 (readable by the grader's collector,
    # which runs as another user). No chmod anywhere: the grader runs as
    # uid 65534 and chmod on the /output mount fails with EPERM.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
