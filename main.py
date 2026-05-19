
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

print(client.client_id)
print(client.full_name)
print(client.age)
print(client.status.value)
print(client.accounts)
print(client.contacts)
print(client.failed_login_attempts)

try:
    Client(full_name="Young Client", age=16)
except InvalidOperationError as error:
    print("Client age error caught:", error)