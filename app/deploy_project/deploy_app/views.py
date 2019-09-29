from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

   firstapptext = "Hi! "
   context = {'firstapptext': firstapptext  } 

   return render(request, 'index.html', context)