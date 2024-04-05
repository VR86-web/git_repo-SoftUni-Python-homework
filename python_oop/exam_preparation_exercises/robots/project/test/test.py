from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Grigor", 31, 1000)

    def test_correct_init(self):

        self.assertEqual("Grigor", self.player.name)
        self.assertEqual(31, self.player.age)
        self.assertEqual(1000, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_if_name_is_too_short_expect_value_error_with_message(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Gi"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_if_ege_is_not_valid_expect_raises_value_error_with_message(self):

        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_adding_successfully_new_win(self):
        self.player.add_new_win("Sofia")
        self.assertEqual(self.player.wins, ["Sofia"])

    def test_adding_not_successfully_new_win_expect_message(self):
        self.player.wins = ["Wimbledon"]

        self.assertEqual("Wimbledon has been already added to the list of wins!", self.player.add_new_win("Wimbledon"))

    def test_if_main_player_points_are_less_than_the_other_player(self):
        self.player2 = TennisPlayer("Novak", 32, 1000.1)

        self.assertEqual('Novak is a top seeded player and he/she is better than Grigor'
                         , self.player.__lt__(self.player2))

    def test_if_main_player_points_are_more_than_the_other_player(self):
        self.player2 = TennisPlayer("Novak", 32, 999.9)

        self.assertEqual(f'Grigor is a better player than Novak', self.player.__lt__(self.player2))

    def test_correct_str_(self):
        self.player = TennisPlayer("Grigor", 31, 1000)
        self.player.wins = ["Sofia Open", "Vraca ATP"]

        result = str(self.player)

        self.assertEqual(result, "Tennis Player: Grigor\nAge: 31\nPoints: 1000.0\nTournaments won: "
                                 "Sofia Open, Vraca ATP")


if __name__ == "__main__":
    main()