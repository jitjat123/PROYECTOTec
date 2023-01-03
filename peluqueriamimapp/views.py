from django.shortcuts import render, HttpResponse
from producto.models import producto

# Create your views here.

def home(request):
    return render(request, "peluqueriamimapp/home.html")


def contacto(request):
    return render(request, "peluqueriamimapp/contacto.html")

