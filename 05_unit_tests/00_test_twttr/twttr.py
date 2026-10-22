def main():
    word = input("Input: ")
    short_word = shorten(word)
    print(f"Output: {short_word}")


def shorten(word):
    vowels = "aeiouAEIOU"
    chars = []
    for c in word:
        if c not in vowels:
            chars.append(c)
    short_word = "".join(chars)
    return short_word


if __name__ == "__main__":
    main()
