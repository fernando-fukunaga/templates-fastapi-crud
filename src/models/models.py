from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker

# Criando motor do banco de dados:
engine = create_engine('mysql+mysqlconnector://root@localhost:3306/lojinha')

# Criando base declarativa que será usada para fazer a base das tabelas do banco:
Base = declarative_base()

# Criando os modelos:
class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    login = Column(String(55))
    senha = Column(String(100))
    administrador = Column(Integer)

class Produtos(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome_produto = Column(String(20))
    categoria_produto = Column(String(20))
    desc_produto = Column(String(100))
    preco_produto = Column(DECIMAL(4,2))
    estoque = Column(Integer, default=0)

# Criando as tabelas
Base.metadata.create_all(engine)

# Criando sessão para utilizar o mysql durante o programa
Session = sessionmaker(bind=engine)
session = Session()

# Criando o administrador
'''adm_user = Usuarios(login="admin", senha="123", administrador=1)
session.add(adm_user)
session.commit()'''