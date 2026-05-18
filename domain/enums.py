from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 'active'
    FROZEN = 'frozen'
    CLOSED = 'closed'

class Currency(Enum):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    KZT = 'KZT'
    CNY = 'CNY'

class ClientStatus(Enum):
    ACTIVE = 'active'
    BLOCKED = 'blocked'
    SUSPICIOUS = 'suspicious'