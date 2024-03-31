from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    pass

    def calculate_difficulty_level(self):
        if self.elevation > 3_000:
            return "Extreme"

        elif 2_000 <= self.elevation <= 3_000:
            return "Advanced"

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
