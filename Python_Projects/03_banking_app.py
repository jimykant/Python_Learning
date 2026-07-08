"""
==========================================================
Simple Banking System Project
==========================================================
Description:
    - A menu-driven banking system.
    - Allows users to check balance, deposit money,
      withdraw money, and manage KYC documents.
"""
balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your current balance is: {balance}")
    print("==================================")

def get_amount(message):
    while True:
        try:
            amount = float(input(message))
            return amount
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            print("===================================")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Amount deposited successfully")
        print(f"Your current balance is: {balance}")
        print("===================================")
    else:
        print("can not deposit negative or zero(0) amount")
        print("===================================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("can not withdraw negative or zero(0) amount")
        print("===================================")
    elif amount > balance:
        print("Can not withdraw. Insufficient balance")
        print(f"Your current balance is: {balance}")
        print("===================================")
    else:
        balance -= amount
        print(f"Amount withdrawn successfully")
        print(f"Your current balance is: {balance}")
        print("===================================")

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done yet")
        print("==============================")
    else:
        for key, value in kyc_documents.items():
            print(f"{key}: {value}")
        print("==============================")

def update_kyc():
    global kyc_documents
    while True:
        try:
            n_documents = int(input("Enter the number of documents you want to add: "))
            if n_documents <= 0:
                print("Number of documents must be greater than 0")
                print("==================================")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            print("==================================")
    print()
    for i in range(n_documents):
        print(f"Document {i + 1}")
        key = input("Enter the document name: ")
        value = input("Enter the document number: ")
        print()
        kyc_documents[key] = value
    print("KYC has been updated successfully!")
    print("==================================")

if __name__ == "__main__":
    print("==============================")
    print("Welcome to ABC Bank!!!")
    print("==============================")
    while True:
        print("1. Check Your Balance")
        print("2. Deposit an Amount")
        print("3. Withdraw an Amount")
        print("4. Check KYC Status")
        print("5. Update your KYC")
        print("6. Quit")
        print("==============================")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_amount = get_amount("Enter the amount you want to deposit:\n")
            deposit(deposit_amount)
        elif choice == "3":
            withdraw_amount = get_amount("Enter the amount you want to withdraw:\n")
            withdraw(withdraw_amount)
        elif choice == "4":
            check_kyc()
        elif choice == "5":
            update_kyc()
        elif choice == "6":
            print("Exiting Program")
            break
        else:
            print("Invalid Input!!! Try again.")
            print("==============================")
    print("==============================")
    print("Thank You For Banking With Us!")
