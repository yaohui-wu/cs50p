import inflect


def main():
    # TODO
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    p = inflect.engine()
    joined_names = p.join(names)
    print(f"Adieu, adieu, to {joined_names}")


if __name__ == "__main__":
    main()
