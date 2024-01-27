from code.models import Attribution


class AttributionSelector:
    def __init__(self, attribution_property, enum_class):
        self.attribution_property = attribution_property
        self.enum_class = enum_class

    async def get_user_distribution_by_property(self):
        attributions = await Attribution.all().only("properties")

        property_distribution = {enum_label.name: 0 for enum_label in self.enum_class}
        for attribution in attributions:
            attribution_value = attribution.properties.get(self.attribution_property)
            if not attribution_value:
                continue
            property_distribution[attribution_value] += 1
        return property_distribution
