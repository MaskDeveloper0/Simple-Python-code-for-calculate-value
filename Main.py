# 🔥 Pro Calculator v2

import math
import os

history = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Enter a valid number!")


def save_history():
    with open("history.txt", "a") as f:
        for item in history:
            f.write(item + "\n")


def show_history():
    if not history:
        print("📭 No history yet.")
    else:
        print("\n📜 History:")
        for item in history:
            print(item)


def calculator():
    result = None

    while True:
        print("\n=== 🧮 Calculator ===")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (x^y)")
        print("6. Modulus (%)")
        print("7. Floor Division (//)")
        print("8. Square Root (√)")
        print("9. Expression (e.g. 5+3*2)")
        print("10. History")
        print("11. Clear Screen")
        print("12. Back to Main Menu")

        choice = input("Choose: ")

        if choice == "12":
            break

        if choice == "10":
            show_history()
            continue

        if choice == "11":
            clear_screen()
            continue

        # Expression Mode
        if choice == "9":
            expr = input("Enter expression: ")
            try:
                result = eval(expr)
                print("✅ Result:", result)
                history.append(f"{expr} = {result}")
            except:
                print("❌ Invalid expression")
            continue

        # Square Root
        if choice == "8":
            num = get_number("Enter number: ")
            if num >= 0:
                result = math.sqrt(num)
                print("✅ Result:", result)
                history.append(f"√{num} = {result}")
            else:
                print("❌ Cannot sqrt negative number")
            continue

        # Normal operations
        if result is None:
            num1 = get_number("Enter first number: ")
        else:
            use_prev = input(f"Use previous result ({result})? (y/n): ")
            num1 = result if use_prev.lower() == 'y' else get_number("Enter first number: ")

        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            op = "+"

        elif choice == "2":
            result = num1 - num2
            op = "-"

        elif choice == "3":
            result = num1 * num2
            op = "*"

        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                op = "/"
            else:
                print("❌ Cannot divide by zero")
                continue

        elif choice == "5":
            result = num1 ** num2
            op = "^"

        elif choice == "6":
            result = num1 % num2
            op = "%"

        elif choice == "7":
            result = num1 // num2
            op = "//"

        else:
            print("❌ Invalid choice")
            continue

        print("✅ Result:", result)
        history.append(f"{num1} {op} {num2} = {result}")


def unit_converter():
    while True:
        print("\n=== 🔄 Unit Converter ===")
        print("1. Length (m ↔ km)")
        print("2. Temperature (C ↔ F)")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "3":
            break

        if choice == "1":
            val = get_number("Enter meters: ")
            print(f"{val} m = {val/1000} km")

        elif choice == "2":
            val = get_number("Enter Celsius: ")
            print(f"{val}°C = {(val * 9/5) + 32}°F")

        else:
            print("❌ Invalid choice")


# MAIN MENU
while True:
    print("\n=== 🔥 MAIN MENU ===")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Save History")
    print("4. Exit")

    main_choice = input("Choose: ")

    if main_choice == "1":
        calculator()

    elif main_choice == "2":
        unit_converter()

    elif main_choice == "3":
        save_history()
        print("💾 History saved to file!")

    elif main_choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice")