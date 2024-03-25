from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Lada", "Niva", 100000, 10000)

    def test_correct_init(self):
        self.assertEqual("Lada", self.car.model)
        self.assertEqual("Niva", self.car.car_type)
        self.assertEqual(100000, self.car.mileage)
        self.assertEqual(10000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_if_price_is_lower_than_1_expect_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_if_car_mileage_is_too_low_expect_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 87

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_if_promotional_price_is_greater_than_current_price_expect_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(15000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_if_promotional_price_is_correct_expect_old_actual_price_to_be_replaced_with_the_new_one(self):
        self.car.set_promotional_price(7000)

        self.assertEqual(7000, self.car.price)

    def test_if_car_price_is_set_correctly_should_return_message(self):
        expected_result = 'The promotional price has been successfully set.'

        self.assertEqual(expected_result, self.car.set_promotional_price(7000))

    def test_if_price_for_repairing_is_too_high_return_message(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(6500, "motor"))

    def test_if_price_for_repair_is_correct_expect_increase_current_price(self):
        self.car.need_repair(2000, "motor")

        self.assertEqual(12000, self.car.price)

    def test_if_after_repairing_the_list_with_repairs_append_description(self):
        self.car.need_repair(2000, "motor")

        self.assertEqual(["motor"], self.car.repairs)

    def test_after_successful_repairing_expect_message(self):
        expected_message = 'Price has been increased due to repair charges.'

        self.assertEqual(expected_message, self.car.need_repair(2000, "motor"))

    def test_if_after_comparing_the_car_type_with_another_different_car_type_expect_message_for_incorrect_type(self):
        car2 = SecondHandCar("Lada", "Samara", 200000, 5000)

        result = car2 > self.car

        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare(self):
        car2 = SecondHandCar("Lada", "Niva", 200000, 5000)

        result = car2 > self.car

        self.assertFalse(result)

    def test_str(self):
        self.assertEqual(str(self.car), """Model Lada | Type Niva | Milage 100000km
Current price: 10000.00 | Number of Repairs: 0""")


if __name__ == "__main__":
    main()

