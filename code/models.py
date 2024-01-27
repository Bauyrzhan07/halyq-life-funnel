import datetime

from pydantic.config import ConfigDict
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi_admin.models import AbstractAdmin

from code.utils import StrEnum


class Common(models.Model):
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class Attribution(Common):
    class Gender(StrEnum):
        MALE = "MALE"
        FEMALE = "FEMALE"

    user_id = fields.BigIntField(index=True, null=True, default=None)
    gender = fields.CharEnumField(enum_type=Gender, null=True, default=None)
    age = fields.CharField(max_length=6, null=True, default=None)
    properties = fields.JSONField(default=dict)


AttributionDTO = pydantic_model_creator(
    Attribution,
    model_config=ConfigDict(from_attributes=True),
)

class Admin(models.Model):
    id = fields.BigIntField(generated=True, pk=True)  # noqa: A003

    email = fields.CharField(max_length=200, default='')
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=200)

    last_login = fields.DatetimeField(default=datetime.datetime.now)

    created_at = fields.DatetimeField(auto_now_add=True)