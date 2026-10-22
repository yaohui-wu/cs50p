import random


def main():
    level = get_positive_int("Level: ")
    target = random.randint(1, level)
    guess = 0
    while guess != target:
        guess = get_positive_int("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
    print("Just right!")


def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            continue
        if num > 0:
            return num


if __name__ == "__main__":
    main()
