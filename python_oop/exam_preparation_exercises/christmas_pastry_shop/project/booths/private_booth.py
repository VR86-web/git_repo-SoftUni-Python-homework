from project.booths.booth import Booth


class PrivateBooth(Booth):
    pass

    def reserve(self, number_of_people: int):
        self.price_for_reservation += number_of_people * 3.5
        self.is_reserved = True
