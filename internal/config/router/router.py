from fastapi import FastAPI
from internal.config.middlewares.auth_key import APIKeyMiddleware
from core.index import Env
from package.index import Logger

from internal.module.index import playwright_router

class Router:
    _app = None
    _initialized = None
    
    def __new__(cls):
        if cls._app is None:
            cls._app = super(Router, cls).__new__(cls)
        return cls._app
        
    def initialize(self):
        if not self._initialized:
            self._app = FastAPI(
                title="My API",
                version="0.0.0",
                debug=Env.get("environment")
            )
            
            self.__class__._initialized = True
            Logger.info("Router Initialized...")
        return self

    def register_middlewares(self):
        self._app.add_middleware(APIKeyMiddleware)

    def register_routes(self):
        self._app.include_router(playwright_router, prefix="/v1", tags=["playwright"])
