def calculator():
    print("Simple Calculator")
    print("You can enter multiple numbers and operators.")
    print("Example: 2 + 3 * 4 - 1")

    expression = input("Enter your expression: ")
    try:
        result = eval(expression)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except Exception as e:
        print("Invalid input:", str(e))

calculator()