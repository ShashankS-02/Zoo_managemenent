from model import db
from model import ma


class AdminModel(db.model):
    __tablename__ = "admin"
    admin_id = db.Column(db.Integer, primary_key=True, nullable=False)
    admin_name = db.Column(db.String, nullable=False)
    admin_password = db.Column(db.String, nullable=False)


class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdminModel
        load_instance = True
