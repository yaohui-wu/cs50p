def main():
    camel = input("camelCase: ")
    snake = snake_case(camel)
    print(f"snake_case: {snake}")


def snake_case(camel):
    chars = []
    for c in camel:
        if c.isupper():
            chars.append("_")
            c = c.lower()
        chars.append(c)
    snake = "".join(chars)
    return snake


if __name__ == "__main__":
    main()
