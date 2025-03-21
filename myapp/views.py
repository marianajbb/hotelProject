import logging

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


def employee_list_view(request):  # Rename the view
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list_api(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def employee_create_api(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_detail_api(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def employee_update_api(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def employee_delete_api(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)