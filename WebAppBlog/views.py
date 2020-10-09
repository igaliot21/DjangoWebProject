from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
from WebAppBlog.models import post
from WebAppBlog.models import categoria
import datetime

# Create your views here.


def blog(request):
    posts = post.objects.all()
    return render(request, "WebAppBlog/Blog.html", {"posts": posts})


def categoria(request, categoria_id):
    #categoria_filter = categoria.objects.get(id=categoria_id)
    posts = post.objects.filter(categorias=categoria_id)
    return render(request, "WebAppBlog/Categoria.html", {"categoria": categoria_id, "posts": posts})
