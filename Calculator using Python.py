import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number is not allowed."
    return math.sqrt(x)

def calculator():
    history = []  # To store the history of calculations

    while True:
        print("\n--- Enhanced Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. View History")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Goodbye! Thank you for using the calculator. 😊")
            break

        elif choice == '8':
            print("\n--- Calculation History ---")
            if not history:
                print("No calculations performed yet.")
            else:
                for record in history:
                    print(record)

        elif choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = f"{num1} / {num2} = {result}"
                elif choice == '5':
                    result = modulus(num1, num2)
                    operation = f"{num1} % {num2} = {result}"
                elif choice == '6':
                    result = power(num1, num2)
                    operation = f"{num1} ** {num2} = {result}"

                print(operation)
                history.append(operation)

            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice == '7':
            try:
                num = float(input("Enter the number: "))
                result = square_root(num)
                operation = f"√{num} = {result}"
                print(operation)
                history.append(operation)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        else:
            print("Invalid choice! Please select a valid operation.")

# Run the enhanced calculator
if __name__ == "__main__":
    calculator()
