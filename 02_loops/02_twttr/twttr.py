def main():
    text = input("Input: ")
    vowels = "aeiouAEIOU"
    chars = []
    for c in text:
        if c not in vowels:
            chars.append(c)
    output = "".join(chars)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
