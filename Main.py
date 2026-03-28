# Basic Calculator in Python 


#For user who use a older version of windows , for example win 7 users , in your windows this ai assistant can not show a emojies.
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect operation:(Give in 1 or 2 or 3 or 4")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid choice")


# main program for a refreshable calculator option 

while True:
    calculator()

    print("\n1. Restart / Refresh Calculator")
    print("2. Exit")

    option = input("Choose option: ")

    if option == "1":
        print("\nRestarting Calculator...\n")
        continue
    else:
        print("Calculator Closed 👋")
        break

        #End
