from pydantic import BaseModel

class DadosCadastro(BaseModel):
    login: str
    senha: str
    administrador: bool | None = None

class DadosNovoProduto(BaseModel):
    nome: str
    categoria: str
    descricao: str | None = None
    preco: float

class DadosSimplesDoUsuario(BaseModel):
    id: int
    login: str
    administrador: bool

class DadosSimplesDoProduto(BaseModel):
    nome: str
    codigo: str
    preco: float
    estoque_disp: int