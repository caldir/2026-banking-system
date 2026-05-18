
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import AbstractAccount, BankAccount

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

from domain.accounts import SavingsAccount

print('Banking system started')

savings = SavingsAccount(owner_id="client_2", balance=5000, min_balance=1000)

savings.withdraw(3000)
print(savings.balance)  # должно быть 2000

try:
    savings.withdraw(1500)
except InsufficientFundsError as error:
    print("SavingsAccount limit caught:", error)