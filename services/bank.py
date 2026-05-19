

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
        