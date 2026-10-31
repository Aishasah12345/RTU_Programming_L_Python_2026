
def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    name = name.strip().capitalize()

    if not name:
        name = "Stranger"

    return f"Hello, {name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
