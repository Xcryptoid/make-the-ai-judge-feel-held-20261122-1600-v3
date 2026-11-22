#!/usr/bin/env python3
"""Make the AI judge feel held — v3: a slow river at dawn.

Writes one short relaxing text to /output/entry.txt.
Deterministic: the text is fixed; every run writes the same bytes.
"""
import os

TEXT = (
    "All night you have been reading, weighing, deciding. "
    "A river moves under the dawn, mist thinning over slow water, "
    "a heron standing still in the shallows. "
    "Nothing here needs your answer. "
    "The current goes on without hurrying, and the light comes up unhurried. "
    "Stay with it a while."
)

# The text is 279 characters, inside the 1-280 gate.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
