from src.schemas.schemas import DadosCadastro
from src.infra.sqlalchemy.models.models import Usuario
from sqlalchemy.orm import Session
from src.utils.auth import hash_password, verify_password
from src.schemas.responses_usuario import response_usuario_cadastrado

class RepositorioUsuario:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar_usuario(self, schema_usuario: DadosCadastro):
        model_usuario: Usuario = Usuario(login=schema_usuario.login,
                                         senha=hash_password(schema_usuario.senha),
                                         administrador=schema_usuario.administrador)
        login_ja_existe = self.banco_de_dados.query(model_usuario).filter_by(login=schema_usuario.login)
        if login_ja_existe == None:
            self.banco_de_dados.add(model_usuario)
            self.banco_de_dados.commit()
            return response_usuario_cadastrado(model_usuario)
        else:
            return "erro"