from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Pod Igoto", 1990, 10.00, )

    def test_correct_init(self):

        self.assertEqual("Pod Igoto", self.movie.name)
        self.assertEqual(1990, self.movie.year)
        self.assertEqual(10.00, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_if_name_is_empty_str_expect_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_movie_year_if_is_not_valid_value_expect_raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1850

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_successful_adding_actor_in_actors_list(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("Andrej Slabakov")

        self.assertEqual(["Andrej Slabakov"], self.movie.actors)

    def test_adding_actor_in_actors_list_if_actor_is_already_there_expect_message(self):
        self.movie.add_actor("Andrej Slabakov")
        result = self.movie.add_actor("Andrej Slabakov")

        expected_message = "Andrej Slabakov is already added in the list of actors!"

        self.assertEqual(expected_message, result)

    def test_compare_if_movie_rating_is_greater_then_another(self):
        movie2 = Movie("The Avengers", 2020, 7.6)

        result = self.movie < movie2

        self.assertEqual('"Pod Igoto" is better than "The Avengers"', result)

    def test_compare_if_new_movie_rating_is_greater_then_the_existing_one(self):
        movie2 = Movie("The Avengers", 2020, 10.1)

        result = self.movie > movie2

        self.assertEqual('"The Avengers" is better than "Pod Igoto"', result)

    def test_repr(self):

        self.movie.add_actor("Georgi Parcalev")
        self.movie.add_actor("Georgi Kaloyanchev")

        expected = """Name: Pod Igoto
Year of Release: 1990
Rating: 10.00
Cast: Georgi Parcalev, Georgi Kaloyanchev"""
        result = self.movie.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

