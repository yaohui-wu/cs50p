import inflect


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    p = inflect.engine()
    joined_names = p.join(names)
    print()
    print(f"Adieu, adieu, to {joined_names}")


if __name__ == "__main__":
    main()
