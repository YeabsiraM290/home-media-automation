def sanitize_img_link(link):
    splited_links = link.split("/")
    splitted_clean_url = splited_links[splited_links.index("https:"):]
    clean_url = ''
    for link_part in splitted_clean_url:
        clean_url += link_part+"/"

    return clean_url[:-1]
