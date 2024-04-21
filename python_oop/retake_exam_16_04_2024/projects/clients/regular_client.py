from project.clients.base_client import BaseClient
from math import floor


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, membership_type="Regular")

    def earning_points(self, order_amount: float):
        self.EARNED_POINTS = floor(order_amount * 0.1)
        self.points += self.EARNED_POINTS
        return self.EARNED_POINTS
