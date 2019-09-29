from django.db import models

# Create your models here.

class Bikes(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    category = models.CharField(max_length=50)      # road bike, mountain, city(hybrid), 
    frame_size = models.PositiveIntegerField()
    used = models.BooleanField(default = False)
    def __str__(self):
        return self.model
   
class Brand(models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Parts(models.Model):
    title = models.CharField(max_length=50)
    part_type = models.CharField(max_length=50)  #wheels, trims, chains, seats
    brand = models.CharField(max_length=50)
    bike_model = models.ManyToManyField(Bikes) 
    used = models.BooleanField()
    def __str__(self):
        return self.title

class Accesories(models.Model):
    title = models.CharField(max_length=50) 
    type = models.CharField(max_length=50) 
    brand = models.CharField(max_length=50) 
    bike_model = models.ManyToManyField(Bikes) 
    part_model = models.ManyToManyField(Parts) 
    def __str__(self):
        return self.title


