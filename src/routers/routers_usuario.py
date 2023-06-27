from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_banco_de_dados
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas import schemas

router = APIRouter(tags=["Usuarios"])

@router.post("/usuarios", response_model=schemas.DadosSimplesDoUsuario)
async def cadastar_usuarios(schema_usuario: schemas.DadosCadastroUsuario, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).criar_usuario(schema_usuario)

@router.get("/usuarios", response_model=List[schemas.DadosSimplesDoUsuario])
async def listar_usuarios(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).listar_usuarios()

@router.get("/usuarios/{id_usuario}", response_model=schemas.DadosSimplesDoUsuario)
async def obter_usuario(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).obter_usuario(id_usuario)

@router.put("/usuarios/{id_usuario}", response_model=schemas.DadosSimplesDoUsuario)
async def editar_usuarios(id_usuario: int, schema_usuario_atualizado: schemas.DadosCadastroUsuario, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).atualizar_usuario(id_usuario, schema_usuario_atualizado)

@router.delete("/usuarios/{id_usuario}")
async def excluir_usuarios(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).deletar_usuario(id_usuario)