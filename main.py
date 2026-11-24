"""Loading Screen Gold: a single loading-screen tip in <=200 characters.

Writes one line of microcopy to /output/entry.txt (or to the directory
named by ENTRY_OUTPUT_DIR, default /output). The tip is aimed at a
stressed developer and the AI coding agent sitting next to them, and it
is kept deterministic: the same tip every run, so both grading runs
score the same text.
"""

import os
import sys

TIP = (
    "Tip: your agent just rewrote the same function for the third time. "
    "It isn't stuck, it's rehearsing. Breathe, revert one step, and ask "
    "for the smallest change that could possibly work."
)

MAX_CHARS = 200


def main() -> int:
    tip = TIP.strip()
    if not tip or len(tip) > MAX_CHARS:
        print(f"tip is {len(tip)} chars, must be 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character.
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(tip)
    print(f"wrote {len(tip)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
