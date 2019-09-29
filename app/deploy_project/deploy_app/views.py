from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
# Create your views here.

def index(request):
   qweryset = Bikes.objects.all()
   
   context = {'qweryset': qweryset  } 

   return render(request, 'index.html', context)