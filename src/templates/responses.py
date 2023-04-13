def response_usuario_cadastrado(usuario):
    if usuario.administrador == 1:
        admin = True
    else:
        admin = False
    response = {
        "dados": {
        "login": usuario.login,
        "admin": admin
        },        
        "status": {
        "mensagem": "Usuário cadastrado com sucesso",
        "status_code": 200
        }
    }
    return response