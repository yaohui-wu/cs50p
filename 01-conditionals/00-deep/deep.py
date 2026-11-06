def main() -> None:
    answer = input(
        "What is the Answer to the Great Question of Life, "
        "the Universe, and Everything?"
    )
    if is_answer(answer):
        print("Yes")
    else:
        print("No")


def is_answer(answer: str) -> bool:
    answer = answer.strip().lower()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return True
    return False


if __name__ == "__main__":
    main()
