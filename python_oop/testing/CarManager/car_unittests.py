from unittest import TestCase, main

from python_oop.testing.CarManager.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_init(self):

        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_amount_with_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_amount_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_car_with_valid_amount_of_fuel_more_then_capacity_fills_to_capacity(self):
        self.car.refuel(1000)
        expecting_result = self.car.fuel_amount = 75

        self.assertEqual(expecting_result, self.car.fuel_amount)

    def test_car_drive_without_fuel_expecting_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(8000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_fuel_decreases_fuel(self):
        self.car.fuel_amount = 10
        self.car.drive(10)
        expected_result = self.car.fuel_amount = 8.5

        self.assertEqual(expected_result, self.car.fuel_amount)


if __name__ == "__main__":
    main()

