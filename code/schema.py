from uuid import UUID

from pydantic import BaseModel

from code.models import Attribution
from code.utils import StrEnum


class AttributionInit(BaseModel):
    attribution_id: UUID
    age: str | None = None
    gender: Attribution.Gender | None = None


class AttributionProperties(BaseModel):
    class HealthStatusEnum(StrEnum):
        BAD = "BAD"
        GOOD = "GOOD"
        EXCELLENT = "EXCELLENT"

    class LevelEnum(StrEnum):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    class FinancialGoalEnum(StrEnum):
        DEBT_PAYMENT = "DEBT_PAYMENT"
        CHILDREN_EDUCATION = "CHILDREN_EDUCATION"
        MORTGAGE_PROTECTION = "MORTGAGE_PROTECTION"
        INCOME_REPLACEMENT = "INCOME_REPLACEMENT"

    class LastInjuramceTimeEnum(StrEnum):
        THIS_MONTH = "THIS_MONTH"
        LAST_MONTH = "LAST_MONTH"
        THIS_YEAR = "THIS_YEAR"
        MORE_THAN_YEAR = "MORE_THAN_YEAR"

    class AssetEnum(StrEnum):
        INVESTMENT = "INVESTMENT"
        SAVINGS = "SAVINGS"
        PROPERTY = "PROPERTY"
        BUSINESS = "BUSINESS"
        OTHER = "OTHER"

    income_level: LevelEnum | None = None
    is_married: bool = False
    number_of_dependants: int = 0
    health_status: HealthStatusEnum | None = None
    financial_goals: list[FinancialGoalEnum] = []
    debt_level: LevelEnum | None = None
    last_injurance_time: LastInjuramceTimeEnum | None = None
    assets: list[AssetEnum] = []


class AttributionUpdate(BaseModel):
    attribution_id: UUID
    properties: AttributionProperties
