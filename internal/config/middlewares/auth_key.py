from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from core.index import Env

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)
        
        api_key = request.headers.get("X-API-Key")
        
        if not api_key or api_key != Env.get("API_KEY"):
            return JSONResponse(
                status_code=403,
                content={"error": "Invalid or missing API key"}
            )
        
        return await call_next(request)