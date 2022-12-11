from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "peluqueriamimapp/home.html")

def productos(request):
    return render(request, "peluqueriamimapp/productos.html")

def contacto(request):
    return render(request, "peluqueriamimapp/contacto.html")

