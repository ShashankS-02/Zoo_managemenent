from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.customer import CustomerModel, CustomerSchema

api = Namespace("customer", description="Customer details")

customer = api.model("Customer", {"cus_id": fields.Integer(required=True, description="Customer id"),
                                  "name": fields.String(required=True, description="customer name"),
                                  "ph_no": fields.Integer(required=True, description="customers phone number"),
                                  "email": fields.String(required=True, description="Customers email")})

customer1 = {"cus_id": 100, "name": "Shashank", "ph_no": 6361377960, "cus_date": "2022-06-12"}



@api.route("/customer")
class Customer(Resource):
    @api.doc("Returning one customers details")
    def get(self):
        get_customer_query = CustomerModel.query.all()
        customer_schema = CustomerSchema(many=True)  # marshmallow obj
        customer_list = customer_schema.dump(get_customer_query)  # converts db obj to py obj
        return customer_list

    @api.doc("")
    @api.expect(customer, validate=True)
    def post(self):
        print(request.json)

    @api.doc("")
    @api.expect(customer, validate=True)
    def put(self):
        customer_db = CustomerModel(customer_name=request.json["name"], phone_number=request.json["ph_no"], email_id=request.json["email"])
        db.session.add(customer_db)  # adds rows to the connected database table
        db.session.commit()  # commit the changes to the row
        print(request.json)


# delete




