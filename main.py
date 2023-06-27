from fastapi import FastAPI
from src.routers import routers_usuario, routers_produto
from src.infra.sqlalchemy.config.database import criar_banco_de_dados

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers_usuario.router)
    app.include_router(routers_produto.router)
    return app

criar_banco_de_dados()
app = create_app()