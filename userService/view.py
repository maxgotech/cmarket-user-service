from app import app
from flask_restful import Api
import userService.service as service

api = Api(app)

api.add_resource(service.User, "/api/user/")
