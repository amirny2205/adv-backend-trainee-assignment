from django.db import models

# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photos = models.JSONField()
    price = models.IntegerField()
