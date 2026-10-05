def main():
    expression = input("Expression: ")
    num1, operator, num2 = expression.split()
    num1, num2 = float(num1), float(num2)
    result = calculate(operator, num1, num2)
    print(result)


def calculate(operator, num1, num2):
    result = None
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    return result


if __name__ == "__main__":
    main()
