def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = input("Insert Coin: ")
        coins = ("25", "10", "5")
        if coin in coins:
            amount -= int(coin)
    change = 0
    if amount < 0:
        change = 0 - amount
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
