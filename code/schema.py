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

    class IncomeLevelEnum(StrEnum):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    class FinancialGoalEnum(StrEnum):
        DEBT_PAYMENT = "DEBT_PAYMENT"
        CHILDREN_EDUCATION = "CHILDREN_EDUCATION"
        MORTGAGE_PROTECTION = "MORTGAGE_PROTECTION"
        INCOME_REPLACEMENT = "INCOME_REPLACEMENT"

    class AssetEnum(StrEnum):
        INVESTMENT = "INVESTMENT"
        SAVINGS = "SAVINGS"
        PROPERTY = "PROPERTY"
        BUSINESS = "BUSINESS"
        OTHER = "OTHER"

    class DebtLevelEnum(StrEnum):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"
        NO = "NO"

    class WorkStyleEnum(StrEnum):
        PHYSICAL = "PHYSICAL"
        OFFICE = "OFFICE"
        REMOTE = "REMOTE"
        OTHER = "OTHER"

    income_level: IncomeLevelEnum | None = None
    number_of_dependants: int | None = None
    health_status: HealthStatusEnum | None = None
    debt_level: DebtLevelEnum | None = None
    work_style: WorkStyleEnum | None = None
    financial_goals: list[FinancialGoalEnum] = []
    assets: list[AssetEnum] = []


class AttributionUpdate(BaseModel):
    attribution_id: UUID
    properties: AttributionProperties
