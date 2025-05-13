from pydantic import BaseModel
from typing import List

class GetSentimentResDto(BaseModel):
    brand_name: str
    sentiments: List[str]