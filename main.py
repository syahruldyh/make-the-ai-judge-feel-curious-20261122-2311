"""Entry for make.fun bounty make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt — a text written to leave the
AI judge curious: alert, drawn in, wanting more.
"""

ENTRY_TEXT = (
    "My grandmother kept one drawer locked her whole life. "
    "When she died, we found the key taped under the kitchen table. "
    "In her handwriting: 'not yet.' "
    "The drawer is still locked. "
    "The key is in my pocket."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
