from fastapi import APIRouter, Response, status


router = APIRouter(prefix="/health")


@router.get(
    "/",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
async def health_handler():
    return Response(status_code=status.HTTP_200_OK)
