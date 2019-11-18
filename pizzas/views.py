from django.shortcuts import render
from pizzas.models import Pizza
from django.views.generic.list import ListView


# Create your views here.
class PizzaList(ListView):
	model = Pizza
	template_name = 'pizza_list.html'

	def get_contex_data(self, **kwargs):
		context = super(PizzaList, self).get_contex_data(**kwargs)
		context['pizzas'] = Pizza.objects.all()
		return context
