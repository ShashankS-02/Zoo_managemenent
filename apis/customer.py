from flask_restx import Namespace, Resource, fields
from flask import request

api = Namespace("customer", description="Customer details")

customer = api.model("Customer", {"cus_id": fields.Integer(required=True, description="Customer id"),
                                  "name": fields.String(required=True, description="customer name"),
                                  "ph_no": fields.Integer(required=True, description="customers phone number"),
                                  "cus_date": fields.Date(required=True, description="date booked by the customer")})

customer1 = {"cus_id": 100, "name": "Shashank", "ph_no": 6361377960, "cus_date": "2022-06-12"}



@api.route("/customer")
class Customer(Resource):
    @api.doc("Returning one customers details")
    def get(self):
        return customer1

    @api.doc("")
    @api.expect(customer, validate=True)
    def post(self):
        print(request.json)

#put
#delete




