from app import db
from flask_restful import fields, Resource, marshal_with, abort, reqparse
import userService.models as models
from flask import request

userFields = {
    "id": fields.Integer,
    "name": fields.String,
    "secondname": fields.String,
    "mail": fields.String,
    "about": fields.String,
}

userMessage_fields = {
    "message": fields.String,
    "user": fields.Nested(userFields),
}

post_args = reqparse.RequestParser()
post_args.add_argument("name", type=str, required=True, help="name cannot be blank")
post_args.add_argument(
    "secondname", type=str, required=True, help="secondname cannot be blank"
)
post_args.add_argument("mail", type=str, required=True, help="mail cannot be blank")
post_args.add_argument(
    "password", type=str, required=True, help="password cannot be blank"
)
post_args.add_argument("role", type=str, required=True, help="role cannot be blank")

patch_args = reqparse.RequestParser()
patch_args.add_argument("id", type=int, required=True, help="id cannot be blank")
patch_args.add_argument("name", type=str, store_missing=False)
patch_args.add_argument("secondname", type=str, store_missing=False)
patch_args.add_argument("mail", type=str, store_missing=False)
patch_args.add_argument("password", type=str, store_missing=False)
patch_args.add_argument("role", type=str, store_missing=False)
patch_args.add_argument("pfp_path", type=str, store_missing=False)
patch_args.add_argument("about", type=str, store_missing=False)


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = db.session.execute(db.select(models.UserModel)).scalars().all()
        return users, 200


class User(Resource):
    @marshal_with(userFields)
    def get(self):
        mail = request.args.get("mail", default="")
        id = request.args.get("id", default=0)

        if not id and not mail:
            abort(400, message="Invalid request data")

        if id and mail:
            abort(400, message="only 1 parameter expected, found 2")

        if id:
            user = db.session.execute(
                db.select(models.UserModel).where(models.UserModel.id == id)
            ).scalar()
        elif mail:
            user = db.session.execute(
                db.select(models.UserModel).where(models.UserModel.mail == mail)
            ).scalar()
        print(user)
        if not user:
            abort(404, message="User not Found")
        return user, 200

    @marshal_with(userMessage_fields)
    def post(self):
        args = post_args.parse_args()
        check = db.session.execute(
            db.select(models.UserModel).where(models.UserModel.mail == args["mail"])
        ).scalar_one_or_none()

        if check:
            abort(409, message="This email is already registered")

        user = models.UserModel(**args)
        db.session.add(user)
        db.session.commit()
        created = db.session.execute(
            db.select(models.UserModel).where(models.UserModel.mail == args["mail"])
        ).scalar()
        return {"message": "success", "user": created}, 201

    @marshal_with(userMessage_fields)
    def patch(self):
        args = patch_args.parse_args()
        user = db.session.execute(
            db.select(models.UserModel).where(models.UserModel.id == args["id"])
        ).scalar_one()
        del args["id"]
        user.update(**args)
        db.session.commit()
        return {"message": "success", "user": user}, 200

    def delete(self):
        id = request.args.get("id", default=0)
        mail = request.args.get("mail", default="")

        if not id and not mail:
            abort(400, message="Invalid request data")

        if id and mail:
            abort(400, message="only 1 parameter expected, found 2")

        if id:
            user = db.session.execute(
                db.select(models.UserModel).where(models.UserModel.id == id)
            ).scalar()
        elif mail:
            user = db.session.execute(
                db.select(models.UserModel).where(models.UserModel.mail == mail)
            ).scalar()

        if not user:
            abort(404, message="User not Found")

        db.session.delete(user)
        db.session.commit()
        return {"message": "success"}, 200
