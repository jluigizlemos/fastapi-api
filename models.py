import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

load_dotenv()

# cria a conexão do seu banco
DATABASE_URL = os.getenv(
    "DATABASE_URL"
)
db = create_engine(DATABASE_URL)

# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
    

# Pedido

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = [
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")]
    

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # status = Column("status", ChoiceType(STATUS_PEDIDOS))
    status = Column("status", String)
    usuario= Column("usuario", Integer, ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco

#ItensPedido    

class ItensPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"))
    
    def __init__(self, pedido, quantidade, sabor, tamanho, preco_unitario):
        self.pedido = pedido
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario


# executa a criação dos metadados do banco de dados