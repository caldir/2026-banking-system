
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import (
    AbstractAccount,
    BankAccount,
    SavingsAccount,
    PremiumAccount,
    InvestmentAccount
)

from exceptions.banking_exceptions import (
    InsufficientFundsError,
    InvalidOperationError,
)

print('Banking system started')

investment = InvestmentAccount(
    owner_id="client_4",
    balance=10000,
    expected_yearly_growth="0.08",
)

print(investment.project_yearly_growth())  # 800.00 или 800
print(investment.balance)                  # 10000