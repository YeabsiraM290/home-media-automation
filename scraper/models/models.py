from typing import List

from enums.custome_types import Quality


class Movie():

    def __init__(self, title: str, description: str, rating: float, gener: str, picture_url: str, release_year: int,
                 language: str, aviliable_quality: List[Quality], likes: float, yifi_url: str, magnet_link: str):

        self.title = title
        self.description = description
        self.rating = rating
        self.gener = gener
        self.picture_url = picture_url
        self.release_year = release_year
        self.language = language
        self.aviliable_quality = aviliable_quality
        self.likes = likes
        self.yifi_url = yifi_url
        self.magnet_link = magnet_link

    def print(self):
        print("*" * 30)
        print("Title: " + self.title)
        print("Rating: " + str(self.rating))
        print("Year: " + str(self.release_year))
        print("Gener: " + self.gener)
        print("Language: " + self.language)
        print("Likes: " + str(self.likes))
        print("Picture: " + self.picture_url)
        print("YIFI url: " + self.yifi_url)
        print("Mangent link: " + self.magnet_link)
