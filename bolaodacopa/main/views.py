from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def login(request):
    return render(request, 'main/login.html')

def index(request):
    return render(request, 'main/index.html')
