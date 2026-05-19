
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

from domain.clients import Client
from services.bank import Bank
from exceptions.banking_exceptions import InvalidOperationError

bank = Bank("Mentor Bank")

client = Client(full_name="Ivan Petrov", age=30)

bank.add_client(client)

print(bank.clients)

try:
    bank.add_client(client)
except InvalidOperationError as error:
    print("Duplicate client caught:", error)