from uuid import UUID

from pydantic import BaseModel

from code import types
from code.models import Attribution


class AttributionInit(BaseModel):
    attribution_id: UUID
    age: types.AgeGroupEnum | None = None
    gender: Attribution.Gender | None = None


class AttributionProperties(BaseModel):
    income_level: types.IncomeLevelEnum | None = None
    health_status: types.HealthStatusEnum | None = None
    debt_level: types.DebtLevelEnum | None = None
    work_style: types.WorkStyleEnum | None = None
    number_of_dependants: int | None = None
    financial_goals: list[types.FinancialGoalEnum] = []
    assets: list[types.AssetEnum] = []


class AttributionUpdate(BaseModel):
    attribution_id: UUID
    properties: AttributionProperties


class PaymentsRecommendationsResponse(BaseModel):
    recommended_payment_amount: str
