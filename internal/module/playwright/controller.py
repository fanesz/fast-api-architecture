from fastapi import APIRouter, Depends, Query
from .service import PlaywrightService
from .dtos.index import GetSentimentResDto

router = APIRouter(prefix="/playwright")

def get_service():
    return PlaywrightService()

@router.get("", response_model=GetSentimentResDto)
async def get_sentiment(
    brand_name: str = Query(None, description="Brand name"),
    service: PlaywrightService = Depends(get_service)
):
    return await service.get_sentiment(brand_name)