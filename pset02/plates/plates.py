def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #TODO
    length = len(s)
    valid_length = 2 <= length <= 6
    if not valid_length:
        return False
    # Starts with at least two letters.
    valid_start = s[0].isalpha() and s[1].isalpha()
    # Ends with a number.
    valid_end = s[-1].isnumeric()
    if not valid_start or not valid_end:
        return False
    for c in s[2:]:
        # Only letters or numbers.
        if not c.isalnum():
            return False
        # First nubmer cannot be 0.
        if c.isnumeric() and int(c) == 0:
            return False
    return True


if __name__ == "__main__":
    main()
