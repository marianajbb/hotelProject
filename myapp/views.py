# from flask import jsonify, request
# from models import Employee, db, app  # Import db from models.py
# from schemas import employee_schema, employees_schema #Import the schemas
#
# # Assuming you have 'app' defined in your main app.py file.
# # If not, you'll need to create it.
#
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     all_employees = Employee.query.all()
#     result = employees_schema.dump(all_employees)
#     return jsonify(result)
#
# @app.route('/employees', methods=['POST'])
# def add_employee():
#     new_employee = employee_schema.load(request.json)
#     db.session.add(new_employee)
#     db.session.commit()
#     return employee_schema.jsonify(new_employee), 201
#
# @app.route('/employees/<int:employee_id>', methods=['GET'])
# def get_employee(employee_id):
#     employee = Employee.query.get_or_404(employee_id)
#     return employee_schema.jsonify(employee)
#
# @app.route('/employees/<int:employee_id>', methods=['PUT'])
# def update_employee(employee_id):
#     employee = Employee.query.get_or_404(employee_id)
#     updated_employee = employee_schema.load(request.json, instance=employee)
#     db.session.commit()
#     return employee_schema.jsonify(updated_employee)
#
# @app.route('/employees/<int:employee_id>', methods=['DELETE'])
# def delete_employee(employee_id):
#     employee = Employee.query.get_or_404(employee_id)
#     db.session.delete(employee)
#     db.session.commit()
#     return jsonify({'message': 'Employee deleted'}), 204