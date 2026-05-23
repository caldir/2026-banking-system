from exceptions.banking_exceptions import InvalidOperationError
from domain.enums import AccountStatus
from decimal import Decimal

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

    def open_account(self, client_id, account):
        if client_id not in self.clients:
            raise InvalidOperationError('Client not found')
        if account.account_id in self.accounts:
            raise InvalidOperationError('Account already exists')
        self.accounts[account.account_id] = account
        self.clients[client_id].add_account(account.account_id)
        
    def close_account(self, account_id):
        if account_id not in self.accounts:
            raise InvalidOperationError('Account not found')
        account = self.accounts[account_id]
        account.status = AccountStatus.CLOSED
        client_id = account.owner_id
        self.clients[client_id].remove_account(account_id)

    def freeze_account(self, account_id):
        if account_id not in self.accounts:
            raise InvalidOperationError('Account not found')
        account = self.accounts[account_id]
        account.status = AccountStatus.FROZEN

    def unfreeze_account(self, account_id):
        if account_id not in self.accounts:
            raise InvalidOperationError('Account not found')
        account = self.accounts[account_id]
        account.status = AccountStatus.ACTIVE

    def get_total_balance(self):
        total = Decimal("0")

        for account in self.accounts.values():
            total += account.balance

        return total

    def get_clients_ranking(self):
        ranking = []
        for client in self.clients.values():
            client_total = Decimal("0")

            for account_id in client.accounts:
                account = self.accounts[account_id]
                client_total += account.balance

            ranking.append(
                {
                    "client_id": client.client_id,
                    "full_name": client.full_name,
                    "total_balance": str(client_total),
                }
            )

        ranking.sort(
            key=lambda item: Decimal(item["total_balance"]),
            reverse=True,
        )

        return ranking