import random

LEVEL_RANGES = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
NUM_QUESTIONS = 10
MAX_ATTEMPTS = 3


def main() -> None:
    level = get_level()
    score = 0

    for _ in range(NUM_QUESTIONS):
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        is_correct = ask_question(first_num, second_num)

        if is_correct:
            score += 1

    print(f"Score: {score}")


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: ").strip())
        except ValueError:
            continue
        if 1 <= level <= MAX_ATTEMPTS:
            return level


def generate_integer(level: int) -> int:
    if level not in LEVEL_RANGES:
        raise ValueError
    lower, upper = LEVEL_RANGES[level]
    num = random.randint(lower, upper)
    return num


def ask_question(first_num: int, second_num: int) -> bool:
    question = f"{first_num} + {second_num} = "
    correct_answer = first_num + second_num
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            user_answer = int(input(question))
        except ValueError:
            user_answer = None

        if user_answer == correct_answer:
            return True
        print("EEE")
        attempts += 1

    print(f"{question}{correct_answer}")
    return False


if __name__ == "__main__":
    main()
