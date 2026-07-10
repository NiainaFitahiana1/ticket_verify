from dataclasses import dataclass
from marshmallow import Schema, fields, validate




class LoginSchema(Schema):
username = fields.Str(required=True)
password = fields.Str(required=True)




class AdminOutSchema(Schema):
id = fields.Int()
username = fields.Str()
is_active = fields.Bool()
created_at = fields.DateTime()




class ProductCreateSchema(Schema):
name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
description = fields.Str(required=False, allow_none=True)
price = fields.Float(required=True)
in_stock = fields.Bool(required=False)




class ProductOutSchema(Schema):
id = fields.Int()
name = fields.Str()
description = fields.Str()
price = fields.Float()
in_stock = fields.Bool()
created_at = fields.DateTime()
updated_at = fields.DateTime()