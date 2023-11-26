from bank.exception.insufficient_amount_exception import InsufficientAmount
from bank.exception.invalid_amount_exception import InvalidAmount
from bank.invalid_pin import InvalidPin


class Account:
    balance = 0

    def __init__(self, account_name, account_number, pin):
        self.accountName = account_name
        self.accountNumber = account_number
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        self.validate_deposit_amount(amount)
        self.balance += amount

    def check_balance(self, pin):
        self.validate_pin(pin)
        return self.balance

    def validate_pin(self, pin):
        if self.pin != pin:
            raise InvalidPin("Invalid Pin")

    def validate_deposit_amount(self, amount):
        if amount < 0:
            raise InvalidAmount("Invalid Amount")

    def validate_withdraw_amount(self, amount):
        if amount > self.balance:
            raise InsufficientAmount("Insufficient Amount")

    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        self.validate_withdraw_amount(amount)
        self.balance -= amount

    def get_account_number(self):
        return self.accountNumber
