from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    genre_choice = [
        ('Comedy','Comedy'),
        ('Fantasy','Fantasy'),
        ('Romance','Romance'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description = models.TextField()
    genre=models.CharField(max_length=50,choices=genre_choice,default = 'Comedy')
    score=models.FloatField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.CharField(max_length=100)
