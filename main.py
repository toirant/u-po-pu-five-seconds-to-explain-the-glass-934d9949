#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.

The cat's case, in its own voice: the glass was not an innocent
bystander. It was squatting in the cat's sunspot while reflecting a
rival cat who would not stop staring. A cat does not apologise for
evicting a trespasser; it enforces the lease.
"""

import os
import sys

MAX_CHARS = 200

# The defence, built from its parts so the reasoning stays readable:
# the provocation (a staring rival in the glass), the trespass (the
# sunspot), and the verdict (an eviction, not an accident).
PROVOCATION = "The glass was reflecting a rival cat who kept staring at me"
TRESPASS = "and it was sitting in my sunspot"
VERDICT = "I merely enforced the lease"

FORBIDDEN = ("sorry", "apolog", "my fault", "i didn't mean", "accident")


def build_sentence() -> str:
    """Assemble the cat's one-sentence defence."""
    return f"{PROVOCATION}, {TRESPASS} \u2014 {VERDICT}."


def validate(sentence: str) -> None:
    """The gate: one sentence, 1-200 chars, no apology, no confession."""
    text = sentence.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    lowered = text.lower()
    for word in FORBIDDEN:
        if word in lowered:
            raise ValueError(f"entry must not apologise or confess: {word!r}")


def main() -> int:
    sentence = build_sentence()
    validate(sentence)

    # The grader mounts /output; create it if missing, never remove it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(sentence)
    print(f"wrote {len(sentence)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
