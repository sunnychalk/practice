from django.urls import path
from django.conf.urls import url, include
from pizzas.views import PizzaList, IncreasePrice, AddPizzaView, CoreTemplateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^pizza_list/$', PizzaList.as_view(), name='pizza-list'),
    url(r'^increase_price/$', IncreasePrice.as_view(), name='increase-price'),
    url(r'^pizzas/$', CoreTemplateView.as_view()),
    url(r'^add_pizza/$', AddPizzaView.as_view()),
]

