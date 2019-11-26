import logging
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def get_brand(url):
    parsed = urlparse(url)
    if parsed.netloc:
        return parsed.netloc.split('.')[1]
    else:
        logger.error('Invalid URL: Unable to find brand.\nCopy link directly from browser.')

def scrape(url):
    brand = get_brand(url) # TODO: Notify client of invalid URL
    print("Brand: {}".format(brand))

    data = requests.get(url)
    page = BeautifulSoup(data.text, 'html.parser')

    if brand == 'jcrew':
        logger.info('Scraping J.Crew page...')
        print("Looking at {}".format(page.title.string))
        reg_price = page.find_all(class_='is-price')[0]
        print("Price: {}".format(reg_price.string))






