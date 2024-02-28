from model import db
from model import ma


# Database Model definition
class EmployeeModel(db.Model):
    __tablename__ = "employee"
    employee_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_name = db.Column(db.String(80), nullable=False)
    employee_age = db.Column(db.Integer, nullable=False)
    employee_role = db.Column(db.String(70), nullable=False)
    email_id = db.Column(db.String(100), nullable=False)


class EmployeeSchema(ma.SQLAlchemyAutoSchema):  # Marshmallow
    class Meta:
        model = EmployeeModel
        load_instance = True
