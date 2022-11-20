from flask_restx import Api
from .ticketing import api as ticketing_api
from .customer import api as customer_api

api = Api(
    title="Zoo management",
    version="1.0",
    description="Zoo management apis"
)

api.add_namespace(ticketing_api, path="/ticketing")
api.add_namespace(customer_api, path="/registration")