from flask_restx import Namespace, Resource, fields

api = Namespace('ticketing', description='Takes bookings and generates a ticket')

ticket = api.model('Ticket', {'id': fields.String(required=True, description="Ticket identifier"),
                              'cus_name': fields.String(required=True, description="Customer name"),
                              'ph_no': fields.Integer(required=True, description="Customers phone number"),
                              'date': fields.Date(required=True, description="Booking date")
                              })   # Nothing known about QR

list_ticket = [{'id': "001", 'cus_name': "Shashank"}, {'id': "002", "cus_name": "Rakshith"}]
ticket1 = {'id': "123", 'cus_name': "Nithin", 'ph_no': 9972736303, 'date': '2022-06-28'}


@api.route("/")
class TicketList(Resource):
    @api.doc("Returning list of tickets")
    @api.marshal_list_with(ticket)
    def get(self):
        return list_ticket


@api.route("/id")
class Ticket(Resource):
    @api.marshal_with(ticket)
    def get(self):
        return ticket1


#shashank