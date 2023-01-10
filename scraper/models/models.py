from typing import List


class Movie():

    def __init__(self, title: str, description: str, rating: float, genre: str, picture_url: str, release_year: int,
                 language: str, aviliable_quality: List[str], likes: float, yifi_url: str, magnet_link: str):

        self.title = title
        self.description = description
        self.rating = rating
        self.genre = genre
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
        print("YIFI url: " + self.yifi_url)
        print("Picture: " + self.picture_url)
        print("Year: " + str(self.release_year))
        print('\n')
        print("Aviliable qualities: " + str(self.aviliable_quality))
        print("Rating: " + str(self.rating))
        print("Gener: " + self.genre)
        print("Language: " + self.language)
        print("Likes: " + str(self.likes))
        print("Mangent link: " + self.magnet_link)
        print('\n')
        print("Description: " + self.description)
