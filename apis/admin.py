from flask_restx import Namespace, Resource, fields
#  from flask import request

api = Namespace("Admin", description="Details of the Admin")

admin = api.model("Admin", {"admin_id": fields.Integer(required=True, description="Admin Identifier"),
                            "admin_name": fields.String(required=True, description="Admin's User Name"),
                            "admin_pass": fields.String(required=True, description="Admin's password")
                            })


admin1 = {"admin_name": "Shashank", "admin_pass": "Shandilya"}


@api.route("/admin")
class Admin(Resource):
    @api.doc("")
    def get(self):
        return admin1
