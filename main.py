
from domain.enums import AccountStatus, Currency 
from domain.accounts import (
    AbstractAccount,
    BankAccount,
    SavingsAccount,
    PremiumAccount,
    InvestmentAccount
)
from exceptions.banking_exceptions import (
    AccountFrozenError,
    InsufficientFundsError,
    InvalidOperationError,
)
from domain.clients import Client
from services.bank import Bank

print('Banking system started')

from services.bank import Bank

bank = Bank("Mentor Bank")

print(bank.name)
print(bank.clients)
print(bank.accounts)