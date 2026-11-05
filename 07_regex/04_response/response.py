"""
CS50P Problem Set 7: Response Validation

Checks whether an email address is syntatically valid.
"""

import validators


def main() -> None:
    email = input("What's your email address? ")
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email: str) -> validators.ValidationError | bool:
    return validators.email(email)


if __name__ == "__main__":
    main()
