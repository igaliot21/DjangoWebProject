from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
import datetime

# Create your views here.


def home(request):
    return render(request, "WebAppProject/Home.html")


def tienda(request):
    return render(request, "WebAppProject/Tienda.html")


def blog(request):
    return render(request, "WebAppProject/Blog.html")


def contacto(request):
    return render(request, "WebAppProject/Contacto.html")
