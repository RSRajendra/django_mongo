import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Destination
# Create your views here.


def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'destination': dest})


def favicon(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imagepath = os.path.join(BASE_DIR, 'static/images/about.jpg')
    img = open(imagepath)
    response = FileResponse(img)
    return HttpResponse(request, imagepath)
