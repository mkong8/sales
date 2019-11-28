import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BLANK = ' '

def get_brand(url):
    parsed = urlparse(url)
    if parsed.netloc:
        return parsed.netloc.split('.')[1]
    else:
        print('Invalid URL: Unable to find brand.\nCopy link directly from browser.')

def scrape(url):
    brand = get_brand(url) # TODO: Notify client of invalid URL

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    html = browser.page_source
    page = BeautifulSoup(html, 'html.parser')

    if brand == 'jcrew':
        print('Scraping J.Crew page...')
        product = page.find_all(class_='product__name')[0].string
        print("Looking at", product)
        if not product:
            print('Invalid item: no product name found')

        reg_price = page.find_all(class_='is-price')[0].string
        sale_price = page.find_all(class_='sale-price')[0].string
        price = sale_price if sale_price != BLANK else reg_price

        print("Price: ", price)
        if not price:
            print('Invalid item: no pricing found')

        return brand, product, price

if __name__ == '__main__':
    print("Running webscraper...")
    try:
        filename = sys.argv[1]
    except:
        sys.exit("No target file specified")

    items = {}

    with open(filename) as urls:
        for url in urls:
            brand, product, price = scrape(url)
            if brand not in items:
                items[brand] = []
            items[brand].append("- {}: {}".format(product, price))

    print('\n\n\n!!!======== SALES ========!!!\n')
    for brand in items:
        print("{}:".format(brand.upper()))
        print('\n'.join(items[brand]))

    print('\n\n\n')