from abc import ABC, abstractmethod


class BaseClient(ABC):

    MEMBERSHIP_TYPES = (
        "Regular",
        "VIP"
    )

    EARNED_POINTS: float = 0.0

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Client name should be determined!")

        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.MEMBERSHIP_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")

        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        discount_percentage = 0

        if self.EARNED_POINTS >= 100:
            discount_percentage = 10
            self.points -= 100 * 0.1
        elif 50 <= self.EARNED_POINTS < 100:
            discount_percentage = 5
            self.points -= 0.5 * self.points
        elif self.EARNED_POINTS < 50:
            discount_percentage = 0

        return f"({discount_percentage, self.points})"
