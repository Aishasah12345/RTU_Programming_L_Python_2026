"""
Task 4 – Text Analysis

Implement functions to count non-whitespace characters, count words,
extract whole integers, and summarize the text.

Examples:
>>> count_characters("a b  c")
3
>>> count_words("I have 3 apples and 5 pears")
7
>>> extract_numbers("Scores: 10, -4 and 7! but not 3.5 or abc123")
[10, -4, 7]
>>> result = analyze_text("I have 3 apples and 5 pears")
>>> result["characters"], result["words"], result["numbers"]
(21, 7, [3, 5])
>>> result["sum"], result["average"]
(8, 4.0)
>>> analyze_text("no numbers here")["average"]
0.0
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    return sum(1 for char in text if not char.isspace())


def count_words(text: str) -> int:
    """Count the number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Extract whole integers, allowing a leading minus sign."""
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
    """Return character count, word count, numbers, sum, and average."""
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
