from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.traveler = Trip(10000, 1, False)
        self.traveler2 = Trip(10000, 2, False)
        self.traveler3 = Trip(10000, 2, True)

    def test_init_trip(self):
        self.assertEqual(10000, self.traveler3.budget)
        self.assertEqual(2, self.traveler2.travelers)
        self.assertFalse(self.traveler2.is_family)
        self.assertEqual({}, self.traveler2.booked_destinations_paid_amounts)

    def test_travellers_setter_if_value_is_less_then_1_expect_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.traveler.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_setter_is_family(self):
        self.assertTrue(self.traveler3.is_family)

        self.traveler.is_family = True

        self.assertFalse(self.traveler.is_family)

    def test_book_a_trip_when_destination_not_in_destinations_offers_expect_return_message_not_valid_destination(self):

        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.traveler.book_a_trip("Vraca"))

    def test_book_a_trip_with_not_enough_budget(self):
        result = self.traveler2.book_a_trip('New Zealand')

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_successfully_no_family_discount(self):
        result = self.traveler2.book_a_trip("Bulgaria")

        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9000.00', result)
        self.assertEqual(9000, self.traveler2.budget)
        self.assertEqual({"Bulgaria": 1000}, self.traveler2.booked_destinations_paid_amounts)

    def test_book_a_trip_successfully_with_family_discount(self):
        result = self.traveler3.book_a_trip("Bulgaria")

        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9100.00', result)
        self.assertEqual(9100, self.traveler3.budget)
        self.assertEqual({"Bulgaria": 900}, self.traveler3.booked_destinations_paid_amounts)

    def test_booking_status_with_no_bookings(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.traveler3.booking_status())

    def test_booking_status_with_bookings(self):
        self.traveler2.budget = 100000
        self.traveler2.book_a_trip("Brazil")
        self.traveler2.book_a_trip("New Zealand")

        result = self.traveler2.booking_status()
        expected = """Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00"""
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()