from django.db import models

# Create your models here.
class User_Info(models.Model):
    username = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)


class MovieDetails(models.Model):
    
    movie_name = models.CharField(max_length=255)
    theatre_name =models.CharField(max_length=255)
    theatre_location = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.movie_name