# Simple Calculator Program
def main():
    # Example numbers
    num1 = 10
    num2 = 5
    operation = "+"  # You can change this to "-", "*", or "/"

    # Perform the operation based on the pre-defined values
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
        print("Invalid operation.")
        return

    # Display the result
    print(f"The result of {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
