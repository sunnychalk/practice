from django.contrib import admin
from pizzas.models import Pizza
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']

admin.site.register(Pizza, PizzaAdmin)