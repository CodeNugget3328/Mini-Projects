def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_input():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        return x, y
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None, None

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        x, y = get_input()
        if x is None or y is None:
            return  # Exit if there was an error in input
        
        if choice == '1':
            print(f"{x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"{x} - {y} = {subtract(x, y)}")
        elif choice == '3':
            print(f"{x} * {y} = {multiply(x, y)}")
        elif choice == '4':
            result = divide(x, y)
            if isinstance(result, str):  # Check if the result is an error message
                print(result)
            else:
                print(f"{x} / {y} = {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
