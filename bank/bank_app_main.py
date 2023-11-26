from bank import account
from bank.bank_app import BankApp

bank = BankApp()


def display():
    print("""
              ======================================
              1. create an account
              2  deposit
              3  withdraw
              4  transfer
              =========================================""")
    return int(input("Enter a number"))


inputs = display()
if inputs == 1:
    name = input("Enter your first name: ")
    secondName = input("Enter your second name: ")
    pin = input("Enter your pin: ")
    bank.create_account(name, secondName, pin)
    account.Account.display_account()
elif inputs == 2:
    amount = int(input("Enter amount : "))
    accountNumber = input("Enter your account number: ")
    bank.deposit(amount, accountNumber)
    account.Account.display_account()
    display()

elif inputs == 3:
    amount = int(input("Enter amount : "))
    pin = input("Enter your pin: ")
    accountNumber = input("Enter your account number: ")
    bank.withdraw(amount, pin, accountNumber)
    account.Account.display_account()
    display()

elif inputs == 4:
    amount = int(input("Enter amount : "))
    pin = input("Enter your pin: ")
    accountNumber = input("Enter your account number: ")
    reciever = input("Enter reciever account number")
    bank.transfer(accountNumber, reciever, amount, pin)
    account.Account.display_account()
    display()
