import requests
from bs4 import BeautifulSoup
import urllib

url = 'http://httpstat.us/500'


def download(url, num_retries=2):
    print('Downloading:', url)
    try:
        html = requests.get(url).content
        print(html)
    except requests as e:
        print('Download error:', requests.status_codes)
        html = None
        if num_retries > 0:
            if hasattr(e, requests.status_codes) and 500 <= requests.status_codes < 600:
                #   recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    return html

download(url)