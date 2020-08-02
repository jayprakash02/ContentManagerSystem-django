from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Dashboard(models.Model):
    head = models.CharField(max_length=50)
    counter = models.IntegerField()

class Table(models.Model):
    name = models.CharField(max_length=50)
    office = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    salary = models.IntegerField()

class Piechart(models.Model):
    label = models.CharField(max_length=50,default='')
    data = models.IntegerField(default=0)

class Barchart(models.Model):
    data = models.IntegerField(default=0)