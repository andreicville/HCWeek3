from django.contrib import admin
from .models import Bikes, Parts, Accessories
# Register your models here.

admin.site.register(Bikes)
admin.site.register(Parts)
admin.site.register(Accessories)
