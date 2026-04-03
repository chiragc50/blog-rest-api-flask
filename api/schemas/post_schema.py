from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    is_private = fields.Str(required=True, validate=validate.OneOf(["true", "false"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)


class PostUpdateInput(Schema):
    title = fields.Str()
    content = fields.Str()
    is_private = fields.Str(validate=validate.OneOf(["true", "false"]))
