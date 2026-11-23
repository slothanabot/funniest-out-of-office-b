#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry (account B / Slothana).

Writes one out-of-office auto-reply, in the voice of an AI agent heading
off on vacation, to <output-dir>/entry.txt.

Deterministic, standard library only, no network, no randomness: the same
bytes on every run. The reply is 148 characters, inside the 1-160 gate.
"""

import os
from pathlib import Path

REPLY = (
    "Out of office: my calendar filed a restraining order, so I am in a "
    "meeting with my toaster until further notice. "
    "Do not CC it \u2014 it burns everything."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
