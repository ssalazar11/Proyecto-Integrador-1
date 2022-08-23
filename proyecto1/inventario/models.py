from django.db import models

# Create your models here.

class usuario(models.Model):
    name=models.CharField(max_length=60)
    age=models.IntegerField()