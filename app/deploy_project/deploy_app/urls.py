from django.urls import path

from . import views

app_name = 'deploy_project'
urlpatterns = [
    path('bikelist/', views.bikeform, name="bikeform"),
]