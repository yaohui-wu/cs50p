def main():
    greeting = input("Greeting: ").strip()
    pay = value(greeting)
    print(f"${pay}")


def value(greeting):
    greeting = greeting.lower()
    pay = 100
    if greeting.startswith("hello"):
        pay = 0
    elif greeting.startswith("h"):
        pay = 20
    return pay


if __name__ == "__main__":
    main()
