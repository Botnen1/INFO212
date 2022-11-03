from rest_framework import serializers
from .models import Car, Customer, Employee, Order

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel'] 
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'address', 'branch']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'age']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['Customer', 'id', 'car', 'status']