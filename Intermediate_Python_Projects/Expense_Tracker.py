expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        item = input("Enter item name: ")
        cost = float(input("Enter amount: ₹"))
        expenses.append((item, cost))
        print("Expense added successfully!")
    elif ch == "2":
        print("\nYour Expenses:")
        for i, e in enumerate(expenses):
            print(f"{i+1}. {e[0]} - ₹{e[1]}")
    elif ch == "3":
        total = sum(x[1] for x in expenses)
        print("Total Spent: ₹", total)
    elif ch == "4":
        print("Gud Byee")
        break
    else:
        print("Invalid choice, please try again.")
