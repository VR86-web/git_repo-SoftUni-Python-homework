from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\n"
        robot = next((r.name for r in self.robots), None)
        if robot is not None:
            result += f"Robots: {' '.join([r for r in robot])}"

        else:
            result += "Robots: none"

        return result
