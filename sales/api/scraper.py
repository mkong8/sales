import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    html = browser.page_source
    page = BeautifulSoup(html, 'html.parser')

    if brand == 'jcrew':
        logger.info('Scraping J.Crew page...')
        print("Looking at {}".format(page.title.string))
        reg_price = page.find_all(class_='is-price')[0]
        print("Price: {}".format(reg_price.string))






