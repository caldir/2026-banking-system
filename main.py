
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
client.add_account("acc_2")
print(client.accounts)  # ['acc_1', 'acc_2']

client.remove_account("acc_1")
print(client.accounts)  # ['acc_2']

try:
    client.add_account("acc_2")
except InvalidOperationError as error:
    print("Duplicate account caught:", error)

try:
    client.remove_account("missing_acc")
except InvalidOperationError as error:
    print("Missing account caught:", error)