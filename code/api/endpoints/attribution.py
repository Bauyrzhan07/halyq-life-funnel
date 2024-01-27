from datetime import datetime, timezone

from fastapi import APIRouter, Request, Response, status
from loguru import logger
from tortoise.exceptions import DoesNotExist

from code.models import Attribution
from code.schema import AttributionInit, AttributionUpdate


router = APIRouter(prefix="/attribution")


@router.post(
    "/init/",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def init_handler(
    request: Request,
    data: AttributionInit,
):
    init_data = {
        "id": data.attribution_id,
        **data.model_dump(exclude={"attribution_id"}),
    }
    attribution = await Attribution.create(**init_data)
    logger.info(f"Created attribution {attribution.id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch(
    "/properties/",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_properties_handler(
    request: Request,
    data: AttributionUpdate,
):
    try:
        attribution = await Attribution.select_for_update().get(
            id=data.attribution_id,
        )
    except DoesNotExist:
        logger.error(f"Attribution {data.attribution_id} not found, data: {data}")
        return Response(
            content={"detail": "Attribution not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    properties_to_update = data.properties.model_dump(exclude_none=True)

    attribution.properties = {**attribution.properties, **properties_to_update}
    attribution.updated_at = datetime.now(tz=timezone.utc)
    await attribution.save()

    logger.info(
        f"Updated attribution {attribution.id} with properties {properties_to_update}",
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
