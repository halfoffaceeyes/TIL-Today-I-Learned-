from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image=models.ImageField(blank=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)