from django.urls import path, re_path, include
from toys import views

urlpatterns = [
    path(r'^', include('drones.urls')),
]