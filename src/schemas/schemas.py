from pydantic import BaseModel

class DadosCadastroUsuario(BaseModel):
    login: str
    senha: str
    administrador: bool | None = None

    class Config:
        orm_mode = True

class DadosNovoProduto(BaseModel):
    nome_produto: str
    categoria_produto: str
    desc_produto: str | None = None
    preco_produto: float

    class Config:
        orm_mode = True    

class DadosSimplesDoUsuario(BaseModel):
    id: int
    login: str
    administrador: bool

    class Config:
        orm_mode = True

class DadosSimplesDoProduto(BaseModel):
    nome_produto: str
    codigo_produto: str
    preco_produto: float
    estoque_disp: int

    class Config:
        orm_mode = True

class DadosAtualizarProduto(BaseModel):
    nome_produto: str
    categoria_produto: str
    desc_produto: str
    preco_produto: float
    estoque_disp: int

    class Config:
        orm_mode = True