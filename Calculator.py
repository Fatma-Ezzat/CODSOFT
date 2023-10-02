def calculator():
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    
    operation = input("Enter the number of operation you want (1-4): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if operation == "1":
        result = num1 + num2
        operator = "+"
    elif operation == "2":
        result = num1 - num2
        operator = "-"
    elif operation == "3":
        result = num1 * num2
        operator = "*"
    elif operation == "4":
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = "/"
    else:
        print("Invalid choice, Please try again.")
        return

    print(f"\nResult: {num1} {operator} {num2} = {result}")


calculator()