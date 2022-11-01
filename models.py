from unittest.util import _MAX_LENGTH
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    

    def __str__(self): 
        return self.make + ' ' + self.carmodel
    
class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name + " " + self.address + " " + self.branch

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name + " " + self.address + " " + self.age