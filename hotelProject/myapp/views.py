from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .mongo_utils import create_employee, read_employee, update_employee, delete_employee, db
from bson.objectid import ObjectId

def employee_list(request):
    employees = list(db.employees.find())
    for employee in employees:
        employee['id'] = str(employee['_id'])
    return render(request, 'employee_list.html', {'employees': employees})

def employee_list_api(request):
    employees = list(db.employees.find())
    for employee in employees:
        employee['id'] = str(employee['_id'])
    return JsonResponse(employees, safe=False)

def employee_create_api(request):
    if request.method == 'POST':
        employee_data = {
            "firstName": request.POST['firstName'],
            "lastName": request.POST['lastName'],
            "age": request.POST['age'],
            "salary": request.POST['salary'],
        }
        create_employee(employee_data)
        return JsonResponse(employee_data, status=201)

def employee_update_api(request, employee_id):
    employee_id = ObjectId(employee_id)
    if request.method == 'PUT':
        update_data = {
            "firstName": request.POST['firstName'],
            "lastName": request.POST['lastName'],
            "age": request.POST['age'],
            "salary": request.POST['salary'],
        }
        update_employee(employee_id, update_data)
        return JsonResponse(update_data)

def employee_delete_api(request, employee_id):
    employee_id = ObjectId(employee_id)
    if request.method == 'DELETE':
        delete_employee(employee_id)
        return JsonResponse({'status': 'deleted'})