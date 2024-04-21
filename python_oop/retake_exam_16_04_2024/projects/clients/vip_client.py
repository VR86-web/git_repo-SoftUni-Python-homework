from project.clients.base_client import BaseClient
from math import floor


class VIPClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, membership_type="VIP")

    def earning_points(self, order_amount: float):
        self.EARNED_POINTS = floor(order_amount * 0.2)
        self.points += self.EARNED_POINTS
        return self.EARNED_POINTS
