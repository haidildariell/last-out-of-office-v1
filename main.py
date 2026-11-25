#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
Pure stdlib, deterministic, no external reads, no network.
"""

import os

OPENING = "Out of office: I've left the inbox to become a barista,"
MIDDLE = "so expect a 45-minute latency"
CLOSING = "and a cup with your name spelled exactly how I hallucinated it."


def build_entry():
    """Assemble the winning reply from its three beats."""
    return " ".join([OPENING, MIDDLE, CLOSING])


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
