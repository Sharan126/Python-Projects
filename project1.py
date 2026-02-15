# Expense Tracker Project
#updated Version
expenses = []  # list of all expenses in dictionary form
print("Welcome to the Expense Tracker! Save your expenses easily")

while True:
    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category (e.g., Food, Transport, etc.): ")
        description = input("Enter a brief description: ")

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\nAll Expenses:")
            count = 1
            for e in expenses:
                print(f"Expense {count} -> Date: {e['date']}, Category: {e['category']}, Description: {e['description']}, Amount: {e['amount']}")
                count += 1

    # 3. VIEW TOTAL EXPENSE
    elif choice == 3:
        total = 0
        for each in expenses:
            total += each["amount"]
        print("\nTOTAL EXPENSE =", total)

    # 4. EXIT
    elif choice == 4:
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
