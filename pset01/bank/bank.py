def main():
    greeting = input("Greeting: ")
    pay = determine_pay(greeting)
    print(pay)


def determine_pay(greeting):
    pay = "$100"
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        pay = "$0"
    elif greeting.startswith("h"):
        pay = "$20"
    return pay


if __name__ == "__main__":
    main()
