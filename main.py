
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import (
    AbstractAccount,
    BankAccount,
    SavingsAccount,
    PremiumAccount
)

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

print('Banking system started')

premium = PremiumAccount(owner_id="client_3", balance=1000)

print(premium)
print(premium.balance)
print(premium.overdraft_limit)
print(premium.fixed_fee)
print(premium.get_account_info())