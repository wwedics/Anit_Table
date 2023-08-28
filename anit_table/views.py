from django.shortcuts import render
from .models import *

# Create your views here.

def anmtn(req):
    return render(req, "pages/anmtn.html")

def analem(req):
    return render(req, "pages/analem.html")