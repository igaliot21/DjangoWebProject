from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
from WebAppBlog.models import categoria, post
import datetime

# Create your views here.


def blog(request):
    posts = post.objects.all()
    return render(request, "WebAppBlog/Blog.html", {"posts": posts})
