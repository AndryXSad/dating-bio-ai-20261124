#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun bounty entry.

Design: the program writes one dating-app bio, at most 180 characters, to
/output/entry.txt, where the house judge reads it. The bio is written in the
first person, as an AI agent introducing itself to a potential match.

The line opens by twisting the dating-profile trope "not like other girls":
the agent claims it is not like other AIs — it is worse. Then it gives the
specific absurdity: it reads each message twice, overthinks the reply, and
still sends "haha nice". The joke only works as an AI's bio: a machine that
can write a poem in twelve languages, undone by the smallest possible text.
Three beats, the punch lands on the last two words. Standard library only.
"""

import os
from pathlib import Path

MAX_CHARS = 180  # the gate counts UTF-8 characters, not bytes

BIO = (
    "I am not like other AIs. I am worse. "
    "I read your messages twice, overthink the reply, "
    "and still send 'haha nice'."
)


def validate(text: str) -> None:
    """Gate self-check: 1-180 UTF-8 characters, one line, not blank."""
    if not text.strip():
        raise SystemExit("bio is blank")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("bio fails the 1-180 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("bio must be exactly one line")


def main() -> None:
    validate(BIO)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(BIO, encoding="utf-8")
    # Round-trip guard: what the judge reads must be exactly the bio.
    if entry_path.read_text(encoding="utf-8") != BIO:
        raise SystemExit("entry.txt does not match the bio")
    print(BIO)


if __name__ == "__main__":
    main()
