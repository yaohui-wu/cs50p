VOWELS = "AEIOUaeiou"


def main() -> None:
    word = input("Input: ")
    short_word = shorten(word)
    print(f"Output: {short_word}")


def shorten(word: str) -> str:
    chars = []

    for c in word:
        if c not in VOWELS:
            chars.append(c)

    short_word = "".join(chars)
    return short_word


if __name__ == "__main__":
    main()
