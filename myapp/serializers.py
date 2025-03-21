from rest_framework import serializers
from myapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["name", "age", "department", "salary", "hire_date", "projects", "id"]