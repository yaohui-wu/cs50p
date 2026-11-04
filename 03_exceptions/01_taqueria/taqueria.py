PRICES = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    print_total(PRICES)


def print_total(prices: dict[str, float]) -> None:
    total = 0

    while True:
        try:
            item = input("Item: ").lower().title()

            if item in prices:
                price = prices[item]
                total += price
                print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            return


if __name__ == "__main__":
    main()
