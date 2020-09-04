from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return HttpResponse("Home")


def servicios(request):
    return HttpResponse("Servicios")


def tienda(request):
    return HttpResponse("Tienda")


def blog(request):
    return HttpResponse("Blog")


def contacto(request):
    return HttpResponse("Contacto")
