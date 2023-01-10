from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from models.models import Movie
from helpers.img_link_sanitizer import sanitize_img_link


def get_html_result(url, header):
    try:
        req = Request(
            url,
            data=None,
            headers=header
        )
        html_content = urlopen(req)
        return html_content

    except HTTPError as e:
        print(e)
        return None

    except URLError as e:
        print('The server could not be found!')
        return None


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
            geners = rating_gener.find_all('h4', {'class': ''})
            picture_url = sanitize_img_link(
                movie.find('figure').img.attrs['src'])
            yifi_url = movie.find(
                'a', {'class': 'browse-movie-link'}).attrs['href']

            gener = ''
            for g in geners:
                gener += g.text + ", "

            gener = gener[:-2]

            data.append(Movie(title=title, description="", rating=rating, picture_url=picture_url, release_year=year, gener=gener,
                              language="", aviliable_quality="", likes=0, yifi_url=yifi_url, magnet_link=""))
        return data

    except AttributeError as e:
        return None


def get_movie_information(movie):
    print(movie)
    pass


def search_movie(url, header):
    search_result = get_html_result(url, header)

    if (search_result):
        movies = get_movies_from_result(search_result)

        if (movies):

            return movies

    return None


url = "https://yts.mx/"
header = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"}

search_results = search_movie(
    url+"browse-movies/car/all/all/0/latest/0/en", header)

get_movie_information(get_html_result(search_results[0].yifi_url, header))
