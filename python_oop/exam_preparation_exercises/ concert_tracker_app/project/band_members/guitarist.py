from project.band_members.musician import Musician

AVAILABLE_SKILLS = (
    "play metal",
    "play rock",
    "play jazz"
)


class Guitarist(Musician):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.available_skills_to_learn = AVAILABLE_SKILLS
