"""One-Line Office Jokes entry for make.fun.

Writes a single one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The joke turns on a real detail of office life -- the printer that
only jams at the worst possible moment -- and lands its laugh in the
last few words, when the printer is revealed to be a predator that
can smell fear. No network, no file reads, no secrets: the text is
embedded verbatim below.
"""

import os

# The entry, exactly as submitted (87 characters, one line).
ENTRY = "The office printer only jams when my deadline is five minutes away \u2014 it can smell fear."


def main():
    """Write ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
