class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie.year, reverse=True)

def sort_by_title(movies):
    def remove_articles(title):
        articles = ["A ", "An ", "The "]
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    return sorted(movies, key=lambda movie: remove_articles(movie.title))

movies = [
    Movie("The Avengers", 2012, ["Action", "Adventure"]),
    Movie("A Clockwork Orange", 1971, ["Crime", "Drama", "Sci-Fi"]),
    Movie("The Godfather", 1972, ["Crime", "Drama"]),
    Movie("Annie Hall", 1977, ["Comedy", "Romance"]),
]

sorted_movies_by_year = sort_by_year(movies)
for movie in sorted_movies_by_year:
    print(movie.title, movie.year)

print()

sorted_movies_by_title = sort_by_title(movies)
for movie in sorted_movies_by_title:
    print(movie.title, movie.year)
