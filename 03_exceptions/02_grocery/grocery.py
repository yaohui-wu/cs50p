def main():
    groceries = get_groceries()
    print_groceries(groceries)


def get_groceries():
    groceries = {}
    while True:
        try:
            item = input()
            item = item.upper()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            print()
            return groceries


def print_groceries(groceries):
    sorted_groceries = sorted(groceries)
    for item in sorted_groceries:
        count = groceries[item]
        print(f"{count} {item}")


if __name__ == "__main__":
    main()
