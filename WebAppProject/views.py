from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
from WebAppServicios.models import servicio
import datetime

# Create your views here.


def home(request):
    return render(request, "Home.html")


def servicios(request):
    servicios = servicio.objects.all()
    return render(request, "Servicios.html", {"servicios": servicios})


def tienda(request):
    return render(request, "Tienda.html")


def blog(request):
    return render(request, "Blog.html")


def contacto(request):
    return render(request, "Contacto.html")
