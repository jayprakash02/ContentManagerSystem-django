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
    nameA = models.CharField(max_length=50,default='A')
    nameB = models.CharField(max_length=50,default='B')
    nameC = models.CharField(max_length=50,default='C')
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()

class Barchart(models.Model):
    data = ArrayField(ArrayField(
            models.IntegerField(),
            size=8,
        ))