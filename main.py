
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import AbstractAccount, BankAccount

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

from domain.accounts import SavingsAccount

print('Banking system started')

savings = SavingsAccount(owner_id="client_2", balance=10000)
print(savings.get_account_info())