import emoji


def main():
    text = input("Input: ")
    output_emoji = emoji.emojize(text, language="alias")
    print(f"Output: {output_emoji}")


if __name__ == "__main__":
    main()
