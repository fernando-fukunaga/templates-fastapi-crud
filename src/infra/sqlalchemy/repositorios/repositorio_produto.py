from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy.orm import Session
from sqlalchemy import update
from typing import List
import uuid

class RepositorioProduto:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar_produto(self, schema_produto: schemas.DadosNovoProduto):
        model_produto: models.Produto = models.Produto(nome_produto=schema_produto.nome_produto,
                                                       codigo_produto=str(uuid.uuid4()),
                                                       categoria_produto=schema_produto.categoria_produto,
                                                       desc_produto=schema_produto.desc_produto,
                                                       preco_produto=schema_produto.preco_produto)
        self.banco_de_dados.add(model_produto)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_produto)
        return model_produto

    def listar_produtos(self):
        lista_produtos: List[models.Produto] = self.banco_de_dados.query(models.Produto).all()
        return lista_produtos

    def obter_produto(self, codigo_produto: str):
        model_produto: models.Produto = self.banco_de_dados.query(models.Produto).filter_by(codigo_produto=codigo_produto).first()
        return model_produto

    def atualizar_produto(self, codigo_produto: str, schema_atualizar_produto: schemas.DadosAtualizarProduto):
        model_produto: models.Produto = self.obter_produto(codigo_produto)
        prepared_statement = (update(models.Produto).where(models.Produto.codigo_produto==codigo_produto).values(nome_produto=schema_atualizar_produto.nome_produto,
                                                                                                                 categoria_produto=schema_atualizar_produto.categoria_produto,
                                                                                                                 desc_produto=schema_atualizar_produto.desc_produto,
                                                                                                                 preco_produto=schema_atualizar_produto.preco_produto,
                                                                                                                 estoque_disp=schema_atualizar_produto.estoque_disp))
        self.banco_de_dados.execute(prepared_statement)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_produto)
        return model_produto

    def deletar_produto(self, codigo_produto: str):
        model_produto: models.Produto = self.obter_produto(codigo_produto)
        self.banco_de_dados.delete(model_produto)
        self.banco_de_dados.commit()
        return {"msg":"produto removido"}