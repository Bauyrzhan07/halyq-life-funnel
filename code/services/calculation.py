from loguru import logger

from code import types
from code.models import Attribution
from code.schema import AttributionProperties


INCOME_LEVEL_BASE_PAYMENT_MAPPER = {
    types.IncomeLevelEnum.LOW: 30000,
    types.IncomeLevelEnum.MEDIUM: 80000,
    types.IncomeLevelEnum.HIGH: 150000,
}


class RecommendedMonthlyPaymentCalculationService:
    def __init__(
        self,
        gender: Attribution.Gender,
        age_group: str,
        properties: AttributionProperties,
    ):
        logger.info(
            f"Init RecommendedMonthlyPaymentCalculationService with properties: {properties}",
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

    def calculate(self):
        multiplier = self._get_multiplier()
        logger.info(f"Calculated multiplier: {multiplier}")
        return str(
            multiplier * INCOME_LEVEL_BASE_PAYMENT_MAPPER[self.income_level],
        )

    def _get_multiplier(self):
        base_coefficient = 1
        if self.gender == Attribution.Gender.MALE:
            base_coefficient += 0.25
        if self.age_group == types.AgeGroupEnum.MIDDLE:
            base_coefficient += 0.25
        elif self.age_group == types.AgeGroupEnum.OLD:
            base_coefficient += 0.4
        if self.health_status == types.HealthStatusEnum.BAD:
            base_coefficient += 0.5
        if self.debt_level in (types.DebtLevelEnum.MEDIUM, types.DebtLevelEnum.HIGH):
            base_coefficient -= 0.5
        if self.work_style == types.WorkStyleEnum.PHYSICAL:
            base_coefficient += 0.5
        if self.financial_goals:
            base_coefficient += 0.1 * len(self.financial_goals)
        if self.number_of_dependants:
            base_coefficient += 0.1 * self.number_of_dependants
        if self.assets:
            base_coefficient -= 0.5 * len(self.assets)
        base_coefficient = min(2.5, base_coefficient)
        base_coefficient = max(1.0, base_coefficient)
        return round(base_coefficient, 2)
