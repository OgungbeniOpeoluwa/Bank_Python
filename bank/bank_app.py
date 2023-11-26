from bank.account import Account


def generate_account_name(first_name, second_name):
    return first_name + second_name


class BankApp:
    total_number_of_account = 0
    store_account = []

    def __init__(self):
        self.total_number_of_account = 0

    def create_account(self, first_name, second_name, pin):
        self.total_number_of_account += 1
        number = self.generate_account_number()
        account_name = generate_account_name(first_name, second_name)
        account = Account(account_name, number, pin)
        self.store_account.append(account)
        return account

    def generate_account_number(self):
        return str(self.total_number_of_account)

    def get_total_number_of_account(self):
        return self.total_number_of_account

    def find_account(self, account_number):
        for account in self.store_account:
            if account.get_account_number() == account_number:
                return account

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        account.deposit(amount)

    def check_balance(self, pin, account_number):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def withdraw(self, amount, pin, account_number):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender, reciever, amount, pin):
        sender_account = self.find_account(sender)
        receiver_account = self.find_account(reciever)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)
