
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

premium.withdraw(3000)
print(premium.balance)  # -2050

try:
    premium.withdraw(4000)
except InsufficientFundsError as error:
    print("PremiumAccount overdraft caught:", error)