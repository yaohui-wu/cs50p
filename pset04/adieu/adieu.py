def main():
    # TODO
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    print("Adieu, adieu, to")


if __name__ == "__main__":
    main()
