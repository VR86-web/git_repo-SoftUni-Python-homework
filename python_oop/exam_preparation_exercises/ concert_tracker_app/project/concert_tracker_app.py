from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIANS_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in self.VALID_MUSICIANS_TYPES:
            raise ValueError("Invalid musician type!")

        musician = next((m for m in self.musicians if m.name == name), None)
        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIANS_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next((b for b in self.bands if b.name == name), None)
        if band is None:
            b = Band(name)
            self.bands.append(b)
            return f"{name} was created."

        raise Exception(f"{name} band is already created!")

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_place = next((p for p in self.concerts if p.place == place), None)
        if concert_place is None:
            new_concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(new_concert)
            return f"{genre} concert in {place} was added."

        raise Exception(f"{concert_place.place} is already registered for {concert_place.genre} concert!")

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        searched_name = next((m for m in band.members if m.name == musician_name), None)
        if searched_name is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(searched_name)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [s for s in band.members if isinstance(s, Singer)]
        drummers = [d for d in band.members if isinstance(d, Drummer)]
        guitarists = [g for g in band.members if isinstance(g, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_singers_qualified = True
        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    are_singers_qualified = False

            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False

            else:
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False

        are_drummers_qualified = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False

            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False

            else:
                if "play the drums with drum brushes" not in drummer.skills:
                    are_drummers_qualified = False

        are_guitarist_qualified = True
        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarist_qualified = False

            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    are_guitarist_qualified = False

            else:
                if "play jazz" not in guitarist.skills:
                    are_guitarist_qualified = False

        if not are_guitarist_qualified or not are_drummers_qualified or not are_singers_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
