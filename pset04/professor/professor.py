import random


def main():
    level = get_level()
    nums1 = []
    nums2 = []
    for _ in range(10):
        num1 = generate_integer(level)
        nums1.append(num1)
        num2 = generate_integer(level)
        nums2.append(num2)
    score = 0
    for i in range(10):
        num1 = nums1[i]
        num2 = nums2[i]
        problem = f"{num1} + {num2} = "
        answer = num1 + num2
        tries = 0
        while tries < 3:
            try:
                attempt = int(input(problem))
                if attempt == answer:
                    score += 1
                    break
            except ValueError:
                pass
            print("EEE")
            tries += 1
        if tries == 3:
            print(f"{problem}{answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if 1 <= level <= 3:
            return level


def generate_integer(level):
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
