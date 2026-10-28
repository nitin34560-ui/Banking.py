import os

FILENAME = "bank.txt"

def load_accounts():
    """Load account data from bank.txt into a dictionary."""
    accounts = {}
    if not os.path.exists(FILENAME):
        return accounts
    
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    acc_no = int(parts[0])
                    balance = float(parts[1])
                    accounts[acc_no] = balance
    except Exception as e:
        print(f"Error loading data: {e}")
    return accounts

def save_accounts(accounts):
    """Save account data from the dictionary into bank.txt."""
    try:
        with open(FILENAME, "w") as file:
            for acc_no, balance in accounts.items():
                file.write(f"{acc_no},{balance}\n")
    except Exception as e:
        print(f"Error saving data: {e}")

def create_account(accounts):
    """Create a new account with a unique account number starting from 1001."""
    name = input("Name: ").strip()
    
    # Validate opening deposit
    while True:
        try:
            deposit = float(input("Opening deposit: "))
            if deposit < 500:
                print("Initial deposit must be at least Rs.500 to meet the minimum balance rule.")
                continue
            break
        except ValueError:
            print("Invalid value. Enter a numeric amount.")

    # Determine unique account number
    if len(accounts) == 0:
        acc_no = 1001
    else:
        acc_no = max(accounts.keys()) + 1

    accounts[acc_no] = deposit
    save_accounts(accounts)
    print(f"Account created. A/C No: {acc_no} | Balance: {int(deposit) if deposit.is_integer() else deposit}")

def deposit_money(accounts):
    """Deposit money into an existing account."""
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in accounts:
            print(f"Account {acc_no} not found.")
            return

        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        accounts[acc_no] += amount
        save_accounts(accounts)
        print(f"Deposit successful. Balance: {accounts[acc_no]}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

def withdraw_money(accounts):
    """Withdraw money while enforcing the minimum balance rule (Rs.500)."""
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in accounts:
            print(f"Account {acc_no} not found.")
            return

        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        # Check minimum balance constraint
        if accounts[acc_no] - amount < 500:
            print("Withdrawal failed. Minimum balance of Rs.500 must always remain.")
            return

        accounts[acc_no] -= amount
        save_accounts(accounts)
        print(f"Withdrawal successful. Balance: {accounts[acc_no]}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

def transfer_money(accounts):
    """Transfer money from one account to another."""
    try:
        from_acc = int(input("Enter Sender Account Number: "))
        if from_acc not in accounts:
            print(f"Account {from_acc} not found. Transfer cancelled.")
            return

        to_acc = int(input("Enter Receiver Account Number: "))
        if to_acc not in accounts:
            print(f"Account {to_acc} not found. Transfer cancelled.")
            return

        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return

        # Check minimum balance for sender
        if accounts[from_acc] - amount < 500:
            print("Transfer failed. Sender account will fall below the minimum balance of Rs.50.")
            return

        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        save_accounts(accounts)
        print("Transfer successful.")
        print(f"Sender balance: {accounts[from_acc]} | Receiver balance: {accounts[to_acc]}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

def balance_enquiry(accounts):
    """Check and display the balance of a specific account."""
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in accounts:
            print(f"Account {acc_no} not found.")
            return
        print(f"Account No: {acc_no} | Balance: {accounts[acc_no]}")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")

def main():
    accounts = load_accounts()
    
    while True:
        print("\n--- Simple Banking System ---")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Balance Enquiry")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_money(accounts)
        elif choice == '3':
            withdraw_money(accounts)
        elif choice == '4':
            transfer_money(accounts)
        elif choice == '5':
            balance_enquiry(accounts)
        elif choice == '6':
            print("Thank you for using the Simple Banking System. Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option from 1 to 6.")

if __name__ == "__main__":
    main()