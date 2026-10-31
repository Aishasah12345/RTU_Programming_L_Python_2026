def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
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
