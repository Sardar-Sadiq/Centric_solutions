import json
import os
from datetime import datetime

class Expense:
    """Represents a single expense item."""
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class ExpenseTracker:
    """Manages a collection of expenses with file persistence."""
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_data()

    def load_data(self):
        """Loads expenses from a JSON file with error handling."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return []

    def save_data(self):
        """Saves current expenses to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.expenses, file, indent=4)
        except IOError as e:
            print(f"Failed to save data: {e}")

    def add_expense(self, amount, category, description):
        """Creates and adds a new expense."""
        try:
            amount = float(amount)
            new_expense = Expense(amount, category, description)
            self.expenses.append(new_expense.to_dict())
            self.save_data()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def view_summary(self):
        """Prints a summary of all expenses and total spent."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        total = 0
        print("\n--- Expense Summary ---")
        for idx, item in enumerate(self.expenses, 1):
            print(f"{idx}. [{item['date']}] {item['category']}: {item['amount']:.2f}/- - {item['description']}")
            total += item['amount']
        print(f"-----------------------")
        print(f"Total Spent: {total:.2f}/- \n")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amt = input("Enter amount: ")
            cat = input("Enter category (e.g., Food, Transport): ")
            desc = input("Enter description: ")
            tracker.add_expense(amt, cat, desc)
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()