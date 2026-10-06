def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount -= coin
    change = 0
    if amount < 0:
        change = 0 - amount
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
