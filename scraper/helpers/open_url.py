from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

def open_url(url, header):
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
