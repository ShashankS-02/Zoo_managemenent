from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.customer import CustomerModel, CustomerSchema

api = Namespace("customer", description="Customer details")



customer = api.model("Customer", {"cus_id": fields.Integer(required=True, description="Customer id"),
                                  "name": fields.String(required=True, description="customer name"),
                                  "ph_no": fields.String(required=True, description="customers phone number"),
                                  "email": fields.String(required=True, description="Customers email"),
                                  "number_of_tickets": fields.String(required=True, description="number of tickets")})

customer1 = {"cus_id": 100, "name": "Shashank", "ph_no": 6361377960, "cus_date": "2022-06-12"}


@api.route("/booking")
class Customer(Resource):
    @api.doc("Returning one customers details")
    def get(self):
        get_customer_query = CustomerModel.query.all()
        customer_schema = CustomerSchema(many=True)  # marshmallow obj
        customer_list = customer_schema.dump(get_customer_query)  # converts db obj to py obj
        print(customer_list)
        return customer_list

    @api.doc("")
    @api.expect(customer, validate=True)
    def post(self):
        ids = str(request.json['cus_id'])
        db.engine.execute("delete from customer where customer_id = " + ids)
        return {"success": True}

    @api.doc("")
    @api.expect(customer, validate=True)
    def put(self):
        customer_db = CustomerModel(customer_name=request.json["name"], phone_number=request.json["ph_no"],
                                    email_id=request.json["email"], num_of_tickets=int(request.json["number_of_tickets"]))
        db.session.add(customer_db)  # adds rows to the connected database table
        db.session.commit()  # commit the changes to the row

        # msg = Message(
        #     'Hello',
        #     sender='yourId@gmail.com',
        #     recipients=['receiver’sid@gmail.com']
        # )
        # msg.body = "Thank you "+ request.json["name"] +" for booking "+ request.json["number_of_tickets"] +" with us. Hope you have a great visit."
        # mail.send(msg)


        return {"success": True}

        print(request.json)


# delete
