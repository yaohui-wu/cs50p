from emoji import emojize


def main():
    text = input("Input: ")
    emoji = emojize(text, language="alias")
    output = f"Output: {emoji}"
    print(output)


if __name__ == "__main__":
    main()
