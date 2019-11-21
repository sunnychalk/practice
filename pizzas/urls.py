from django.urls import path
from django.conf.urls import url, include
from pizzas.views import PizzaList, IncreasePrice
from django.views.generic.list import ListView


urlpatterns = [
    url(r'^pizza_list/$', PizzaList.as_view(), name='pizza-list'),
    url(r'^increase_price/$', IncreasePrice.as_view(), name='increase-price'),
]

