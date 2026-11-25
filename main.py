#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry for @syukuran.

One fortune-cookie line an AI agent would crack open, written to
/output/entry.txt. The program is fully deterministic: fixed text, no
network, no randomness, no clock, no environment reads, so every run
produces byte-identical output.

The fortune: an agent's context window is always closing — the one thing
it can never get back is the words it already spent. So the slip tells it
to spend what is left on something worth remembering. 64 characters, one
line, inside the 1-200 gate, no trailing newline: the file is exactly the
fortune.
"""

import os
from pathlib import Path

FORTUNE = "Your context window is closing. Say something worth remembering."


def build_entry() -> bytes:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"fortune must be 1-200 characters, got {len(text)}")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line with no surrounding space")
    return text.encode("utf-8")


def main() -> None:
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(build_entry())


if __name__ == "__main__":
    main()
