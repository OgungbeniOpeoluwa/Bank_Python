import unittest
import pytest

from bank.account import Account
from bank.exception.insufficient_amount_exception import InsufficientAmount
from bank.exception.invalid_amount_exception import InvalidAmount
from bank.invalid_pin import InvalidPin


class MyTestCase(unittest.TestCase):
    def test_something(self):
        account = Account("delighted", "123", "1999")
        account.deposit(1000)
        self.assertEqual(1000, account.check_balance("1999"))

    def test_deposit_lesser_than_0(self):
        account = Account("delighted", "123", "1999")
        with pytest.raises(InvalidAmount) as ex:
            account.deposit(-1)
        assert(str(ex.value)) == "Invalid Amount"


    def test_withdraw_method(self):
        account = Account("delighted", "123", "1999")
        account.deposit(1000)
        account.withdraw(500, "1999")
        self.assertEqual(500, account.check_balance("1999"))

    def test_withdraw_method_with_wrong_password(self):
        account = Account("delighted", "123", "1999")
        account.deposit(1000)
        with pytest.raises(InvalidPin) as ex:
            account.withdraw(500, "1998")
        assert(str(ex.value)) == "Invalid Pin"

    def test_withdraw_method_with_Insufficient_Amount(self):
        account = Account("delighted", "123", "1999")
        account.deposit(1000)
        with pytest.raises(InsufficientAmount) as ex:
            account.withdraw(5000, "1999")
        assert(str(ex.value)) == "Insufficient Amount"


if __name__ == '__main__':
    unittest.main()
