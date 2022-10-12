from email.policy import default
from django.db import models
from datetime import date

class Director(models.Model):
    id_director = models.AutoField(primary_key=True,blank= False, null=False)
    name = models.CharField(max_length=50,blank= False, null=False)
    last_name = models.CharField(max_length=50 ,blank= False, null=False)
    born_date = models.DateField(default=date.today)
    city_born = models.CharField(max_length=20,blank= False, null=False)
    nacionalidad = models.CharField(max_length=20, blank= False, null=False)
    
    def __str__(self):
        return self.name
    
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True,blank= False, null=False)
    name = models.CharField(max_length=50,blank= False, null=False)
    date = models.DateField(default=date.today)
    productora = models.CharField(max_length=50, blank= False, null=False)
    genero = models.CharField(max_length=20, blank= False, null=False)
    director = models.ForeignKey(Director, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name