from fastapi import APIRouter, HTTPException
from src.models.database import *
from src.utils.auth import *
from src.templates.responses_produto import *
from src.models.models import *
import uuid

router = APIRouter(tags=["Produtos"])

@router.post('/cadastrar-produto')
async def cadastra_produto(dados_produto: DadosNovoProduto):
    ja_existe_produto_igual = session.query(Produtos).filter_by(nome_produto = dados_produto.nome).first()
    if not ja_existe_produto_igual == None:
        raise HTTPException(status_code=400, detail="Este produto já foi cadastrado!")
    codigo = str(uuid.uuid4())
    novo_produto = Produtos(nome_produto = dados_produto.nome, codigo_produto = codigo, categoria_produto = dados_produto.categoria, desc_produto = dados_produto.descricao, preco_produto = dados_produto.preco, estoque = 0)
    session.add(novo_produto)
    session.commit()
    return response_produto_cadastrado(novo_produto)

@router.get('/listar-produtos')
async def listar_produtos():
    produtos = session.query(Produtos).all()
    return response_listando_produtos(produtos)

@router.get('/resgatar-produto/{codigo}')
async def resgatar_produto(codigo: str):
    produto_encontrado = session.query(Produtos).filter_by(codigo_produto=codigo).first()
    if not produto_encontrado:
        raise HTTPException(status_code=404, detail="Produto não encontado, código inválido")
    return response_produto_encontrado(produto_encontrado)

async def editar_produto():
    pass

async def excluir_produto():
    pass

async def abastecer_estoque():
    pass