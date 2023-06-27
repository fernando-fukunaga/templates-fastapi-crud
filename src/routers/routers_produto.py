from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_banco_de_dados

router = APIRouter(tags=["Produtos"])

@router.post("/produtos", response_model=schemas.DadosSimplesDoProduto)
async def criar_produto(schema_produto: schemas.DadosNovoProduto, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioProduto(banco_de_dados).criar_produto(schema_produto)

@router.get("/produtos", response_model=List[schemas.DadosSimplesDoProduto])
async def listar_produtos(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioProduto(banco_de_dados).listar_produtos()

@router.get("/produtos/{codigo_produto}", response_model=schemas.DadosSimplesDoProduto)
async def obter_produto(codigo_produto: str, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioProduto(banco_de_dados).obter_produto(codigo_produto)

@router.put("/produtos/{codigo_produto}", response_model=schemas.DadosSimplesDoProduto)
async def atualizar_produto(codigo_produto: str, schema_produto: schemas.DadosAtualizarProduto, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioProduto(banco_de_dados).atualizar_produto(codigo_produto, schema_produto)

@router.delete("/produtos/{codigo_produto}")
async def deletar_produto(codigo_produto: str, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioProduto(banco_de_dados).deletar_produto(codigo_produto)