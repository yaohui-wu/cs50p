"""
CS50P Problem Set 7: Response Validation

Checks whether an email address is syntatically valid.
"""

import validators


def main():
    email = input("What's your email address? ")
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    return validators.email(email)


if __name__ == "__main__":
    main()
