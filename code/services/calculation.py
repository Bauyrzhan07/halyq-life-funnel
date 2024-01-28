from loguru import logger

from code import types
from code.models import Attribution, Product
from code.schema import AttributionProperties


INCOME_LEVEL_BASE_PAYMENT_MAPPER = {
    types.IncomeLevelEnum.LOW: 30000,
    types.IncomeLevelEnum.MEDIUM: 80000,
    types.IncomeLevelEnum.HIGH: 150000,
}


class RecommendedPremiumCalculationService:
    def __init__(
        self,
        gender: Attribution.Gender,
        age_group: str,
        properties: AttributionProperties,
        product: Product,
    ):
        logger.info(
            f"Init RecommendedPremiumCalculationService with properties: {properties}",
        )
        self.gender = gender
        self.age_group = age_group
        self.income_level = properties.get("income_level")
        self.health_status = properties.get("health_status")
        self.debt_level = properties.get("debt_level")
        self.work_style = properties.get("work_style")
        self.number_of_dependants = properties.get("number_of_dependants")
        self.financial_goals = properties.get("financial_goals", [])
        self.assets = properties.get("assets", [])
        self.product = product

    def calculate(self):
        premium = self._get_premium()
        logger.info(f"Calculated premium: {premium}")
        return {
            "premium": str(premium),
            "insurance_coverage": str(self.product.max_insurance_coverage),
            "duration_in_years": self.product.duration_in_years,
        }

    def _get_premium(self):
        premium = self.product.min_premium_amount
        if self.gender == Attribution.Gender.MALE:
            premium *= 1.1
        if self.age_group in (types.AgeGroupEnum.MIDDLE, types.AgeGroupEnum.OLD):
            premium *= 1.2
        if self.health_status == types.HealthStatusEnum.BAD:
            premium *= 1.3
        if self.debt_level in (types.DebtLevelEnum.MEDIUM, types.DebtLevelEnum.HIGH):
            premium *= 1.3
        if self.work_style == types.WorkStyleEnum.PHYSICAL:
            premium *= 1.3
        premium = min(self.product.max_premium_amount, premium)
        premium = max(self.product.min_premium_amount, premium)
        return round(premium, 2)
