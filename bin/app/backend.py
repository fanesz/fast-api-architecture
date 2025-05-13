from package.index import Logger
from core.index import Env
from internal.config.router.router import Router
import uvicorn

def create_app():
    Env.initialize()

    router = Router().initialize()
    router.register_middlewares()
    router.register_routes()
    
    return router._app

def run_app():
    Logger.info("Starting backend app...")
    
    app = create_app()
    
    host = Env.get("BE_HOST")
    port = int(Env.get("BE_PORT"))
    is_dev = Env.isDevelopment
    
    Logger.info("Starting server...")
    
    if is_dev:
        Logger.info("Development mode: Using hot reload")
        uvicorn.run(
            "app.backend:create_app",
            host=host,
            port=port,
            reload=True,
            factory=True
        )
    else:
        Logger.info("Production mode: No hot reload")
        uvicorn.run(
            app,
            host=host,
            port=port
        )