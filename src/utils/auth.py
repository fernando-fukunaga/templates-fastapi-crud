from passlib.context import CryptContext

# Criando um contexto de senha, usado para definir qual script será usado e será chamado para hashear e validar senhas:
context = CryptContext(schemes=["bcrypt"], deprecated='auto')

# Definindo qual será a chave secreta para encodar e decodar os tokens jwt, o algoritmo e o tempo de expiração:
SECRET_KEY = "d9fd25fb5fbad53273ef0ab9ed7e06934be36bb413a18b85e74610e2b37914a6"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 3600
# Secret key foi gerada digitando openssl rand -hex 32 no terminal

def hash_password(senha):
    return context.hash(senha)

def verify_password(senha_pura, senha_hash):
    return context.verify(senha_pura, senha_hash)