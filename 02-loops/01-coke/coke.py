COINS = {"25", "10", "5"}


def main() -> None:
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = input("Insert Coin: ").strip()
        if coin in COINS:
            amount_due -= int(coin)

    change = abs(amount_due)
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
