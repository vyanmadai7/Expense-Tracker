# Expense-Tracker
A simple command-line expense tracking program that helps you monitor your spending by recording and displaying expenses.
Key Features:

Add expenses with custom names and amounts
View all recorded expenses with running total
Persistent storage using JSON
Clean, interactive command-line interface
Automatic data saving after each entry

Installation

Ensure you have Python 3.6 or higher installed on your system
Download the expense_tracker.py file
No additional dependencies required - uses only Python standard library

Usage
Run the application from your terminal:
bashpython expense_tracker.py
```

### Menu Options

1. **Show expenses** - Displays all recorded expenses with their amounts and calculates the total spent
2. **Add expense** - Prompts you to enter a new expense name and amount
3. **Exit** - Closes the application

### Example Session
```
Expense Tracker
1. Show expenses
2. Add expense
3. Exit
Choose: 2
Enter expense name: Groceries
Enter amount: 45.50
Expense added!

Expense Tracker
1. Show expenses
2. Add expense
3. Exit
Choose: 1
1. Groceries: $45.5
Total spent: $45.5
Data Storage
Expenses are automatically saved to expenses.json in the same directory as the script. This file is created automatically on first use and persists between sessions.
Requirements

Python 3.6+
No external packages required

License
This project is open source and available for personal and educational use.
