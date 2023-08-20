from django.db import models
from django.urls import reverse
from datetime import date
# from django.contrib.auth.models import User

# Create your models here.

# Not yet migrated
class Plant(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField('Date Planted')
    description = models.TextField(max_length=500)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# class Collection(models.Model):