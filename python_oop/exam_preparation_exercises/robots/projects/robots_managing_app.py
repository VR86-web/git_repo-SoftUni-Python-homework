from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICE_TYPE = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    VALID_ROBOT_TYPE = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPE:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICE_TYPE[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPE:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOT_TYPE[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_name(robot_name)
        service = self.find_service_name(service_name)

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."

        if service.capacity <= len(self.services):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot.name} to {service.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_name(robot_name)
        service = self.find_service_name(service_name)

        if robot is None:
            return "No such robot in this service!"

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_name(service_name)
        fed_robots = [r.eating() for r in service.robots]
        return f"Robots fed: {len(fed_robots)}."

    def service_price(self, service_name: str):
        service = self.find_service_name(service_name)
        robots_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {robots_price:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def find_robot_name(self, robot_name):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        return robot if robot is not None else None

    def find_service_name(self, service_name):
        service = next((s for s in self.services if s.name == service_name), None)
        return service if service is not None else None