from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    MIN_STRENGTH: float = 75.0
    INITIAL_STRENGTH: float = 150.0

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)

    def can_climb(self):
        return self.strength >= SummitClimber.MIN_STRENGTH
