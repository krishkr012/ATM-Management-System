pin = "1234"
balance = 5000
mini_statement = []

def authenticate():
    print("Demo PIN: 1234")
    entered_pin = input("Enter Your PIN: ")

    if entered_pin == pin:
        print("Login Successful\n")
        return True
    else:
        print("Incorrect PIN")
        return False

def atm_system():
    global balance, pin, mini_statement

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")
        print("==============================")

        choice = input("Enter Your Choice: ")

        # Check Balance
        if choice == "1":
            print(f"Current Balance: ₹{balance}")
            mini_statement.append(f"Checked Balance: ₹{balance}")

        # Deposit Money
        elif choice == "2":
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount > 0:
                balance += amount
                print(f"₹{amount} Deposited Successfully")
                print(f"Updated Balance: ₹{balance}")
                mini_statement.append(f"Deposited: ₹{amount}")
            else:
                print("Invalid Amount")

        # Withdraw Money
        elif choice == "3":
            amount = float(input("Enter Withdraw Amount: ₹"))

            if amount <= balance:
                if amount > 0:
                    balance -= amount
                    print(f"₹{amount} Withdrawn Successfully")
                    print(f"Remaining Balance: ₹{balance}")
                    mini_statement.append(f"Withdrawn: ₹{amount}")
                else:
                    print("Invalid Amount")
            else:
                print("Insufficient Balance")

        # Change PIN
        elif choice == "4":
            old_pin = input("Enter Old PIN: ")

            if old_pin == pin:
                new_pin = input("Enter New PIN: ")
                confirm_pin = input("Confirm New PIN: ")

                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN Changed Successfully")
                    mini_statement.append("PIN Changed")
                else:
                    print("PIN Mismatch")
            else:
                print("Wrong Old PIN")

        # Mini Statement
        elif choice == "5":
            print("\n------ MINI STATEMENT ------")

            if len(mini_statement) == 0:
                print("No Transactions Yet")
            else:
                for transaction in mini_statement:
                    print("->", transaction)

        # Exit
        elif choice == "6":
            print("Thank You For Using ATM")
            print("Exiting System...")
            break

        # Invalid Choice
        else:
            print("Invalid Choice")


# Program Start
if authenticate():
    atm_system()
else:
    print("Access Denied")