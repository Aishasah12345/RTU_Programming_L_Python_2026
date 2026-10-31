def greet_user(name):
    """Clean up a name and return a greeting."""
    name = name.strip().title()
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
