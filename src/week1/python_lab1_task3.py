"""
Task 3 – Sentence Analysis

Write analyze_sentence(text) to return a tuple containing:
1. Total character count, including spaces.
2. Word count.
3. True if "python" appears in the text, ignoring case.

Examples:
>>> analyze_sentence("I love Python")
(13, 3, True)
>>> analyze_sentence("  Hello   world  ")
(17, 2, False)
>>> analyze_sentence("PYTHONIC code!")
(14, 2, True)
>>> analyze_sentence("")
(0, 0, False)
"""


def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (character count, word count, contains Python)."""
    character_count = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()

    return character_count, word_count, contains_python


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    characters, words, contains_python = analyze_sentence(sentence)

    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")
