# Simple calculator program

def main():
    print("Welcome to the simple calculator!")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Error: Invalid operation.")
            return
        
        # Print the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()