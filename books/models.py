from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  image = models.URLField()
  rating = models.FloatField(null=True)
  views = models.IntegerField(null=True)
  description = models.TextField()