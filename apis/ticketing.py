from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.ticket import TicketModel, TicketSchema

api = Namespace('ticketing', description='Takes bookings and generates a ticket')

ticket = api.model('Ticket', {'ticket_id': fields.Integer(required=True, description="Ticket identifier"),
                              'cus_name': fields.String(required=True, description="Customer name"),
                              'ph_no': fields.Integer(required=True, description="Customers phone number"),
                              'date': fields.Date(required=True, description="Booking date")
                              })   # Nothing known about QR

list_ticket = [{'id': "001", 'cus_name': "Shashank"}, {'id': "002", "cus_name": "Rakshith"}]
ticket1 = {'id': "123", 'cus_name': "Nithin", 'ph_no': 9972736303, 'date': '2022-06-28'}


@api.route("/get_ticket_list")
class TicketList(Resource):
    @api.doc("Returning list of tickets")
    @api.marshal_list_with(list_ticket)
    def get(self):
        ticket_query = TicketModel.querry.all()
        ticket_schema = TicketSchema(many=True)
        ticket_list = ticket_schema.dump(ticket_query)
        return ticket_list

    @api.doc("creates a new entry in the ticket table")
    @api.expect(ticket, validate=True)
    def put(self):
        ticket_db = TicketModel(ticket_id=request.json["ticket_id"], customer_name=request.json["cus_name"],
                                phone_number=request.json["ph_no"], booked_date=request.json["date"])
        db.session.add(ticket_db)
        db.session.commit()
