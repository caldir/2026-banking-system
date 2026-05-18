
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import AbstractAccount, BankAccount

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

print('Banking system started')

account = BankAccount(owner_id="client_1")
print(account)
account.deposit(1000)
account.withdraw(300)
print(account.balance)
print(account.get_account_info())
try:
    account.withdraw(100000)
except InsufficientFundsError as error:
    print('InsufficientFundError cauth:', error)
try:
    account.deposit(-100)
except InvalidOperationError as error:
    print("InvalidOperationError caught:", error)