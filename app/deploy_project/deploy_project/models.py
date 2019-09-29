from django.db import models

# Create your models here.

class Bikes(models.Model):
    ROAD = 'Road Bike'
    MOUNTAIN = 'Mountain Bike'
    CITY = 'City/Hybrid Bike'
    FOLDING = 'Folding Bike'
    BMX = 'BMX Bike'
    TRIATHLON = 'Trithlon Bike'
    KIDS = 'Kids Bike'
    CRUISER = 'Beach Cruiser Bike'
    BIKE_TYPES = [
        (ROAD, _('Best for roads')),
        MOUNTAIN, _('Best for forests, hills')),
        CITY, _('Best for towns and cities')),
        FOLDING, _('Easy to transfer')),
        BMX, _('BMX Bike')),
        TRIATHLON, _('Trithlon Bike')),
        KIDS, _('Kids Bike')),
        CRUISER, _('Beach Cruiser Bike'))
    ]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices = BIKE_TYPES)      # road bike, mountain, city(hybrid), 
    frame_size = PositiveIntegerField()
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


