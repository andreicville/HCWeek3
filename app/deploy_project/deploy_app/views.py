from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
from .forms import bike_form
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
   queryset = Bikes.objects.all()
   context = {'queryset': queryset  } 
   return render(request, 'index.html', context)

def bikeform(request):
   if request.method == 'POST': 
      form=bike_form(request.POST)
      if form.is_valid(): 
         form.save()
         return redirect('home')
   else: 
      form = bike_form()
   return render(request, 'bikeform.html', {"form":form})


