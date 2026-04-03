from marshmallow import Schema, fields


class UserSignUp(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class UserLogin(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    access_token = fields.Str(dump_only=True)
