balance = 1000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        print(" Current Balance:", balance)
    elif ch == "2":
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print(" Deposited! New Balance:", balance)
    elif ch == "3":
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print(" Withdrawn! Remaining Balance:", balance)
        else:
            print(" Insufficient balance.")
    elif ch == "4":
        print("Thank you for using ATM!")
        break
    else:
        print(" Invalid choice, try again.")
