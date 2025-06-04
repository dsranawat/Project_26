class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs{amount:.2f} deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs{amount:.2f} withdrawn.")
        else:
            print("Inssufficient funds or invalid withdrawal amount.")
    def check_balance(self):
        print(f"Current balance: Rs{self.balance:.2f}")

def menu():
    name = input("Enter account holder's name: ")
    account = BankAccount(name)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: Rs"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: Rs"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the system.Thankyou for using our bank system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()