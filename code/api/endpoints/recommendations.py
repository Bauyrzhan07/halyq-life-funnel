from uuid import UUID

from fastapi import APIRouter, Request, status
from loguru import logger
from starlette.responses import JSONResponse
from tortoise.exceptions import DoesNotExist

from code.models import Attribution
from code.schema import ProductRecommendationsResponse
from code.services.recommendation import ProductRecommendationService


router = APIRouter(prefix="/recommendations")


@router.get(
    "/products/",
    response_model=ProductRecommendationsResponse,
    status_code=status.HTTP_200_OK,
)
async def get_recommended_products(
    request: Request,
    attribution_id: UUID,
):
    try:
        attribution = await Attribution.get(id=attribution_id)
    except DoesNotExist as exc:
        logger.error(
            f"Error getting recommendations with attribution_id {attribution_id}: {exc}",
        )
        return JSONResponse(
            content={"detail": "Error getting recommendations"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    response = await ProductRecommendationService(
        attribution=attribution,
    ).process()
    return JSONResponse(
        content={
            "recommended_products": ProductRecommendationsResponse(
                recommended_products=response,
            ).model_dump(),
        },
        status_code=status.HTTP_200_OK,
    )
