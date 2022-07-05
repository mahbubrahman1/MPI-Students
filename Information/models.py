from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    reg = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name