import enum


class Quality(enum.Enum):
    all = "all"
    low = 480
    standard_hd = 720
    full_hd = 1080
    ultra_hd = 2160
    three_D = "3D"


class Gener(enum.Enum):
    all = "all"
    action = "action"
    adventure = "adventure"
    animation = "animation"
    biography = "biography"
    comedy = "comedy"
    crime = "crime"
    documentary = "documentary"
    drama = "drama"
    family = "family"
    fantasy = "fantasy"
    film_noir = "film-noir"
    game_show = "game-show"
    history = "history"
    horror = "horror"
    music = "music"
    musical = "musical"
    mystery = "mystery"
    news = "news"
    reality_tv = "reality-tv"
    romance = "romance"
    sci_fi = "sci-fi"
    sport = "sport"
    talk_show = "talk-show"
    thriller = "thriller"
    war = "war"
    western = "western"


class Rating(enum.Enum):
    all = "all"
    one_plus = "1"
    two_plus = "2"
    three_plus = "3"
    four_plus = "4"
    five_plus = "5"
    six_plus = "6"
    seven_plus = "7"
    eight_plus = "8"
    nine_plus = "9"


class Year(enum.Enum):
    all = "0"
    y1900_1949 = "1900-1949"
    y1950_1969 = "1950-1969"
    y1970_1979 = "1970-1979"
    y1980_1989 = "1980-1989"
    y1990_1999 = "1990-1999"
    y2000_2009 = "2000-2009"
    y2010_2014 = "2010-2014"
    y2015_2018 = "2015-2018"
    y2019 = "2019"
    y2020 = "2020"
    y2021 = "2021"
    y2022 = "2022"
    y2023 = "2023"


class Language(enum.Enum):
    all = "all"
    english = "en"
    korean = "ko"
    russian = "ru"
    foreign = "foreign"


class Orderby(enum.Enum):
    latest = "latest"
    oldest = "oldest"
    featured = "featured"
    seeds = "seeds"
    peers = "peers"
    year = "year"
    rating = "rating"
    likes = "likes"
    rt_audience = "rt_audience"
    alphabetical = "alphabetical"
    downloads = "downloads"
