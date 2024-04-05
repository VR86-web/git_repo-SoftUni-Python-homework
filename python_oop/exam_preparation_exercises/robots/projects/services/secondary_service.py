from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        robot = next((r.name for r in self.robots), None)
        if robot is not None:
            result += f"Robots: {' '.join(*robot)}"

        else:
            result += "Robots: none"

        return result
