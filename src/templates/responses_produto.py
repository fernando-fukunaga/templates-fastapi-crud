from ..models.models import DadosSimplesDoProduto

def response_produto_cadastrado(produto):
    response = {
        "dados": {
        "nome_do_produto": produto.nome_produto,
        "codigo_do_produto": produto.codigo_produto,
        "categoria_produto": produto.categoria_produto,
        "descricao_produto": produto.desc_produto,
        "preco_produto": produto.preco_produto
        },        
        "status": {
        "mensagem": "Produto cadastrado com sucesso",
        "status_code": 200
        }
    }
    return response

def response_listando_produtos(produtos):
    produtos_simples = []
    for produto in produtos:
        produto_simples = DadosSimplesDoProduto(nome=produto.nome_produto, codigo=produto.codigo_produto, preco=produto.preco_produto, estoque=produto.estoque)
        produtos_simples.append(produto_simples)
    response = {
        "produtos": produtos_simples
    }
    return response

def response_produto_encontrado(produto):
    response = {
        "dados": {
        "nome_produto": produto.nome_produto,
        "codigo_produto": produto.codigo_produto,
        "preco_produto": produto.preco_produto,
        "desc_produto": produto.desc_produto,
        "categoria_produto": produto.categoria_produto,
        "estoque_produto": produto.estoque
        }
    }
    return response