"""One word from grandma.

Writes a single word to /output/entry.txt -- the word a grandma
would text back when you tell her about AI.
"""

import os

WORD = "jeepers"  # the old-fashioned, delighted exclamation she reaches for


def main():
    word = WORD
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert " " not in word and "\n" not in word and "\t" not in word, (
        "word must be a single word"
    )
    assert word == word.strip(), "word must not have surrounding whitespace"
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
