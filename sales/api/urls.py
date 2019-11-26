from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create-user/', views.create_user, name='create_user'),
    path('item/<item_id>', views.get_item, name='get_item'),
    path('add-item/', views.add_item, name='add_item')
]