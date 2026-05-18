
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import AbstractAccount, BankAccount

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

from domain.accounts import SavingsAccount

print('Banking system started')

savings = SavingsAccount(
    owner_id="client_2",
    balance=10000,
    monthly_interest_rate="0.01",
    status=AccountStatus.FROZEN
)

savings.apply_monthly_interest()
print(savings.balance)  # должно быть 10100.00 или 10100