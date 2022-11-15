from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default = 2000)
    c_is_damaged = models.BooleanField(default = False)
    c_booked = "Booked"
    c_rented = "Rented"
    c_available = "Available"
    c_damaged = "Damaged"
    c_status_choices = [(c_booked, "Booked"),(c_rented, "Rented"),(c_available, "Available"),(c_damaged, "Damaged")]
    status = models.CharField(
        choices = c_status_choices,
        max_length = 50,
        default = c_available
        )
    location = models.CharField(max_length=50, default = 'Store garage')
    


    def __str__(self): 
        return self.make + ' ' + self.carmodel + ' ' + str(self.year)
    
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
    hasbooked = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.name + " " + self.address + " " + self.age
#test

class Order(models.Model):
    Ola = "Ola"
    Peter = "Peter"
    Adam = "Adam"
    customerlist= [(None, None),(Ola, "Ola"),(Peter, "Peter"), (Adam, "Adam")]
    Customer = models.CharField(choices = customerlist, max_length = 100, default = None)
    o_car = Car.make, Car.carmodel, Car.year
    o_status = Car.status
    o_id = None

    def str(self) -> str:
        return self.Customer + " " + self.o_car + " " + self.o_status
