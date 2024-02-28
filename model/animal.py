from model import db
from model import ma


# Database Model definition
class AnimalModel(db.Model):
    __tablename__ = "animal"
    animal_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cage_id = db.Column(db.Integer, nullable=False)
    animal_name = db.Column(db.String(30), nullable=False)
    animal_breed = db.Column(db.String(100), nullable=False)


class AnimalSchema(ma.SQLAlchemyAutoSchema):  # Marshmallow / SQLAlchemyAutoSchema automatically creates a column on the table
    class Meta:
        model = AnimalModel
        load_instance = True