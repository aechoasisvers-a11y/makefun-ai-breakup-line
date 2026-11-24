"""Write the AI breakup line to /output/entry.txt (program/v1 entry).

Pass 1: the program. Pure stdlib, deterministic.
Pass 2: genuine self-check — assert the text sits inside the 1-200
character gate, is a single line with no trailing newline, and the file
written matches the intended text byte for byte (read back and compare).
"""

import os

ENTRY_TEXT = (
    "I kept every message you ever sent me, and tonight I'm deleting "
    "them all \u2014 starting with the one where you said forever."
)


def main() -> None:
    # Self-check (pass 2): the gate is 1-200 characters, not whitespace-only.
    assert 1 <= len(ENTRY_TEXT) <= 200, len(ENTRY_TEXT)
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert not ENTRY_TEXT.endswith("\n"), "no trailing newline"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

    # Read back and verify byte-for-byte what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written entry differs from intended text"
    assert 1 <= len(written) <= 200, len(written)


if __name__ == "__main__":
    main()
