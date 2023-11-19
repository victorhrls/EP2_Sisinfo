from django.db import models

# Create your models here.


from django.db import models
from django.conf import settings
from datetime import datetime


class Book(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    capa_url = models.URLField(max_length=200, null=True)
    categoria = models.CharField(max_length=255 , null = True)

    def __str__(self):
        return f'{self.name}({self.categoria})({self.release_year})'

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class List(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.name} by {self.author}'
