from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from myapp.models import Employee  # Import Employee model

class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
