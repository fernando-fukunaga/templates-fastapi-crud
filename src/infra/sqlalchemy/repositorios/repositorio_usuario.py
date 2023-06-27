from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.utils.auth import hash_password
from typing import List

class RepositorioUsuario:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar_usuario(self, schema_usuario: schemas.DadosCadastroUsuario):
        model_usuario: models.Usuario = models.Usuario(login=schema_usuario.login,
                                                       senha=hash_password(schema_usuario.senha),
                                                       administrador=schema_usuario.administrador)
        self.banco_de_dados.add(model_usuario)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_usuario)
        return model_usuario
    
    def listar_usuarios(self):
        lista_usuarios: List[models.Usuario] = self.banco_de_dados.query(models.Usuario).all()
        return lista_usuarios
    
    def obter_usuario(self, id_usuario: int):
        model_usuario: models.Usuario = self.banco_de_dados.query(models.Usuario).filter_by(id=id_usuario).first()
        return model_usuario

    def atualizar_usuario(self, id_usuario: int, schema_usuario_atualizado: schemas.DadosCadastroUsuario):
        prepared_statement = (update(models.Usuario).where(models.Usuario.id==id_usuario).values(login=schema_usuario_atualizado.login,
                                                                                 senha=hash_password(schema_usuario_atualizado.senha),
                                                                                 administrador=schema_usuario_atualizado.administrador))
        self.banco_de_dados.execute(prepared_statement)
        self.banco_de_dados.commit()
        return self.obter_usuario(id_usuario)

    def deletar_usuario(self, id_usuario: int):
        model_usuario: models.Usuario = self.obter_usuario(id_usuario)
        self.banco_de_dados.delete(model_usuario)
        self.banco_de_dados.commit()
        return {"msg":"usuario removido"}
