from flask_restx import Api
from .ticketing import api as ticketing_api
from .customer import api as customer_api
from .employee import api as employee_api
from .admin import api as admin_api
from .animals import api as animal_api

api = Api(
    title="Zoo management",
    version="1.0",
    description="Zoo management apis"
)

api.add_namespace(ticketing_api, path="/ticketing")
api.add_namespace(customer_api, path="/registration")
api.add_namespace(employee_api, path="/emp_details")
api.add_namespace(admin_api, path="/auth")
api.add_namespace(animal_api, path="/animal_details")