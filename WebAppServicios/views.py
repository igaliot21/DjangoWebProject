from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
from WebAppServicios.models import servicio
import datetime

# Create your views here.


def servicios(request):
    servicios = servicio.objects.all()
    return render(request, "WebAppServicios/Servicios.html", {"servicios": servicios})
