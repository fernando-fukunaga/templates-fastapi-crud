from pydantic import BaseModel

class DadosCadastroUsuario(BaseModel):
    login: str
    senha: str
    administrador: bool | None = None

    class Config:
        orm_mode = True

class DadosNovoProduto(BaseModel):
    nome: str
    categoria: str
    descricao: str | None = None
    preco: float

    class Config:
        orm_mode = True    

class DadosSimplesDoUsuario(BaseModel):
    id: int
    login: str
    administrador: bool

    class Config:
        orm_mode = True

class DadosSimplesDoProduto(BaseModel):
    nome: str
    codigo: str
    preco: float
    estoque_disp: int

    class Config:
        orm_mode = True