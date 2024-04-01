from unittest import TestCase, main

from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Vraca")

    def test_correct_init(self):

        self.assertEqual("Vraca", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_correct_name_expect_raise_value_error(self):

        with self.assertRaises(ValueError) as ve:

            self.station.name = "AI"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_successful_adding_new_train_info_on_board_into_arrival_trains(self):
        self.station.new_arrival_on_board("Info")
        expected_result = self.station.arrival_trains = deque(["Info"])

        self.assertEqual(self.station.arrival_trains, expected_result)

    def test_train_has_arrived_others_arrival_trains(self):
        self.station.new_arrival_on_board("Test")

        train_info = "Test2"
        result = self.station.train_has_arrived(train_info)
        expected_message = f"There are other trains to arrive before {train_info}."
        self.assertEqual(expected_message, result)

    def test_train_has_arrived_returning_message(self):
        self.station.new_arrival_on_board("Test")
        train_info = "Test"
        result = self.station.train_has_arrived(train_info)
        expected_message = f"{train_info} is on the platform and will leave in 5 minutes."

        self.assertEqual(expected_message, result)

    def test_train_has_arrived_go_to_departures(self):
        self.station.new_arrival_on_board("Test")
        train_info = "Test"
        self.station.train_has_arrived(train_info)

        self.assertEqual(len(self.station.arrival_trains), 0)

    def test_train_has_left_no_departure_trains_true(self):
        self.station.arrival_trains = deque(["Test"])
        train_info = "Test"
        self.station.train_has_arrived(train_info)

        self.assertTrue(self.station.departure_trains)

    def test_train_has_left_no_departure_trains_false(self):
        self.station.arrival_trains = deque(["Test"])
        train_info = "Test2"
        self.station.train_has_arrived(train_info)

        self.assertFalse(self.station.departure_trains)


if __name__ == "__main__":
    main()
