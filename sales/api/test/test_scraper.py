import pytest
from .. import scraper

def test_get_brand_valid():
    url = 'https://www.test.com'
    brand = scraper.get_brand(url)
    assert brand == 'test'

def test_get_brand_invalid():
    url = 'www.test.com'
    brand = scraper.get_brand(url)
    assert brand == None

def test_scrape_jcrew():
    url = 'https://www.jcrew.com/p/mens_category/coats_and_jackets/bomber_jacket/harrington-jacket/H6538?color_name=warm-indigo'
    product, price = scraper.scrape(url)
    assert product == "Harrington jacket"
    assert price == 178.00

