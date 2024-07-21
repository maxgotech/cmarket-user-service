from flask_restful import fields, Resource, marshal_with
from app import db
import userService.models as models

userFields = {
    "id": fields.Integer,
    "name": fields.String,
    "mail": fields.String,
}


class User(Resource):
    @marshal_with(userFields)
    def get(self):
        users = db.session.execute(db.select(models.UserModel)).scalars().all()
        return users, 200
