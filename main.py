
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

client_1 = Client(full_name="Ivan Petrov", age=30)
client_2 = Client(full_name="Anna Smirnova", age=28)

bank.add_client(client_1)
bank.add_client(client_2)

account_1 = BankAccount(owner_id=client_1.client_id, balance=1000)
account_2 = SavingsAccount(owner_id=client_1.client_id, balance=5000)
account_3 = PremiumAccount(owner_id=client_2.client_id, balance=10000)

bank.open_account(client_1.client_id, account_1)
bank.open_account(client_1.client_id, account_2)
bank.open_account(client_2.client_id, account_3)

ranking = bank.get_clients_ranking()

for item in ranking:
    print(item)