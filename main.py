
from domain.enums import AccountStatus, Currency 
from exceptions.banking_exceptions import AccountFrozenError
from domain.accounts import AbstractAccount, BankAccount

print('Banking system started')
print(AccountStatus.ACTIVE.value)
print(Currency.RUB.value)
print(AccountFrozenError)

print(AbstractAccount)

account = BankAccount(owner_id="client_1")
print(account.get_account_info())