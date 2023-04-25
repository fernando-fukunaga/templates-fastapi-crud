from pydantic import BaseModel

class DadosCadastro(BaseModel):
    login: str
    senha: str
    permissao_de_adm: int

class DadosNovoProduto(BaseModel):
    nome: str
    categoria: str
    descricao: str
    preco: float

class DadosSimplesDoUsuario(BaseModel):
    id: int
    login: str
    administrador: bool