"""Unit 1, Task 3: Encapsulation and controlled balance access."""


class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    print(f"Balance after deposit: {account.get_balance():.2f}")
    print(f"Withdrawal successful: {account.withdraw(80)}")
    print(f"Balance after withdrawal: {account.get_balance():.2f}")
    print(f"Overdraft allowed: {account.withdraw(100)}")
