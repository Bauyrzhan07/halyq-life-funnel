from datetime import datetime

from fastapi import Depends
from fastapi.requests import Request
from fastapi_admin.app import app
from fastapi_admin.depends import get_resources
from fastapi_admin.template import templates

from code import types
from code.selectors.attribution_selector import AttributionSelector
from code.visualization.income_level import plot_attribution_by_value_distribution


@app.get("/")
async def home(
    request: Request,
    resources=Depends(get_resources),
    created_at__gte: datetime = None,
):
    income_level_data = await AttributionSelector(
        attribution_property="income_level",
        enum_class=types.IncomeLevelEnum,
    ).get_user_distribution_by_property()
    health_status_data = await AttributionSelector(
        attribution_property="health_status",
        enum_class=types.HealthStatusEnum,
    ).get_user_distribution_by_property()
    work_style_data = await AttributionSelector(
        attribution_property="work_style",
        enum_class=types.WorkStyleEnum,
    ).get_user_distribution_by_property()
    debt_level_data = await AttributionSelector(
        attribution_property="debt_level",
        enum_class=types.DebtLevelEnum,
    ).get_user_distribution_by_property()
    income_level_chart = plot_attribution_by_value_distribution(
        data=income_level_data,
        enum_class=types.IncomeLevelEnum,
        x_label="Income Level",
        y_label="Number of Users",
        title="User Distribution by Income Level",
    )
    health_status_chart = plot_attribution_by_value_distribution(
        data=health_status_data,
        enum_class=types.HealthStatusEnum,
        x_label="Health Status",
        y_label="Number of Users",
        title="User Distribution by Health Status",
    )
    work_style_chart = plot_attribution_by_value_distribution(
        data=work_style_data,
        enum_class=types.WorkStyleEnum,
        x_label="Work Style",
        y_label="Number of Users",
        title="User Distribution by Work Style",
    )
    debt_level_chart = plot_attribution_by_value_distribution(
        data=debt_level_data,
        enum_class=types.DebtLevelEnum,
        x_label="Debt Level",
        y_label="Number of Users",
        title="User Distribution by Debt Level",
    )

    return templates.TemplateResponse(
        "dashboard.html",
        context={
            "request": request,
            "resources": resources,
            "resource_label": "Dashboard",
            "page_pre_title": "overview",
            "page_title": "Dashboard",
            "income_level_chart": income_level_chart,
            "health_status_chart": health_status_chart,
            "work_style_chart": work_style_chart,
            "debt_level_chart": debt_level_chart,
        },
    )
