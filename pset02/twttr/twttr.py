def main():
    text = input("Input: ")
    vowels = "aeiou"
    chars = []
    for c in text:
        if c.lower() not in vowels:
            chars.append(c)
    output = "".join(chars)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
