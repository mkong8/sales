import json
from django.http import HttpResponse

from .models import Item
from .scraper import scrape


def index(request):
    return HttpResponse("Welcome to Sales API")

def login(request):
    return HttpResponse('login')

def create_user(request):
    return HttpResponse('Create new user')

def get_item(request, item_id):
    return HttpResponse('Get item {}'.format(item_id))

def add_item(request):
    item = Item()
    url = json.loads(request.body)['url']
    brand, product, price = scrape(url)
    item.brand = brand
    item.name = product
    item.price = price
    item.url = url
    item.save()

    return HttpResponse('Item {} costs ${}'.format(product, price))
