from django.urls import path 
from . import views
urlpatterns = [ 
    path('cineasta/<int:pk>', views.verPeliculas, name='cineasta'),           
    ]