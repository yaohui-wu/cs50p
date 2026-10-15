import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if 1 <= level <= 3:
            return level


def generate_integer(level):
    # TODO
    if level not in (1, 2, 3):
        raise ValueError
    num = 0
    if level == 1:
        num = random.randint(1, 9)
    elif level == 2:
        num = random.randint(10, 99)
    elif level == 3:
        num = random.randint(100, 999)
    return num


if __name__ == "__main__":
    main()
