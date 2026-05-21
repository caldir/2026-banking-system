
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
bank.add_client(client)

account_1 = BankAccount(owner_id=client.client_id, balance=1000)
account_2 = SavingsAccount(owner_id=client.client_id, balance=5000)

bank.open_account(client.client_id, account_1)
bank.open_account(client.client_id, account_2)

print(bank.get_total_balance())  # 6000