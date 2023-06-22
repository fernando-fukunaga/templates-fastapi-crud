from src.infra.sqlalchemy.config import Base
from sqlalchemy import Column, String, Integer, Boolean, DECIMAL

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    login = Column(String(15), nullable=False, unique=True)
    senha = Column(String(60), nullable=False)
    administrador = Column(Boolean, nullable=False, default=False)

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    nome_produto = Column(String(55), nullable=False, unique=True)
    codigo_produto = Column(String(36), nullable=False, unique=True)
    categoria_produto = Column(String(15), nullable=False)
    desc_produto = Column(String(55), nullable=False, default="Sem informação")
    preco_produto = Column(DECIMAL(5,2), nullable=False)
    estoque_disp  = Column(Integer, nullable=False, default=0)