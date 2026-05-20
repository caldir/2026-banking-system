
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

bank = Bank("Mentor Bank")
client = Client(full_name="Ivan Petrov", age=30)
account = BankAccount(owner_id=client.client_id, balance=1000)

bank.add_client(client)
bank.open_account(client.client_id, account)

print(bank.accounts)
print(client.accounts)