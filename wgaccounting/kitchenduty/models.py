from django.db import models
from persons.models import Inhabitant

class ShiftPeriod(models.Model):
	start = models.DateField()
	end = models.DateField()
	
	def __str__(self):
		return f'From {self.start} to {self.end}'
	
class Roster(models.Model):
	kitchen_lord = models.ForeignKey(Inhabitant, on_delete=models.CASCADE, related_name='kitchen_lord')
	shift = models.ForeignKey(ShiftPeriod, on_delete=models.CASCADE, related_name='shift')
	duty_completed = models.BooleanField()
	
	def __str__(self):
		return f'{self.kitchen_lord.username} responsible for {self.shift.start} to {self.shift.end}, completion status = {self.duty_completed}'
	
