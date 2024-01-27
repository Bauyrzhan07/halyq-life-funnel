from uuid import UUID

from fastapi import APIRouter, Request, status
from loguru import logger
from starlette.responses import JSONResponse
from tortoise.exceptions import DoesNotExist

from code.models import Attribution
from code.schema import PaymentsRecommendationsResponse
from code.services.calculation import RecommendedMonthlyPaymentCalculationService


router = APIRouter(prefix="/recommendations")


@router.get(
    "/",
    response_model=PaymentsRecommendationsResponse,
    status_code=status.HTTP_200_OK,
)
async def get_recommendations_handler(
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

    return JSONResponse(
        content={
            "recommended_payment_amount": RecommendedMonthlyPaymentCalculationService(
                gender=attribution.gender,
                age_group=attribution.age,
                properties=attribution.properties,
            ).calculate(),
        },
        status_code=status.HTTP_200_OK,
    )
