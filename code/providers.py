from fastapi import Depends, Form, status, Request

from fastapi_admin.depends import (
    get_current_admin,
    get_resources,
)
from fastapi_admin.utils import hash_password, check_password
from fastapi_admin.models import AbstractAdmin
from fastapi_admin.providers.login import UsernamePasswordProvider


class LoginProvider(UsernamePasswordProvider):
    async def password(
            self,
            request: Request,
            old_password: str = Form(...),
            new_password: str = Form(...),
            re_new_password: str = Form(...),
            admin: AbstractAdmin = Depends(get_current_admin),  # noqa: B008
            resources=Depends(get_resources),  # noqa: B008
    ):
        return await self.logout(request)

    async def pre_save_admin(self, _, instance: AbstractAdmin, using_db, update_fields):
        instance.password = hash_password(instance.password)
