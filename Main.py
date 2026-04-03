# Improved Calculator in Python

def get_number(prompt):
    """Safely get a number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")


def calculator():
    print("\n=== Simple Calculator ===")

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("✅ Result:", num1 + num2)

    elif choice == "2":
        print("✅ Result:", num1 - num2)

    elif choice == "3":
        print("✅ Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("✅ Result:", num1 / num2)
        else:
            print("❌ Error: Cannot divide by zero")

    else:
        print("❌ Invalid choice")


# Main loop
while True:
    calculator()

    print("\nOptions:")
    print("1. Continue")
    print("2. Exit")

    option = input("Choose option: ")

    if option == "1":
        continue
    elif option == "2":
        print("Calculator Closed 👋")
        break
    else:
        print("Invalid option, exiting...")
        break