from django.urls import path
from .views import index, add_fruit
urlpatterns = [
    path('', index, name='index'),
    path('add_fruit/', add_fruit, name='add_fruit'),
]