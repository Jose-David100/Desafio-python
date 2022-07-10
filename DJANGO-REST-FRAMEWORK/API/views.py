from rest_framework import serializers
from .models import PlacasPatentes
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect



# Serializacion del model
class PatenteSerializers(serializers.ModelSerializer):
	class Meta:
		model = PlacasPatentes
		fields = '__all__'


# vistas de la api
class PatentesList(APIView):
	def get(self, request):
		placas = PlacasPatentes.objects.all()
		data = PatenteSerializers(placas, many=True).data
		return Response(data)

class PatentesDetail(APIView):
	def get(self, request, pk):
		placas = get_object_or_404(PlacasPatentes, pk=pk )
		data = PatenteSerializers(placas).data
		return Response(data)

class PatentesDetailName(APIView):
	def get(self, request, patente):
		placas = get_object_or_404(PlacasPatentes, patente=patente )
		data = PatenteSerializers(placas).data
		return Response(data)

class CrearPatentes(View):
	def get(self, request):

		datos = []

		with open("/Users/Jose David/Desktop/Desafio Python/ApiDatos/DJANGO-REST-FRAMEWORK/API/abc.txt") as fname:
			lineas = fname.readlines()
			for linea in lineas:

				datos.append(linea.strip('\n'))

				patente = PlacasPatentes()
				patente.id = str(datos.index(linea.strip('\n')) + 1)
				patente.patente = linea.strip('\n')
				patente.save()

		return redirect('/')
