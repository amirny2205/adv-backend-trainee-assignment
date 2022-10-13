from django.db import models

# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    main_photo = models.CharField(max_length=200, null=True)
    photos = models.JSONField(null=True)
    price = models.IntegerField()
