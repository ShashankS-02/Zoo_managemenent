from flask_restx import Namespace, Resource, fields
from flask import request
from model import db
from model.admin_data import AdminModel, AdminSchema

api = Namespace("Admin", description="Details of the Admin")

admin = api.model("Admin", {"admin_name": fields.String(required=True, description="Admin's User Name"),
                            "admin_pass": fields.String(required=True, description="Admin's password")
                            })


admin1 = {"admin_name": "Shashank", "admin_pass": "Shandilya"}


@api.route("/admin")
class Admin(Resource):
    @api.doc("")
    def get(self):
        get_admin_query = AdminModel.query.all()
        admin_schema = AdminSchema(many=True)
        admin_list = admin_schema.dump(get_admin_query)
        print(admin_list)
        return admin_list

    @api.expect(admin, validate=True)
    def post(self):
        # admin_db = AdminModel(admin_name=request.json["admin_name"], admin_password=request.json["admin_pass"])

        if(request.json["admin_name"] == admin1["admin_name"] and request.json["admin_pass"] == admin1["admin_pass"]):
            return {"success" : True}
        else:
            return {"success": False}
        # db.session.add(admin_db)  # adds rows to the connected database table
        # db.session.commit()  # commit the changes to the row
        # print(request.json)