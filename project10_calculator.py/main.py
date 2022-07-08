def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))


def calculate(n1, n2, symbol):

    return operations[symbol](n1, n2)


answer = calculate(num1, num2, operation_symbol)

print(f"{num1} {operation_symbol} {num2} = {answer}")
