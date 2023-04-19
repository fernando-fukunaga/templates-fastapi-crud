from fastapi import APIRouter, HTTPException
from src.models.database import *
from src.utils.auth import *
from src.templates.responses_usuario import *
from src.models.models import *

router = APIRouter()

@router.post('/cadastrar-usuario')
async def cadastra_usuario(dados_cadastro: DadosCadastro):
    ja_existe_login_igual = session.query(Usuarios).filter_by(login = dados_cadastro.login).first()
    if not ja_existe_login_igual == None:
        raise HTTPException(status_code=400, detail="Ja existe um usuario com esse mesmo login!")
    senha_hash = hash_password(dados_cadastro.senha)
    novo_usuario = Usuarios(login=dados_cadastro.login, senha=senha_hash, administrador=dados_cadastro.permissao_de_adm)
    session.add(novo_usuario)
    session.commit()
    return response_usuario_cadastrado(novo_usuario)

@router.get('/resgatar-usuario')
async def resgata_usuario(login: str):
    usuario_encontrado = session.query(Usuarios).filter_by(login=login).first()
    if usuario_encontrado == None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return response_usuario_encontrado(usuario_encontrado)

@router.put('/editar-usuario')
async def edita_usuario(login: str, dados_cadastro: DadosCadastro):
    usuario_encontrado = session.query(Usuarios).filter_by(login=login).first()
    if usuario_encontrado == None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    senha_hash = hash_password(dados_cadastro.senha)
    setattr(usuario_encontrado, 'login', dados_cadastro.login)
    setattr(usuario_encontrado, 'senha', senha_hash)
    setattr(usuario_encontrado, 'administrador', dados_cadastro.permissao_de_adm)
    session.commit()
    return response_usuario_editado(usuario_encontrado)

@router.delete('/excluir-usuario')
async def excluir_usuario(login: str):
    usuario_encontrado = session.query(Usuarios).filter_by(login=login).first()
    if usuario_encontrado == None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    session.delete(usuario_encontrado)
    session.commit()
    return response_usuario_deletado()