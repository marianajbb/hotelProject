# from pymongo import MongoClient
# from bson.objectid import ObjectId
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client["employeeProject"]
# employees = db["employees"]
#
# def create_employee(employee_data):
#     result = employees.insert_one(employee_data)
#     return result.inserted_id
#
# def read_employee(employee_id):
#     employee = employees.find_one({"_id": employee_id})
#     return employee
#
# def update_employee(employee_id, update_data):
#     result = employees.update_one({"_id": employee_id}, {"$set": update_data})
#     return result.modified_count
#
# def delete_employee(employee_id):
#     result = employees.delete_one({"_id": employee_id})
#     return result.deleted_count
