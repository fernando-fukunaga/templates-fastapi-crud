from fastapi import APIRouter, HTTPException
from src.models.database import *
from src.utils.auth import *
from src.templates.responses_produto import *
from src.models.models import *

router = APIRouter()

@router.post('/cadastrar-produto')
async def cadastra_produto(dados_produto: DadosNovoProduto):
    ja_existe_produto_igual = session.query(Produtos).filter_by(nome_produto = dados_produto.nome).first()
    if not ja_existe_produto_igual == None:
        raise HTTPException(status_code=400, detail="Este produto já foi cadastrado!")
    novo_produto = Produtos(nome_produto = dados_produto.nome, categoria_produto = dados_produto.categoria, desc_produto = dados_produto.descricao, preco_produto = dados_produto.preco, estoque = 0)
    session.add(novo_produto)
    session.commit()
    return response_produto_cadastrado(novo_produto)