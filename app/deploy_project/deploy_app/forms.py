from django.forms import ModelForm
from django import forms
from .models import Bikes, Parts, Accessories

class bike_form(ModelForm):
    class Meta: 
        model = Bikes
        fields = ['brand', 'model', 'category','frame_size', 'used']
class part_form(ModelForm):
    class Meta: 
        model = Parts
        fields = ['title', 'part_type', 'brand','bike_model', 'used']
class accessory_form(ModelForm):
    class Meta: 
        model = Accessories
        fields = ['title', 'accessory_type', 'brand','bike_model', 'part_model']