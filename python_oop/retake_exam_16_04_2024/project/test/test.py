from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Main", 100)

    def test_correct_init(self):
        self.assertEqual("Main", self.restaurant.name)
        self.assertEqual(100, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_correct_name_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:

            self.restaurant.name = ""

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_correct_capacity_value_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -10

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters(self):
        self.restaurant.waiters = [{'name': "Test", 'total_earnings': 10}]

        self.assertEqual([{'name': 'Test', 'total_earnings': 10}], self.restaurant.get_waiters(None, None))

    def test_add_waiter_if_waiters_capacity_is_not_lower_expect_message(self):
        self.restaurant.capacity = 2
        self.restaurant.waiters = ["Test"]

        self.assertEqual("No more places!", self.restaurant.add_waiter('Test2'))

    def test_add_waiter_if_waiter_exist_expect_message(self):

        self.assertEqual(f"The waiter Test has been added.", self.restaurant.add_waiter("Test"))

    def test_incorrect_remove_waiter_expect_message(self):
        self.restaurant.waiters = [{'name': "Test"}]

        self.assertEqual(f"No waiter found with the name Test2.", self.restaurant.remove_waiter("Test2"))

    def test_correct_remove_waiter(self):
        self.restaurant.waiters = [{'name': "Test"}]

        self.assertEqual(f"The waiter Test has been removed.", self.restaurant.remove_waiter("Test"))

    def test_total_earnings(self):
        self.restaurant.waiters = [{'total_earnings': 10}]

        self.assertEqual(10, 10)


if __name__ == "__maim__":
    main()