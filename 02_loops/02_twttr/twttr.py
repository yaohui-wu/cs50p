VOWELS = "AEIOUaeiou"


def main() -> None:
    text = input("Input: ").strip()
    chars = []

    for c in text:
        if c not in VOWELS:
            chars.append(c)

    text_no_vowels = "".join(chars)
    print(f"Output: {text_no_vowels}")


if __name__ == "__main__":
    main()
