from django.shortcuts import render
from . models import Director, Pelicula

def verPeliculas(request, pk):
    context = Pelicula.objects.get(pk = Pelicula.director)
    
    return render(request, 'cineasta.html', context)
