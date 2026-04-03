from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from passlib.hash import pbkdf2_sha256
from api.db import db
from api.models.User import User
from api.models.RevokedToken import RevokedToken
from api.schemas.user_schema import UserSignUp, UserLogin

blp = Blueprint("users", "users", description="Operations on users")


@blp.route("/signup")
class SignUp(MethodView):
    @blp.arguments(UserSignUp)
    @blp.response(201, UserSignUp)
    def post(self, user_data):
        if User.query.filter_by(email=user_data["email"]).first():
            abort(409, message="User already exists")
        if User.query.filter_by(username=user_data["username"]).first():
            abort(409, message="Username already exists")
        user = User(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()
        return user


@blp.route("/login")
class Login(MethodView):
    @blp.arguments(UserLogin)
    @blp.response(200, UserLogin)
    def post(self, user_data):
        user = User.query.filter_by(email=user_data["email"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id), fresh=True)
            return {"access_token": access_token}
        abort(401, message="Invalid credentials")


@blp.route("/logout")
class Logout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        revoked_token = RevokedToken(jti=jti)
        db.session.add(revoked_token)
        db.session.commit()
        return {"message": "Successfully logged out"}
