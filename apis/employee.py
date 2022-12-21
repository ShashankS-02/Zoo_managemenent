from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.employee import EmployeeModel, EmployeeSchema

api = Namespace("Employee", description="Employee details")

employee = api.model("Employee", {"emp_id": fields.Integer(required=True, description="Employee id"),
                                  "name": fields.String(required=True, description="Employee name"),
                                  "emp_age": fields.Integer(required=True, description="Employee age"),
                                  "emp_role": fields.String(required=True, description="Employee phone number"),
                                  "email": fields.String(required=True, description="Employee email")})

employee1 = {"emp_id": 15, "name": "Sharanidhi", "emp_age": 28, "emp_role": "admin", "email": "shara@gmail.com"}



@api.route("/employee")
class Employee(Resource):
    @api.doc("Returning one employee details")
    def get(self):
        get_employee_query = EmployeeModel.query.all()
        employee_schema = EmployeeSchema(many=True)
        employee_list = employee_schema.dump(get_employee_query)
        return employee_list

    @api.doc("")
    @api.expect(employee, validate=True)
    def post(self):
        print(request.json)

    @api.doc("")
    @api.expect(employee, validate=True)
    def put(self):
        employee_db = EmployeeModel(employee_name=request.json["name"], employee_id=request.json["emp_id"],
                                    employee_age=request.json["emp_age"], employee_role=request.json["emp_role"],
                                    email_id=request.json["email"])
        db.session.add(employee_db)
        db.session.commit()
        print(request.json)





