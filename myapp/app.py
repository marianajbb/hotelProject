from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from myapp.models import Employee
from myapp.schema import employees_schema, employee_schema
from myapp.extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/admco/Downloads/projects/hotelProject/instance/employee.db'
db.init_app(app)

migrate = Migrate(app, db)

# Import your routes (views) here.
# Example:


@app.route('/')
def index():
    return render_template('employee_list.html')

@app.route('/employees', methods=['GET'])
def get_employees():
    all_employees = Employee.query.all()
    result = employees_schema.dump(all_employees)
    return jsonify(result)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = employee_schema.load(request.json)
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(employee_schema.dump(new_employee)), 201 # Corrected line

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    return jsonify(employee_schema.dump(employee)) # Corrected line

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    updated_employee = employee_schema.load(request.json, instance=employee)
    db.session.commit()
    return jsonify(employee_schema.dump(updated_employee)) # Corrected line

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)