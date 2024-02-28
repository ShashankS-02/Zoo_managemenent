from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.animal import AnimalModel, AnimalSchema
from sqlalchemy import delete


api = Namespace("Animals", description="Animal Details")

animal = api.model("Animal", {"ani_id": fields.Integer(required=True, description="Animal id"),
                              "cage_id": fields.String(required=True, description="Cage id"),
                              "ani_name": fields.String(required=True, description="Animal name"),
                              "ani_breed": fields.String(required=True, description="Breed to which animal belongs to")})


animal1 = {"ani_id": 10, "cage id": 5, "ani_name": "Lion", "ani_breed": "African lion Panthera Leo" }


@api.route("/animals")
class Animal(Resource):
    @api.doc("Returning animal details")
    def get(self):
        get_animal_query = AnimalModel.query.all()
        animal_schema = AnimalSchema(many=True)
        animal_list = animal_schema.dump(get_animal_query)
        return animal_list

    # @api.doc("")
    # @api.expert(animal, validate=True)
    # def post(self):
    #     print(request.json)


    @api.doc("")
    @api.expect(animal, validate=True)
    def put(self):
        animal_db = AnimalModel(animal_name=request.json["ani_name"], animal_id=request.json["ani_id"],
                                cage_id=int(request.json["cage_id"]), animal_breed=request.json["ani_breed"])
        db.session.add(animal_db)
        db.session.commit()
        print(request.json)
        return {"success":True}

    @api.doc("")
    @api.expect(animal, validate=True)
    def post(self):
        ids = str(request.json['ani_id'])
        db.engine.execute("delete from animal where animal_id = "+ids)
        return {"success":True}
