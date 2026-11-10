"""
Task 2 – Greeting Function

Write greet_user(name) to clean up a name and return a greeting.
Remove leading and trailing spaces and capitalize the name.
If the name is empty, use "Stranger".

Examples:
>>> greet_user("alice")
'Hello, Alice! Welcome to Python!'
>>> greet_user("   bob  ")
'Hello, Bob! Welcome to Python!'
>>> greet_user("anna MARIE")
'Hello, Anna marie! Welcome to Python!'
>>> greet_user("   ")
'Hello, Stranger! Welcome to Python!'
"""


def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    name = name.strip().capitalize()

    if not name:
        name = "Stranger"

    return f"Hello, {name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
