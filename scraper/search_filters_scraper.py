from bs4 import BeautifulSoup
import json
import os


def update_filters(page_html, file_path):

    if (page_html):
        filters = scrape_filters(page_html)

        if (filters):

            for filter in filters:

                fill_json(os.path.join(file_path,
                          filter.lower()+".json"), filters[filter])


def scrape_filters(html):

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        data = {}
        search_filters = bs.find('div', {'id': 'main-search-fields'})
        filters = search_filters.find_all(
            'div', {'class': 'selects-container'})

        for filter in filters:
            key = filter.find('p').get_text()[:-1]
            values = filter.find('select').find_all('option')
            data[key] = []
            for filter_value in values:
                data[key].append(filter_value.attrs['value'])

        return data

    except AttributeError as e:
        print(e)
        return None


def fill_json(file_name, data):
    with open(file_name, "w") as fp:
        json.dump(data, fp, indent=4)
