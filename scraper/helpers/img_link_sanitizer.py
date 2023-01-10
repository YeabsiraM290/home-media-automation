

def sanitize_img_link(link):
    splited_links = link.split("/")
    splitted_clean_url = splited_links[splited_links.index("https:"):]
    clean_url = ''
    for link_part in splitted_clean_url:
        clean_url += link_part+"/"

    return clean_url[:-1]


sanitize_img_link("/cdn-cgi/mirage/e24b7060fb695b3a71758e7e66d60e58e9ccf8d3ccbaf4880beb459f73e780e1/1280/https://img.yts.mx/assets/images/movies/the_red_book_ritual_2022/medium-cover.jpg")