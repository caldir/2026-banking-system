
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

investment = InvestmentAccount(owner_id="client_4", balance=10000)

print(investment)
print(investment.balance)
print(investment.portfolio)
print(investment.expected_yearly_growth)
print(investment.get_account_info())