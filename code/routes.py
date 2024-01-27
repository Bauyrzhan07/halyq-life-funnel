from fastapi import Depends
from fastapi.requests import Request
from fastapi_admin.app import app
from fastapi_admin.depends import get_resources
from fastapi_admin.template import templates

from code import types
from code.selectors.attribution_selector import AttributionSelector
from code.visualization.pie_charts import plot_attribution_by_value_distribution


@app.get("/")
async def home(
    request: Request,
    resources=Depends(get_resources),
):
    properties = (
        ("income_level", types.IncomeLevelEnum, "User Distribution by Income Level"),
        ("health_status", types.HealthStatusEnum, "User Distribution by Health Status"),
        ("work_style", types.WorkStyleEnum, "User Distribution by Work Style"),
        ("debt_level", types.DebtLevelEnum, "User Distribution by Debt Level"),
    )
    pie_charts = {
        f"{name}_pie_chart": plot_attribution_by_value_distribution(
            data=await AttributionSelector(
                attribution_property=name,
                enum_class=enum_class,
            ).get_user_distribution_by_property(),
            title=title,
        )
        for name, enum_class, title in properties
    }

    return templates.TemplateResponse(
        "dashboard.html",
        context={
            "request": request,
            "resources": resources,
            "resource_label": "Dashboard",
            "page_pre_title": "overview",
            "page_title": "Dashboard",
            **pie_charts,
        },
    )
