from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.models.models import *
from src.templates.responses import *
from src.utils.auth import *

app = FastAPI()

class DadosCadastro(BaseModel):
    login: str
    senha: str
    permissao_de_adm: int

@app.post('/cadastrar-usuario')
async def cadastra_usuario(dados_cadastro: DadosCadastro):
    ja_existe_login_igual = session.query(Usuarios).filter_by(login = dados_cadastro.login).first()
    if not ja_existe_login_igual == None:
        raise HTTPException(status_code=400, detail="Ja existe um usuario com esse mesmo login!")
    senha_hash = hash_password(dados_cadastro.senha)
    novo_usuario = Usuarios(login=dados_cadastro.login, senha=senha_hash, administrador=dados_cadastro.permissao_de_adm)
    session.add(novo_usuario)
    session.commit()
    return response_usuario_cadastrado(novo_usuario)