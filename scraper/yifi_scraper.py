from helpers.open_url import open_url
from constants.header import header
from movies_scraper import get_movies_from_result, get_movie_information


def search_movie(url, header):
    search_result = open_url(url, header)

    if (search_result):
        movies = get_movies_from_result(search_result)

        if (movies):

            for movie in movies:
                movie.print()

            return movies

    return None


def get_movie(movie_url, header):
    movie_result = open_url(movie_url, header)

    if (movie_result):
        movie = get_movie_information(movie_result, movie_url=movie_url)

        if (movie):
            movie.print()
            return movie

    return None


url = "https://yts.mx/"

# search_results = search_movie(
#     url+"browse-movies/car/all/all/0/latest/0/en", header)

get_movie(url+"movies/the-prophecy-forsaken-2005", header)
