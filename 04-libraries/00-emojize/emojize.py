from emoji import emojize


def main() -> None:
    text = input("Input: ").strip()
    emoji = emojize(text, language="alias")
    print(f"Output: {emoji}")


if __name__ == "__main__":
    main()
