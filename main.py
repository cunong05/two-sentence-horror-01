"""Two-Sentence Horror.

Writes one exactly-two-sentence horror story to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The story is 150 characters, exactly two sentences, no trailing newline.
No dependencies, no network, deterministic: the same text every run.
"""

import os

STORY = (
    "The hospice nurse told me my grandmother squeezes twice for yes "
    "and once for no. I asked her if she was afraid of dying, and she "
    "squeezed three times."
)


def main() -> None:
    # Gate: the entry must be 1-400 characters, not only whitespace,
    # and exactly two sentences; fail loudly here instead of shipping
    # an invalid entry.
    assert 1 <= len(STORY) <= 400, f"story is {len(STORY)} characters, must be 1-400"
    assert STORY.strip(), "story is only whitespace"
    sentence_endings = STORY.count(".")
    assert sentence_endings == 2, (
        f"story has {sentence_endings} sentence-ending periods, must be exactly 2"
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)  # no trailing newline
    print(f"wrote {len(STORY)} characters to {path}")


if __name__ == "__main__":
    main()
