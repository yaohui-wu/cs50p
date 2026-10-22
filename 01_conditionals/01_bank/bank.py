def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip().lower()
    pay = determine_pay(greeting)
    print(pay)


def determine_pay(greeting):
    pay = "$100"
    if greeting.startswith("hello"):
        pay = "$0"
    elif greeting.startswith("h"):
        pay = "$20"
    return pay


if __name__ == "__main__":
    main()
