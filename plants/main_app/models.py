from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField('Date Planted')
    description = models.TextField(max_length=500)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # New and updated plants redirect back to dashboard
    def get_absolute_url(self):
        return reverse('plants_list')

    @property
    def Get_age(self):
        calc_age = date.today().year - self.date.year
        date_stripped = str(calc_age).split(",", 1)[0]
        return date_stripped

    def save(self, *args, **kwargs):
        self.age = self.Get_age
        super(Plant, self).save(*args, **kwargs)
    # @property
    # def get_age(self):
    #     return relativedelta(self.birth_date.days, datetime.date.now()).years
     

    # def save(self, *args, **kwargs):
    #     self.unique_id = self.get_unique_id
    #     self.age = self.get_age
    #     super(Person, self).save(*args, **kwargs)

# class Collection(models.Model):