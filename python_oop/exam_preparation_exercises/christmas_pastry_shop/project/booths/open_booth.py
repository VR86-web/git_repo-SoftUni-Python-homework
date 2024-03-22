from project.booths.booth import Booth


class OpenBooth(Booth):
    pass

    def reserve(self, number_of_people: int):
        self.price_for_reservation += number_of_people * 2.5
        self.is_reserved = True
