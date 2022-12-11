from django.urls import path
from peluqueriamimapp import views

urlpatterns = [

    path('',views.home,name="Inicio"),
    path('productos',views.productos,name="Productos"),
    path('contacto',views.contacto,name="Contacto"),

]