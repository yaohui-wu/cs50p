def main() -> None:
    input_message = input("Enter message: ")
    output_message = input_message.replace(":)", "🙂").replace(":(", "🙁")
    print(output_message)


if __name__ == "__main__":
    main()
