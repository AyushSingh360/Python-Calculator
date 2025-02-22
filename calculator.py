def calculator():
    print("Welcome to your Python Calculator!")
    print("Select an operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if operation == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Oops! Division by zero is undefined.")
    else:
        print("Invalid input. Please choose a number between 1 and 4.")

calculator()
