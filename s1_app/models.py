
from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    salary = models.IntegerField()
    birth_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
