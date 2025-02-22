import math

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")

def calculator():
    print("Welcome to Your Advanced Python Calculator!")

    while True:
        print("\nSelect an operation:")
        print("1 - Addition (+)")
        print("2 - Subtraction (-)")
        print("3 - Multiplication (*)")
        print("4 - Division (/)")
        print("5 - Exponentiation (^)")
        print("6 - Square Root (√)")
        print("7 - Logarithm (log)")
        print("8 - Exit")

        operation = input("Enter your choice (1-8): ")

        if operation == '8':
            print("Goodbye!")
            break
        elif operation in ['1', '2', '3', '4', '5']:
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")

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
                    print("Hold on! Can't divide by zero.")
            elif operation == '5':
                result = num1 ** num2
                print(f"{num1} ^ {num2} = {result}")
        elif operation == '6':
            num = get_number("Enter the number: ")
            if num >= 0:
                result = math.sqrt(num)
                print(f"√{num} = {result}")
            else:
                print("Square root of a negative number isn't real.")
        elif operation == '7':
            num = get_number("Enter the number: ")
            base = get_number("Enter the base (default is e): ") or math.e
            if num > 0 and base > 0 and base != 1:
                result = math.log(num, base)
                print(f"log base {base} of {num} = {result}")
            else:
                print("Invalid input for logarithm.")
        else:
            print("Invalid choice. Please select a valid option.")

calculator()
