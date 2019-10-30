from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes, Parts, Accessories
from .forms import bike_form, part_form, accessory_form 
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
   queryset = Bikes.objects.all()
   context = {'queryset': queryset  } 
   return render(request, 'index.html', context)

def parts(request):
   queryset = Parts.objects.all()
   context = {'queryset': queryset  } 
   return render(request, 'parts.html', context)

def accessories(request):
   queryset = Accessories.objects.all()
   context = {'queryset': queryset  } 
   return render(request, 'accessories.html', context)

def bikeform(request):
   if request.method == 'POST': 
      form=bike_form(request.POST)
      if form.is_valid(): 
         form.save()
         return redirect('home')
   else: 
      form = bike_form()
   return render(request, 'bikeform.html', {"form":form})

def partform(request):
   if request.method == 'POST': 
      form=part_form(request.POST)
      if form.is_valid(): 
         form.save()
         return redirect('parts')
   else: 
      form = part_form()
   return render(request, 'partform.html', {"form":form})

def accessoryform(request):
   if request.method == 'POST': 
      form=accessory_form(request.POST)
      if form.is_valid(): 
         form.save()
         return redirect('accessories')
   else: 
      form = accessory_form()
   return render(request, 'accessoryform.html', {"form":form})

@csrf_exempt
def log(request):
   temp = request.body.decode('utf-8')
   print(temp)
   with open('log.txt', 'a') as f:
      f.write("{}\n".format(temp))
   return HttpResponse(temp)

