from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    VALID_WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }

    VALID_CLIENTS_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        name = self.get_waiter_name(waiter_name)
        if name is not None:
            return f"{waiter_name} is already on the staff."

        waiter = self.VALID_WAITER_TYPES[waiter_name](hours_worked)
        self.waiters.append(waiter)
        return f"{waiter.name} is successfully hired as a {waiter.type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENTS_TYPES:
            return f"{client_type} is not a recognized client type."

        name = self.get_client_name(client_name)
        if name:
            return f"{client_name} is already a client."

        client = self.VALID_CLIENTS_TYPES[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        name = self.get_waiter_name(waiter_name)

        if name is None:
            return f"No waiter found with the name {waiter_name}."

        else:
            return name.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        name = self.get_client_name(client_name)

        if name is None:
            return f"{client_name} is not a registered client."

        else:
            return name.earning_points(order_amount)

    def apply_discount_to_client(self, client_name: str):
        name = self.get_client_name(client_name)

        if name is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        else:
            return name.apply_discount()

    def generate_report(self):
        pass

    def get_waiter_name(self, waiter_name):
        name = next((w for w in self.waiters if w.name == waiter_name), None)
        if name is not None:
            return name
        else:
            return None

    def get_client_name(self, client_name):
        name = next((c for c in self.clients if c.name == client_name), None)

        if name is not None:
            return name

        else:
            return None

