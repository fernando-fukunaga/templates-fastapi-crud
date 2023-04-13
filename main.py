from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.models.models import *
from src.templates.responses import *

app = FastAPI()

class DadosCadastro(BaseModel):
    login: str
    senha: str
    permissao_de_adm: int

@app.post('/cadastrar-usuario')
async def cadastra_usuario(dados_cadastro: DadosCadastro):
    ja_existe_login_igual = session.query(Usuarios).filter_by(dados_cadastro.login).first()
    if not ja_existe_login_igual == None:
        raise HTTPException(status_code=400, detail="Ja existe um usuario com esse mesmo login!")
    novo_usuario = Usuarios(login=dados_cadastro.login, senha=dados_cadastro.senha, administrador=dados_cadastro.permissao_de_adm)
    return response_usuario_cadastrado(novo_usuario)