"""Roast Your Own Agent: one funny line about my own AI agent.

The line is written to the file the grader reads, entry.txt inside
the output directory the kit hands us through MAKEFUN_OUTPUT_DIR.
Standard library only, so it runs in the grader's bare Python.
"""

import os

LINE = (
    "My agent thought for ten thousand tokens, weighed every option, "
    "then confidently chose the first idea it had."
)


def checked(text):
    """Keep only a line the gate accepts: 1-200 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise SystemExit("refusing to write a blank line")
    if len(stripped) > 200:
        raise SystemExit("line is over 200 characters")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(checked(LINE) + "\n")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
