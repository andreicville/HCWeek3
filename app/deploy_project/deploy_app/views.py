from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
from .forms import bike_form
# Create your views here.

def index(request):
   qweryset = Bikes.objects.all()
   
   context = {'qweryset': qweryset  } 

   return render(request, 'index.html', context)

def form(request):
   form=bike_form()
   return render(request, 'bikeform.html', {"form":form})
