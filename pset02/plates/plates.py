def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length < 2 or length > 6:
        return False
    # Starts with at least two letters.
    valid_start = s[0].isalpha() and s[1].isalpha()
    if not valid_start:
        return False
    is_first_num = True
    for c in s[2:]:
        # Only letters or numbers.
        if not c.isalnum():
            return False
        # First nubmer cannot be 0.
        if c.isdigit() and is_first_num:
            if c == "0":
                return False
            else:
                is_first_num = False
        # Numbers cannot be used in the middle.
        if not is_first_num and c.isalpha():
            return False
    return True


if __name__ == "__main__":
    main()
