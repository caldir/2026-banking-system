from exceptions.banking_exceptions import InvalidOperationError

class Bank():

    def __init__(
        self,
        name,
        clients=None,
        accounts=None
    ):
        self.name = name
        if clients is None:
            self.clients = {}
        else:
            self.clients = clients
        if accounts is None:
            self.accounts = {}
        else:
            self.accounts = accounts

    def add_client(self, client):
        if client.client_id in self.clients:
            raise InvalidOperationError('Client already exists')
        self.clients[client.client_id] = client

    def open_account(self,client,account):
        if client.client_id not in self.clients:
            raise InvalidOperationError('Client not found')
        if account.account_id in self.accounts:
            raise InvalidOperationError('Account already exists')
        self.accounts[account_id] = account
        self.clients[client_id].add_account(account.account_id)
        