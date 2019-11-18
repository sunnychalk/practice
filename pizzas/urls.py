from django.urls import path
from django.conf.urls import url, include
from pizzas.views import PizzaList
from django.views.generic.list import ListView


urlpatterns = [
    url(r'^pizza_list/$', PizzaList.as_view(), name='pizza-list'),
]

