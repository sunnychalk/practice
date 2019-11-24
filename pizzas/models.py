from django.db import models

# Create your models here.
class Pizza(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, default="kukhftdgdkg")
	is_vegan = models.BooleanField(default=False)
	is_meat = models.BooleanField(default=False)
	price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	status = models.CharField(max_length=20, default="Active")

	class Meta:
		verbose_name = "Пицца"
		verbose_name_plural = "Пиццы"

	def __str__(self):
		return self.name



	
