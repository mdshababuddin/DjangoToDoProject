from django.db import models
from datetime import date

# Create your models here.
class List(models.Model):
	date = models.DateField(default=date.today)
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item + ' | ' + str(self.completed)
