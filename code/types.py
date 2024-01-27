from enum import Enum


class StrEnum(str, Enum):
    pass


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


class DebtLevelEnum(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NO = "NO"


class WorkStyleEnum(StrEnum):
    PHYSICAL = "PHYSICAL"
    OFFICE = "OFFICE"
    REMOTE = "REMOTE"


class AgeGroupEnum(StrEnum):
    YOUNG = "18-30"
    MIDDLE = "30-50"
    OLD = "50+"
