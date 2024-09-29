from django.urls import path  
from .views import flight_list, flight_create  

urlpatterns = [  
    path('', flight_list, name='flight_list'),  
    path('create/', flight_create, name='flight_create'),  
]