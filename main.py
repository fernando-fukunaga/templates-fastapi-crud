from fastapi import FastAPI
from src.routers import routers_usuario, routers_produto

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers_usuario.router)
    app.include_router(routers_produto.router)
    return app