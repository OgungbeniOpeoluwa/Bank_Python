import unittest

from bank.bank_app import BankApp


class MyTestCase(unittest.TestCase):
    def test_create_account(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        self.assertEqual(1, bank.get_total_number_of_account())
        self.assertEqual("1", account.get_account_number())

    def test_create_two_account_get_total_number_of_account_created(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        account2 = bank.create_account("Delighted", "Joy", "1999")
        self.assertEqual(2, bank.get_total_number_of_account())
        self.assertEqual("1", account.get_account_number())
        self.assertEqual("2", account2.get_account_number())

    def test_create_two_account_find_account(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        account2 = bank.create_account("Delighted", "Joy", "1999")
        self.assertEqual(2, bank.get_total_number_of_account())
        self.assertEqual(account, bank.find_account('1'))
        self.assertEqual(account2, bank.find_account('2'))

    def test_deposit(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        bank.deposit(1000, "1")
        self.assertEqual(1000, bank.check_balance("1999", "1"))

    def test_withdraw(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        bank.deposit(1000, "1")
        bank.withdraw(500, "1999", "1")
        self.assertEqual(500, bank.check_balance("1999", "1"))

    def test_transfer_to_another_account(self):
        bank = BankApp()
        account = bank.create_account("Delighted", "Joy", "1999")
        account2 = bank.create_account("Delighted", "Joy", "1999")
        bank.deposit(5000, "1")
        bank.transfer("1", "2", 2000, "1999")
        self.assertEqual(3000, bank.check_balance("1999", "1"))
        self.assertEqual(2000, bank.check_balance("1999", "2"))


if __name__ == '__main__':
    unittest.main()
