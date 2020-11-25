from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
