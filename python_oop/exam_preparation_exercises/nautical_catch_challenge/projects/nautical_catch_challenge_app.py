from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_TYPES_OF_DIVERS = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    VALID_TYPES_OF_FISH = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_TYPES_OF_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is not None:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_TYPES_OF_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_TYPES_OF_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = next((f for f in self.divers if f.name == fish_name), None)
        if fish is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_TYPES_OF_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return "{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver.name} missed a good {fish.name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver.name} missed a good {fish.name}."

        else:
            diver.hit(fish)
            message = f"{diver.name} hits a {fish.points}pt. {fish.name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()

        return message

    def health_recovery(self):
        divers_with_health_issues = [d for d in self.divers if d.has_health_issue]

        for diver in divers_with_health_issues:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self, diver_name: str):

        diver = [d for d in self.divers if d.name == diver_name]

        result = f"**{diver_name} Catch Report**\n"

        fish_details = "\n".join([fish.fish_details for fish in diver.catch])
        result += fish_details

        return result

    def competition_statistics(self):
        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        healthy_divers = [d for d in sorted_divers if not d.has_health_issue]

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join([str(d) for d in healthy_divers])

        return result
