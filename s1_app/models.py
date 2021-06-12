
from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    salary = models.IntegerField()
    birth_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RegData(models.Model):
    name = models.CharField(max_length=100, )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name

    def is_valid(self):
        pass


