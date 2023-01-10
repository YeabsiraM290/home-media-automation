from bs4 import BeautifulSoup

from models.models import Movie
from helpers.img_link_sanitizer import sanitize_img_link


def get_movies_from_result(search_result):

    try:
        bs = BeautifulSoup(search_result.read(), 'html.parser')
        data = []
        movie_resluts = bs.find('div', {'class': 'browse-content'}).section
        movies = movie_resluts.find_all(
            'div', {'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})

        for movie in movies:

            title = movie.find('a', {'class': 'browse-movie-title'}).get_text()
            year = movie.find('div', {'class': 'browse-movie-year'}).get_text()
            rating_gener = movie.find(
                'figcaption', {'class': 'hidden-xs hidden-sm'})
            rating = rating_gener.find('h4', {'class': 'rating'}).get_text()
            genres = rating_gener.find_all('h4', {'class': ''})
            picture_url = sanitize_img_link(
                movie.find('figure').img.attrs['src'])
            yifi_url = movie.find(
                'a', {'class': 'browse-movie-link'}).attrs['href']

            genre = ''
            for g in genres:
                genre += g.text + ", "

            genre = genre[:-2]

            data.append(Movie(title=title, description="", rating=rating, picture_url=picture_url, release_year=year, genre=genre,
                              language="", aviliable_quality="", likes=0, yifi_url=yifi_url, magnet_link=""))
        return data

    except AttributeError as e:
        return None


def get_movie_information(movie, movie_url):

    try:
        bs = BeautifulSoup(movie.read(), 'html.parser')

        movie_container = bs.find(
            'div', {'id': 'movie-content'}).find('div', {'class', 'row'})
        movie_info = movie_container.find('div', {'id': 'movie-info'})
        year_genre_title = movie_info.find('div', {'class': 'hidden-xs'})
        year_genre = year_genre_title.find_all('h2')
        movie_download_qualities = movie_info.find('p').find_all('a')
        likes_rating = movie_info.find(
            'div', {'class': 'bottom-info'}).find_all('div', {'class': 'rating-row'})

        title = year_genre_title.find('h1').get_text()
        release_year = year_genre[0].get_text()
        genre = year_genre[1].get_text()
        picture_url = sanitize_img_link(movie_container.find(
            'div', {'id': 'movie-poster'}).img.attrs['src'])
        yifi_url = movie_url

        aviliable_quality = []

        for quality in movie_download_qualities:
            aviliable_quality.append(quality.get_text())

        aviliable_quality = aviliable_quality[:-1]

        likes = likes_rating[0].find('span', {'id': 'movie-likes'}).get_text()
        rating = likes_rating[1].find('span').get_text()

        description = bs.find(
            'div', {'id': 'movie-sub-info'}).find_all('p')[1].get_text()
        language = ""
        magnet_link = ""

        return Movie(title=title, description=description, rating=rating, picture_url=picture_url, release_year=release_year, genre=genre,
                     language=language, aviliable_quality=aviliable_quality, likes=likes, yifi_url=yifi_url, magnet_link=magnet_link)

    except AttributeError as e:
        return None
