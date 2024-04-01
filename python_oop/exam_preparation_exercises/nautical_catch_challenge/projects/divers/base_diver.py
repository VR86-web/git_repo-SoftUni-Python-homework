from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.__competition_points: float = 0.0
        self.has_health_issue: bool = False

    @property
    def competition_points(self):
        return round(self.__competition_points, 1)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")

        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")

        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        ...

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.__competition_points += fish.points

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, " \
               f"Points earned: {self.competition_points}]"
