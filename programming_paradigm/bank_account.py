class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds are available."""
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
