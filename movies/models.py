from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    synopsis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"