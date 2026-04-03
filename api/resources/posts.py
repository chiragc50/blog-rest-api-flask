from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models.Post import Post
from api.schemas.post_schema import PostSchema, PostUpdateInput
from api.db import db
from api.extensions import limiter

blp = Blueprint("posts", __name__, description="Operations on posts")


@blp.route("/")
class PostList(MethodView):
    decorators = [limiter.limit("100/hour")]

    @blp.response(200, PostSchema(many=True))
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        is_private = request.args.get("is_private")
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        try:
            query = Post.query
            if is_private == "true":
                query = query.filter_by(user_id=user, is_private="true")
            else:
                query = query.filter_by(is_private="false")

            posts = query.paginate(page=page, per_page=per_page)
            return posts.items
        except Exception:
            abort(400, message="Error: unable to get posts")

    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    @jwt_required()
    def post(self, data):
        user = get_jwt_identity()
        post = Post(**data, user_id=user)
        try:
            db.session.add(post)
            db.session.commit()
        except Exception:
            abort(400, message="unable to create post")
        return post


@blp.route("/<int:post_id>")
class PostDetail(MethodView):
    decorators = [limiter.limit("100/hour")]

    @blp.response(200, PostSchema)
    @jwt_required()
    def get(self, post_id):
        user = get_jwt_identity()
        try:
            post = Post.query.filter_by(user_id=user, id=post_id).first()
            if post is None:
                abort(404, message="Post not found")
            return post
        except Exception:
            abort(400, message="Error: unable to get post")

    @blp.arguments(PostUpdateInput)
    @blp.response(200, PostSchema)
    @jwt_required()
    def put(self, data, post_id):
        user = get_jwt_identity()
        try:
            post = Post.query.filter_by(user_id=user, id=post_id).first()
            if post is None:
                abort(404, message="Post not found")

            if "title" in data:
                post.title = data["title"]
            if "content" in data:
                post.content = data["content"]
            if "is_private" in data:
                post.is_private = data["is_private"]

            db.session.commit()
            return post

        except Exception:
            abort(400, message="Error: unable to update post")

    @jwt_required()
    def delete(self, post_id):
        user = get_jwt_identity()
        try:
            post = Post.query.filter_by(user_id=user, id=post_id).first()
            if post is None:
                abort(404, message="Post not found")
            db.session.delete(post)
            db.session.commit()
            return {"message": f"post deleted with {post_id}"}
        except Exception:
            abort(400, message="Error: unable to delete post")
