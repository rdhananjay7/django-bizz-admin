from django.db import models
from datetime import datetime


class Team(models.Model):

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_employed = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
