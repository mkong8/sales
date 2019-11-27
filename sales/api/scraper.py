import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from .models import Item

LOGGER = logging.getLogger(__name__)
BLANK = ' '

def get_brand(url):
    parsed = urlparse(url)
    if parsed.netloc:
        return parsed.netloc.split('.')[1]
    else:
        LOGGER.error('Invalid URL: Unable to find brand.\nCopy link directly from browser.')

def scrape(url):
    brand = get_brand(url) # TODO: Notify client of invalid URL
    print("Brand: {}".format(brand))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    html = browser.page_source
    page = BeautifulSoup(html, 'html.parser')

    if brand == 'jcrew':
        LOGGER.info('Scraping J.Crew page...')
        product = page.find_all(class_='product__name')[0].string
        print("Looking at", product)
        if not product:
            LOGGER.error('Invalid item: no product name found')

        reg_price = page.find_all(class_='is-price')[0].string
        sale_price = page.find_all(class_='sale-price')[0].string
        price = sale_price if sale_price != BLANK else reg_price
        price = float(price.strip('$'))

        print("Price: ", price)
        if not price:
            LOGGER.error('Invalid item: no pricing found')

        return product, price

        






