from django import forms
class bike_form(forms.Form):
    th_brand = forms.CharField(label="Bike brand",max_length = 50)
    th_model= forms.CharField(label="Bike model",max_length = 50)
    th_category = forms.CharField(label="Bike category",max_length = 50)
    th_frame_size = forms.IntegerField(label="Bike frame size")
    th_used = forms.BooleanField()
    
    
    # brand = models.CharField(max_length=50)
    # model = models.CharField(max_length=50)
   # category = models.CharField(max_length=50)      # road bike, mountain, city(hybrid), 
   # frame_size = models.PositiveIntegerField()
   # used = models.BooleanField(default = False)