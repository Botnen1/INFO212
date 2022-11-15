from .models import Car
from .models import Employee
from .models import Customer
from .models import Order
from rest_framework.response import Response
from .serializers import CarSerializer
from .serializers import EmployeeSerializer
from .serializers import CustomerSerializer
from .serializers import OrderSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view


"""
Min kode:
"""
@api_view(['GET'])
def get_customer(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(Customer, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_customer(request):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_employee(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(Employee, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['PUT'])
def update_employee(request):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PATCH'])
def order_car(request, customer_id, car_id):
    customer = Customer.objects.get(pk=customer_id)
    car = Car.object.get(pk=car_id)
    if customer.hasbooked == False and car.status == "Available":
        customer.hasbooked = True
        car.status = "Booked"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    

@api_view(['CANCEL-ORDER-CAR'])
def cancel_order_car(request, customer_id, car_id):
    customer = Customer.objects.get(pk=customer_id)
    car = Car.object.get(pk=car_id)
    if customer.hasbooked == True and car.status == "Booked":
        customer.hasbooked = False
        car.status = "Available"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['RENT-CAR'])
def rent_car(request, customer_id, car_id):
    customer = Customer.objects.get(pk=customer_id)
    car = Car.object.get(pk=car_id)
    if customer.hasbooked == True and car.status == "Booked":
        car.status = "Rented"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['RETURN-CAR'])
def return_car(request, customer_id, car_id):
    customer = Customer.objects.get(pk=customer_id)
    car = Car.object.get(pk=car_id)
    if customer.hasbooked == True and car.status == "Rented":
        if Car.c_is_damaged != False:
            Car.status = "Damaged"
        else:
            Car.status = "Available"

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)