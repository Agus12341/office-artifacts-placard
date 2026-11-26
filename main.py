"""Museum placard for the paper clip, an ordinary office object."""

import os

TEXT = (
    "Paper Clip, c. 2500 BCE. Bent bronze. A humble clasp once "
    "believed to hold the empire together. It did not. "
    "Gift of the Department of Paperwork."
)


def write_entry(path, text):
    """Write the placard text, refusing anything outside the 180-char gate."""
    if not (1 <= len(text) <= 180) or not text.strip():
        raise ValueError("entry text fails the 1-180 character gate")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry("/output/entry.txt", TEXT)


if __name__ == "__main__":
    main()
