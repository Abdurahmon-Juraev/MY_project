from django.core.signals import request_started
from django.shortcuts import render


def home(request):

    data = {
        "name": "John"
    }
    return render(request,'index.html',data)


def contact(request):

    data = {
        "name": "John"
    }
    return render(request,'about.html',data)

def blog(request):

    data = {
        "name": "John"
    }
    return render(request,'blog.html',data)

def services(request):

    deta ={
        "nama":"John"
    }
    return render(request,'services.html',deta)