from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    name = ["Rajendra", "naveen", "kiran"]
    return render(request, 'home.html', {'name': name})


def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    s = num1+num2
    return render(request, 'result.html', {'result': s})
