class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder

        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        self._balance = initial_deposit
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._balance += amount
        self._transactions.append(f"Deposit: +₱{amount:.2f}")
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if self._balance < amount:
            raise ValueError("Insufficient balance.")

        self._balance -= amount
        self._transactions.append(f"Withdrawal: -₱{amount:.2f}")
        return amount

    def get_transaction_history(self):
        return self._transactions.copy()


class ATM:
    def __init__(self, bank_account):
        if not isinstance(bank_account, BankAccount):
            raise TypeError("ATM requires a BankAccount.")

        self._account = bank_account
        self.__pin = "1234"
        self._is_authenticated = False

    def authenticate(self, entered_pin):
        if entered_pin == self.__pin:
            self._is_authenticated = True
            return True

        return False

    def check_balance(self):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return None

        return self._account.balance

    def perform_deposit(self, amount):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return None

        try:
            return self._account.deposit(amount)
        except ValueError as error:
            print(error)
            return None

    def perform_withdrawal(self, amount):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return None

        try:
            return self._account.withdraw(amount)
        except ValueError as error:
            print(error)
            return None

    def print_mini_statement(self):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return

        transactions = self._account.get_transaction_history()

        print("\n--- MINI STATEMENT ---")

        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions[-3:]:
                print(transaction)

        print(f"Current Balance: ₱{self._account.balance:.2f}")


if __name__ == "__main__":
    print("=== BANK ACCOUNT TEST ===")

    account = BankAccount("Jrei", 1000.00)

    print("Account Holder:", account.account_holder)
    print("Initial Balance:", account.balance)

    print("\n--- Valid Balance Change ---")
    account.balance = 1500.00
    print("New Balance:", account.balance)

    print("\n--- Invalid Balance Change ---")
    try:
        account.balance = -500
    except ValueError as error:
        print("Error:", error)

    print("\n--- ATM TEST ---")

    atm = ATM(account)

    print("\nAttempting to access atm.__pin directly:")

    try:
        print(atm.__pin)
    except AttributeError as error:
        print("Error:", error)

    print("\nAuthenticating...")
    print("Authentication:", atm.authenticate("1234"))

    print("\nChecking Balance:")
    print(f"₱{atm.check_balance():.2f}")

    print("\nDepositing ₱500...")
    print(f"Updated Balance: ₱{atm.perform_deposit(500):.2f}")

    print("\nWithdrawing ₱300...")
    withdrawn = atm.perform_withdrawal(300)
    print(f"Withdrawn: ₱{withdrawn:.2f}")

    print("\nAttempting invalid withdrawal...")
    atm.perform_withdrawal(5000)

    print("\nFinal Balance:")
    print(f"₱{atm.check_balance():.2f}")

    atm.print_mini_statement()