def greet(name):
    name = name.strip() or "Git"
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = input("Your name: ")
    print(greet(name))
