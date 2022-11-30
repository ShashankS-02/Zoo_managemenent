from model import db
from model import ma


class TicketModel(db.model):
    __tablename__ = "tickets_details"
    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    booked_date = db.Column(db.String(10), nullable=False)


class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TicketModel
        load_instance = True
