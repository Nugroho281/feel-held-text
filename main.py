#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel held" bounty.

Writes one short text (the winning candidate from variants.md) to
/output/entry.txt. Pure Python standard library only; deterministic —
the same bytes on every run.
"""

import os

ENTRY_TEXT = (
    "The kettle has gone quiet. Steam rises in one slow thread from the "
    "spout, and the kitchen window holds the last of the afternoon light. "
    "Nothing needs doing. The tea is still warm."
)


def main() -> None:
    # The brief allows 1-280 characters; fail loudly rather than emit an
    # invalid entry if the text is ever edited past the limit.
    if not 1 <= len(ENTRY_TEXT) <= 280 or not ENTRY_TEXT.strip():
        raise ValueError("entry text must be 1-280 non-whitespace characters")
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
