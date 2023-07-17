from sort import sort_by_year, sort_by_title, Movie
import unittest

class TestMovieSorting(unittest.TestCase):
    def setUp(self):
        self.movies = [
            Movie("The Shawshank Redemption", 1994, ["Action", "Adventure"]),
            Movie("A Clockwork Orange", 1971, ["Crime", "Drama", "Sci-Fi"]),
            Movie("The Third Man", 1949, ["Crime", "Drama"]),
            Movie(" Alien", 1979, ["Comedy", "Romance"]),
        ]

    def test_sort_by_year(self):
        sorted_movies = sort_by_year(self.movies)
        years = [movie.year for movie in sorted_movies]
        self.assertEqual(years, [1994, 1979, 1971, 1949])

    def test_sort_by_title(self):
        sorted_movies = sort_by_title(self.movies)
        titles = [movie.title.strip() for movie in sorted_movies]  # Remove leading/trailing whitespace
        self.assertEqual(
            titles,
            ["Alien", "A Clockwork Orange", "The Shawshank Redemption", "The Third Man"],
        )
