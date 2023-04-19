def response_produto_cadastrado(produto):
    response = {
        "dados": {
        "nome_do_produto": produto.nome_produto,
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