from django.db import models
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
