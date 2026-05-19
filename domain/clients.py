import uuid
from domain.enums import ClientStatus
from exceptions.banking_exceptions import InvalidOperationError

class Client():

    def __init__(
        self,
        age,
        full_name,
        client_id=None,
        status=ClientStatus.ACTIVE,
        accounts=None,
        contacts=None,
        failed_login_attempts=0
    ):
        if age < 18:
            raise InvalidOperationError("Client must be at least 18 years old")
        self.age = age
        
        if client_id is None:
            self.client_id = self._generate_client_id()
        else:
            self.client_id = client_id

        self.full_name = full_name
        self.status = status

        if accounts is None:
            self.accounts = []
        else:
            self.accounts = accounts

        if contacts is None:
            self.contacts = {}
        else:
            self.contacts = contacts
        self.failed_login_attempts = failed_login_attempts

    def _generate_client_id(self):
        return uuid.uuid4().hex[:10]

    def add_account(self, account_id):
        if account_id in self.accounts:
            raise InvalidOperationError('Account already exists')
        self.accounts.append(account_id)

    def remove_account(self, account_id):
        if account_id not in self.accounts:
            raise InvalidOperationError('Account not found')
        self.accounts.remove(account_id)

    def get_client_info(self):
        info = {
            "client_id": self.client_id,
            "full_name": self.full_name,
            "age": self.age,
            "status": self.status.value,
            "accounts": self.accounts,
            "contacts": self.contacts,
            "failed_login_attempts": self.failed_login_attempts,
        }
        return info