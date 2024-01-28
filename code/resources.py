from fastapi.requests import Request
from fastapi_admin.app import app
from fastapi_admin.resources import Action, Dropdown, Field, Model, ToolbarAction
from fastapi_admin.widgets import displays, filters, inputs

from code.models import Admin, Attribution, Product


@app.register
class AdminResource(Model):
    label = "Admin"
    model = Admin
    icon = "fas fa-user"
    page_pre_title = "admin list"
    page_title = "admin model"
    filters = [
        filters.Search(
            name="username",
            label="Name",
            search_mode="contains",
            placeholder="Search for username",
        ),
        filters.Date(name="created_at", label="CreatedAt"),
    ]
    fields = [
        "id",
        "username",
        Field(
            name="password",
            label="Password",
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        Field(
            name="email",
            label="Email",
            input_=inputs.Email(),
        ),
        "created_at",
    ]

    async def get_toolbar_actions(self, request: Request) -> list[ToolbarAction]:
        return []

    async def cell_attributes(
        self,
        request: Request,
        obj: dict,
        field: Field,
    ) -> dict:
        if field.name == "id":
            return {"class": "bg-danger text-white"}
        return await super().cell_attributes(request, obj, field)

    async def get_actions(self, request: Request) -> list[Action]:
        return []

    async def get_bulk_actions(self, request: Request) -> list[Action]:
        return []


@app.register
class Content(Dropdown):
    class AttributionResource(Model):
        label = "Attribution"
        model = Attribution
        fields = [
            "id",
            "created_at",
            "updated_at",
            "gender",
            "age",
            "properties",
        ]

    class ProductResource(Model):
        label = "Product"
        model = Product
        fields = [
            "id",
            "created_at",
            "updated_at",
            "title",
            "description",
            "tags",
            "link_to_product",
            "min_premium_amount",
            "max_premium_amount",
            "max_insurance_coverage",
            "duration_in_years",
        ]

    label = "Content"
    icon = "fas fa-bars"
    resources = [AttributionResource, ProductResource]
