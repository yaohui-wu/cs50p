LIGHT_SPEED = 300_000_000


def main() -> None:
    mass = int(input("m: "))
    energy = mass * LIGHT_SPEED**2
    print(f"E: {energy}")


if __name__ == "__main__":
    main()
