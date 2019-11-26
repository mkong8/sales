from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Sales API")

def login(request):
    return HttpResponse('login')

def create_user(request):
    return HttpResponse('Create new user')

def get_item(request, item_id):
    return HttpResponse('Get item {}'.format(item_id))


def add_item(request):
    return HttpResponse('Add item')
