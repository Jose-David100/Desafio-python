from django.db import models

# Create your models here.

class PlacasPatentes(models.Model):
	id = models.IntegerField(unique=True, primary_key=True)
	patente = models.CharField(max_length=7, unique=True)

	def __str__(self):
		return str(self.patente)

	class Meta:
		ordering = ['id']