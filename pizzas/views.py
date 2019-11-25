from django.shortcuts import render
from django import template
from pizzas.models import Pizza, InstancePizza, Order
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from pizzas.forms import IncreasePriceForm, PizzaForm
from django.db.models import F


# Create your views here.
class PizzaList(ListView):
	model = Pizza
	template_name = 'pizza_list.html'
	
	def get_context_data(self, **kwargs):
		context = super(PizzaList, self).get_context_data(**kwargs)
		context['pizza_amount'] = Pizza.objects.all().count()
		context['more_than_40'] = Pizza.objects.filter(price__gt=40).filter(status="Active").values('name')
		context['values_list'] = Pizza.objects.all().values_list('name')
		return context


class IncreasePrice(FormView):
	model = Pizza
	form_class = IncreasePriceForm
	template_name = 'increase_price.html'
	success_url = '/'
	queryset = Pizza.objects.all()

	def post(self, request, *args, **kwargs):
		increase_price_form = self.form_class(request.POST)
		self.object = Pizza.objects.all().update(price=F('price')+100)
		return super().post(request, *args, **kwargs)


class AddPizzaView(FormView):
	template_name = 'core.html'
	form_class = PizzaForm
	success_url = '/pizzas/'

	def form_valid(self, form):
		print('form.cleaned_data:', form.cleaned_data)
		pizza = Pizza.objects.get(id=form.cleaned_data.get('pizza_id'))
		count = form.cleaned_data.get('count')
		instance_pizza = pizza.create_instance_pizza(count)
		order, created = Order.objects.get_or_create(user=self.request.user, full_price=0)
		order.pizzas.add(instance_pizza)
		print ('instance_pizza', instance_pizza)
		return super().form_valid(form)





	

