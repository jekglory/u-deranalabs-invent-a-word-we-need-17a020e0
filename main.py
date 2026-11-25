"""u-deranalabs-invent-a-word-we-need-17a020e0 entry: "scrollblank".

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The entry is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

The word names a moment with no name yet: the blank that follows a long
scroll, when you surface and cannot recall a single thing you just saw.
"Doomscrolling" names the act; "scrollblank" names the empty aftermath.
It is a transparent compound, scroll + blank, so it is sayable on first
sight, spellable on first hearing, and memorable because the feeling is
one almost everyone with a phone already knows.
"""

import os


ENTRY = (
    "scrollblank (n.): the empty feeling after scrolling for twenty "
    "minutes and remembering nothing you just saw."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The competition requires the word and its one-line definition in a
# single line of at most 140 characters.
MAX_CHARS = 140


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if "  " in text:
        raise SystemExit("entry must not contain double spaces")
    word = text.split(" ", 1)[0]
    if not word.isalpha() or not word.islower():
        raise SystemExit("entry must open with one lowercase word")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the entry.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the entry")
    print(text)


if __name__ == "__main__":
    main()
