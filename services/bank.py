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
            raise InvalidOperationError('Client already exist')
        self.clients[client.client_id] = client
        