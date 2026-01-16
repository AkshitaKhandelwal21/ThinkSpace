from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.name