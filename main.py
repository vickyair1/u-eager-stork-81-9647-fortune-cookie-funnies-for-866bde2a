#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers: one fortune cookie message aimed
at a software engineer, at most 120 characters.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# V2 REVISION (critique of v1): "fixing a bug that turns out to be a typo"
# wastes words on "turns out to be", and "So is the typo" only half-lands
# the second punch. "Hunting" is the truer engineer verb, and the double
# blame -- "The comment is yours. The typo is also yours." -- makes the
# fortune sting twice, with the funniest word at the end.
LINE = "You will spend three days hunting a bug that is a typo in a comment. The comment is yours. The typo is also yours."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-120 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
