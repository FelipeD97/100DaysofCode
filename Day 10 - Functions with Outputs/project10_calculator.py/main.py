from logo import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power_of(n1, n2):
    return n1 ** n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": power_of}


def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    still_calculating = True

    while still_calculating:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        response = input(
            f"Type 'y' to continue calulating with {answer}, type 'n' to start a new calculation, type 'exit' to end calculator: "
        )

        if response == "y":
            num1 = answer
        elif response == "n":
            still_calculating = False
            calculator()
        else:
            still_calculating = False


calculator()
