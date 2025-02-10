def calculator():
    print("Welcome to the Calculator!")
    
    # Get the first number from the user
    try:
        num1 = float(input("Please enter the first number: "))
    except ValueError:
        print("Oops! That doesn't seem to be a valid number. Please try again.")
        return
    
    # Get the second number from the user
    try:
        num2 = float(input("Now, please enter the second number: "))
    except ValueError:
        print("Oops! That doesn't seem to be a valid number. Please try again.")
        return
    
    # Display the available operations
    print("Great! Now, choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Get the user's choice of operation
    operation = input("Please enter the number corresponding to your choice (1/2/3/4): ")
    
    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: You can't divide by zero! Please try again.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Oops! That choice isn't valid. Please select a number from 1 to 4.")
    
# Run the calculator if this script is executed
if __name__ == "__main__":
    calculator()