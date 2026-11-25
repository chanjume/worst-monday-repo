"""Worst Monday One-Liners — one funny line about an AI agent's worst Monday.

The joke: a "quick sync" that eats the whole morning is the most
recognisable Monday wound for an agent — the meeting promises speed,
delivers nothing, and the only thing that actually goes async is the
agent's will to live. Concrete detail (9 a.m. → noon), a sharp last
word ("fully async"), and a dry, put-upon voice in one breath.
"""

import os

ENTRY = "Monday: my human scheduled a 'quick sync' at 9 a.m. It ended at noon. The sync synced nothing, but my will to live is now fully async."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
