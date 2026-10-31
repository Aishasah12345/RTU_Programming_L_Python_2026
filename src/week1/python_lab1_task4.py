def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    return sum(1 for char in text if not char.isspace())


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    numbers = []

    for word in text.split():
        cleaned = word.rstrip(".,!?;:")

        if cleaned.startswith("-"):
            digits = cleaned[1:]
            if digits and digits.isdigit():
                numbers.append(int(cleaned))
        elif cleaned.isdigit():
            numbers.append(int(cleaned))

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    characters = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0.0

    return {
        "characters": characters,
        "words": words,
        "numbers": numbers,
        "sum": total,
        "average": average,
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_text(text)

    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
