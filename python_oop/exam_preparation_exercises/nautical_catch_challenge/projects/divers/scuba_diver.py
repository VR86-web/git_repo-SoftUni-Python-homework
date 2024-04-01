from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    OXYGEN_LEVEL_VALUE = 540

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL_VALUE)

    def miss(self, time_to_catch: int):
        reduced_amount = round(time_to_catch * 0.3)

        if self.oxygen_level < reduced_amount:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= reduced_amount

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL_VALUE
