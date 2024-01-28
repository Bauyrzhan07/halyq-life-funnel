from loguru import logger

from code.models import Attribution, Product
from code.services.calculation import RecommendedPremiumCalculationService


class ProductRecommendationService:
    def __init__(self, attribution: Attribution):
        self.gender = attribution.gender
        self.age_group = attribution.age
        self.properties = attribution.properties

    async def process(self):
        products = await Product.all()
        logger.info(f"Got products: {products}")
        product_recommendation_coefficient = {
            product.id: self._calc_product_recommendation_coefficient(product)
            for product in products
        }
        max_product_recommendation_coefficient = max(
            product_recommendation_coefficient.values(),
        )
        recommended_products = []
        for product in products:
            coefficient = product_recommendation_coefficient[product.id]
            if coefficient == max_product_recommendation_coefficient:
                recommended_calculation = RecommendedPremiumCalculationService(
                    gender=self.gender,
                    age_group=self.age_group,
                    properties=self.properties,
                    product=product,
                ).calculate()
                recommended_products.append(
                    {
                        "product": {
                            "title": product.title,
                            "description": product.description,
                            "link_to_product": product.link_to_product,
                        },
                        **recommended_calculation,
                    },
                )
        return recommended_products

    def _calc_product_recommendation_coefficient(self, product: Product):
        product_tags = product.tags
        coefficient = 0
        for _property, value in self.properties.items():
            if isinstance(value, str):
                product_tag_value = product_tags.get(_property, [])
                coefficient += int(value in product_tag_value)
            elif isinstance(value, list):
                coefficient += len(
                    set(value).intersection(set(product_tags.get(_property, []))),
                )
        return coefficient
