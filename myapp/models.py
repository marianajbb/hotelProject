from flask_sqlalchemy import SQLAlchemy
from myapp.extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    department = db.Column(db.String(100))
    salary = db.Column(db.Float)
    hire_date = db.Column(db.Date)
    projects = db.Column(db.String) #Store JSON as string.

    def __repr__(self):
        return f'<Employee {self.name}>'