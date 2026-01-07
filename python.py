import json
import os

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")

def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']}: ${exp['amount']}")
        total += exp['amount']
    print(f"Total spent: ${total}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Show expenses")
        print("2. Add expense")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            show_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
