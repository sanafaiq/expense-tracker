import os

FILE_NAME = "expenses.txt"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

def add_expense():
    item = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(item + "," + amount + "\n")

    print("Expense added successfully!")

def view_expenses():
    print("\nAll Expenses:")
    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            if "," in line:
                item, amount = line.strip().split(",")
                if amount != "":
                    print(item, "-", amount)
                    total += float(amount)

    print("\nTotal Expense:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")