import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operation = {
    "+": add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)
    should_continue = True
    num_1 = float(input("Type the first number\n"))
    while should_continue:
        for symbol in operation:
            print(symbol)
        operator = input("Pick the operation  ")
        num_2 = float(input("Enter the next number\n"))
        ans = (operation[operator](num_1, num_2))
        print(ans)
        proceed = input(f"Do you want to continue operation on {ans} ? 'y' or 'n' ").lower()
        if proceed == 'y':
            num_1 = ans
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()