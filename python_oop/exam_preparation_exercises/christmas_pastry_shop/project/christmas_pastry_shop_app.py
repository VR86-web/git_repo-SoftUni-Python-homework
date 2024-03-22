from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    VALID_DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    VALID_BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if type_delicacy not in self.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        searched_delicacy = [d for d in self.delicacies if d.name == name]
        if searched_delicacy:
            raise Exception(f"{name} already exists!")

        delicacy = self.VALID_DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        searched_booth = [b for b in self.booths if b.booth_number == booth_number]
        if searched_booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        searched_booth = next((b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved), None)
        if searched_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        searched_booth.reserve(number_of_people)
        return f"Booth {searched_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        searched_booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        searched_delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if searched_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if searched_delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        searched_booth.delicacy_orders.append(searched_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number))
        all_orders_price = sum([b.price for b in booth.delicacy_orders])
        bill = booth.price_for_reservation + all_orders_price
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
