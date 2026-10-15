import random


def main():
    level = 0
    while level <= 0:
        level = int(input("Level: "))
    target = random.randint(1, level)
    print(target)
    guess = 0
    while guess != target:
        guess = int(input("Guess: "))
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
    print("Just right!")


if __name__ == "__main__":
    main()
