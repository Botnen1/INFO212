from django.contrib import admin
from .models import Car
from .models import Employee
from .models import Customer
from .models import Order

admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Order)