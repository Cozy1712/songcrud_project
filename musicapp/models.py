from turtle import title
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    
    
class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.IntegerField(max_length=10)
    likes = models.CharField(max_length=10)
    artiste_id = models.integerField(max_length=50)
    artiste = models.OneToOneField(Artiste,on_delete = models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length=50)
    song_id = models.IntegerField(max_length=50)
    song = models.OneToOneField(Song,on_delete = models.CASCADE)
