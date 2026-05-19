
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

print('Banking system started')

client = Client(full_name="Ivan Petrov", age=30)
client.add_account("acc_1")

print(client.get_client_info())