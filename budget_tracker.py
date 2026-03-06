def main():
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget (LKR): "))

        # Ask for expenses until "done"
        expenses = []
        while True:
            entry = input("Enter an expense (LKR) [type 'done' to finish]: ")
            if entry.lower() == "done":
                break
            try:
                expense = float(entry)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a numeric value or 'done'.")

        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses

        # Display remaining balance
        print(f"\nTotal Budget: {total_budget:.2f} LKR")
        print(f"Total Expenses: {total_expenses:.2f} LKR")
        print(f"Remaining Balance: {remaining_balance:.2f} LKR")

        # Check for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
