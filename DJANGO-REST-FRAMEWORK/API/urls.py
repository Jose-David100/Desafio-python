from django.urls import path

from .views import PatentesList, PatentesDetail, CrearPatentes, PatentesDetailName
urlpatterns = [
    # LOGIN
    
    # DJANGO_RESTFRAMWORK
    path('patentes/list/', PatentesList.as_view(), name = "list"),
    path('patente/<int:pk>/', PatentesDetail.as_view(), name = "detail"),
    path('patente/<str:patente>/', PatentesDetailName.as_view(), name = "detailName"),
    path('crear_patente/', CrearPatentes.as_view(), name = "crear"),

]