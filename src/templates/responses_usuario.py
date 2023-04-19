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

def response_usuario_encontrado(usuario):
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
        "mensagem": "Usuário resgatado com sucesso",
        "status_code": 200
        }
    }
    return response   

def response_usuario_editado(usuario):
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
        "mensagem": "Usuário atualizado com sucesso",
        "status_code": 200
        }
    }
    return response

def response_usuario_deletado():
    response = {       
        "status": {
        "mensagem": "Usuário excluído com sucesso",
        "status_code": 200
        }
    }
    return response