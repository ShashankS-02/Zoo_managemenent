from model import db
from model import ma


# Database Model definition
class CustomerModel(db.Model):
    __tablename__ = "customer"
    customer_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    customer_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    email_id = db.Column(db.String(100), nullable=False)


class CustomerSchema(ma.SQLAlchemyAutoSchema):  # Marshmallow / SQLAlchemyAutoSchema automatically creates a column on the table
    class Meta:
        model = CustomerModel
        load_instance = True
