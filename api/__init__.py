from flask import Flask
from dotenv import load_dotenv
import os
from api.extensions import jwt, limiter, api, cors, migrate
from api.db import db
from api.resources.posts import blp as PostsBlueprint
from api.resources.users import blp as UsersBlueprint
from api.models.User import User
from api.models.Post import Post
from api.models.RevokedToken import RevokedToken

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Flask-Smorest / OpenAPI
    app.config["API_TITLE"] = "My API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["OPENAPI_SWAGGER_UI"] = True

    # Optional
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    # initialize extensions
    api.init_app(app)
    limiter.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # custom jwt token claims
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        if RevokedToken.query.filter_by(jti=jti).first():
            return True
        return False

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return {
            "description": "The token has been revoked",
            "error": "token_revoked",
        }, 401

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return {"description": "The token has expired", "error": "token_expired"}, 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            {"description": "Signature verification failed", "error": "invalid_token"},
        )
        401

    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return {
            "description": "Authorization credentials are missing or incorrect",
            "error": "unauthorized",
        }, 401

    # register blueprints
    api.register_blueprint(UsersBlueprint, url_prefix="/api/v1/users")
    api.register_blueprint(PostsBlueprint, url_prefix="/api/v1/posts")

    return app
