from abc import ABC, abstractmethod
from domain.enums import AccountStatus, Currency
from decimal import Decimal
from exceptions.banking_exceptions import InvalidOperationError, AccountClosedError, AccountFrozenError, InsufficientFundsError

import uuid

class AbstractAccount(ABC):
    def __init__(
        self, 
        owner_id, 
        balance=0, 
        currency=Currency.RUB, 
        account_id=None, 
        status=AccountStatus.ACTIVE
    ):
        self._balance = Decimal(balance)
        self.currency = currency
        self.owner_id = owner_id
        self.status = status

        if account_id is None:
            self.account_id = self._generate_account_id()
        else:
            self.account_id = account_id
  
    def _generate_account_id(self):
        return uuid.uuid4().hex[:10]

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_account_info(self):
        pass

class BankAccount(AbstractAccount):

    def __str__(self):
        return (
                f"{self.__class__.__name__} | "
                f"Owner: {self.owner_id} | "
                f"Account: ****{self.account_id[-4:]} | "
                f"Status: {self.status.value} | "
                f"Balance: {str(self._balance)} {self.currency.value}"
        )

    def deposit(self, amount):
        amount = Decimal(amount)
        self._check_active()
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount):
        amount = Decimal(amount)
        self._check_active()
        self._validate_amount(amount)
        self._check_sufficient_funds(amount)
        self._balance -= amount

    def get_account_info(self):
        return {'account_id': self.account_id,
                'owner_id': self.owner_id,
                'type': self.__class__.__name__,
                'balance':str(self._balance),
                'currency': self.currency.value,
                'status':self.status.value}

    def _validate_amount(self, amount):
        amount = Decimal(amount)
        if amount <= 0:
            raise InvalidOperationError("Amount must be greater than zero")

    def _check_sufficient_funds(self, amount):
        amount = Decimal(amount)
        if amount > self._balance:
            raise InsufficientFundsError('Insufficient funds')
    
    def _check_active(self):
        if self.status == AccountStatus.FROZEN:
            raise AccountFrozenError('Account is frozen')
        elif self.status == AccountStatus.CLOSED:
            raise AccountClosedError('Account is closed')
    
    @property
    def balance(self):
        return self._balance


class SavingsAccount(BankAccount):

    def __init__(
        self,
        owner_id,
        balance=0,
        currency=Currency.RUB,
        account_id=None,
        status=AccountStatus.ACTIVE,
        min_balance=1000,
        monthly_interest_rate="0.01",
    ):
        super().__init__(
            owner_id=owner_id,
            balance=balance, 
            currency=currency, 
            account_id=account_id, 
            status=status
        )

        self.min_balance = Decimal(min_balance)
        self.monthly_interest_rate = Decimal(monthly_interest_rate)

    def withdraw(self, amount):
        amount = Decimal(amount)
        self._check_active()
        self._validate_amount(amount)
        
        if self._balance - amount < self.min_balance:
            raise InsufficientFundsError('Cannot go below minimum balance')
        
        self._balance -= amount

    def apply_monthly_interest(self):
        self._check_active()

        interest = self._balance * self.monthly_interest_rate
        self._balance += interest

    def get_account_info(self):
        info = super().get_account_info()
        info['min_balance'] = str(self.min_balance)
        info['monthly_interest_rate'] = str(self.monthly_interest_rate)

        return info

class PremiumAccount(BankAccount):

    def __init__(
        self,
        owner_id,
        balance=0,
        currency=Currency.RUB,
        account_id=None,
        status=AccountStatus.ACTIVE,
        overdraft_limit=5000,
        fixed_fee=50
        ):
        super().__init__(
            owner_id=owner_id,
            balance=balance, 
            currency=currency, 
            account_id=account_id, 
            status=status
        )

        self.overdraft_limit = Decimal(overdraft_limit)
        self.fixed_fee = Decimal(fixed_fee)

    def withdraw(self, amount):
        amount = Decimal(amount)
        self._check_active()
        self._validate_amount(amount)
        total_amount = amount + self.fixed_fee
        if self._balance + self.overdraft_limit < total_amount:
            raise InsufficientFundsError('Overdraft limit exceeded')
        self._balance -= total_amount
