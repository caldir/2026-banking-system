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
        
        if client_id == None:
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
