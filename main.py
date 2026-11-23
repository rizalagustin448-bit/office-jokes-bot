"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one office joke to /output/entry.txt.
"""

import os

JOKE = "I've been on mute so long my own thoughts started raising their hand before speaking."


def main() -> None:
    if not 1 <= len(JOKE) <= 199 or not JOKE.strip():
        raise ValueError(f"joke must be 1-199 non-blank chars, got {len(JOKE)}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
