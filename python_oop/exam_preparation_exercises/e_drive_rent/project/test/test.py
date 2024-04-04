from project.robot import Robot

from unittest import TestCase, main


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']

    def setUp(self):
        self.robot = Robot("Test", 'Military', 10, 1000.0)

    def test_correct_init(self):

        self.assertEqual("Test", self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1000.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_if_category_is_not_in_allowed_categories_expect_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_if_price_is_negative_value_expect_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.price = - 1

        self.assertEqual("Price cannot be negative!", str(ve.exception ))

    def test_update_if_component_already_in_robot_components_expect_message(self):
        self.robot.hardware_upgrades = ["Test Upgrade"]
        self.robot.robot_id = "Test"
        testing = self.robot.upgrade("Test Upgrade", 4)

        self.assertEqual(f"Robot Test was not upgraded.", testing)

    def test_upgrade_if_component_is_not_in_robot_components(self):
        self.robot.hardware_upgrades = []
        testing = self.robot.upgrade("Testing", 6)
        expected_result = f'Robot Test was upgraded with Testing.'

        self.assertEqual(expected_result, testing)

    def test_update_with_less_capacity_than_needed_expect_message(self):
        self.robot.available_capacity = 10

        testing = self.robot.update(1.1, 12)
        expected_result = f"Robot Test was not updated."

        self.assertEqual(expected_result, testing)

    def test_update_with_correct_parameters_expect_message(self):
        self.robot.software_updates = [0.0]
        testing = self.robot.update(1.4, 4)
        expected_result = "Robot Test was updated to version 1.4."

        self.assertEqual(expected_result, testing)

    def test_if_robot_price_is_higher_than_given_price_expect_message(self):
        robot2 = Robot("Test2", 'Military', 10, 67.3)
        self.robot.price = 100
        testing = self.robot.__gt__(robot2)
        expected_result = f'Robot with ID Test is more expensive than Robot with ID Test2.'

        self.assertEqual(expected_result, testing)

    def test_if_robot_price_is_equal_than_given_price_expect_message(self):
        robot2 = Robot("Test2", 'Military', 10, 100.0)
        self.robot.price = 100
        testing = self.robot.__gt__(robot2)
        expected_result = 'Robot with ID Test costs equal to Robot with ID Test2.'

        self.assertEqual(expected_result, testing)

    def test_if_robot_price_is_lower_than_given_price_expect_message(self):
        robot2 = Robot("Test2", 'Military', 10, 100.0)
        self.robot.price = 99.9
        testing = self.robot.__gt__(robot2)
        expected_result = 'Robot with ID Test is cheaper than Robot with ID Test2.'

        self.assertEqual(expected_result, testing)


if __name__ == "__main__":
    main()

