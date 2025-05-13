class PlaywrightService:
    async def get_sentiment(self, brand_keyword: str):
        print("[mock] success get sentiment...")
        return { "brand_name": brand_keyword, "sentiments": ["yeah", "cool", "anjass"] }