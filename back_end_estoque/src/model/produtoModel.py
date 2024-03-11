from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DATE, Time, Table
from sqlalchemy.orm import relationship


from src.configs.base import Base
from src.configs.db import engine


class Categorias(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(255), nullable=False, unique=True)
    produto = relationship("Produtos", backref='categorias', lazy=True)

    

    def __repr__(self):
        return f'Categoria (id={self.id}, name={self.categoria}'
Base.metadata.create_all(engine)

class Produtos(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(30))
    descricao = Column(String(255), nullable=False)
    entrada = relationship("Entradas", backref='produtos', lazy=True)
    saida = relationship("Saidas", backref='produtos', lazy=True)
    quantidade = relationship("Quantidades", backref='produtos', lazy=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    def __repr__(self):
        return f'Produto (id={self.id}, marca={self.marca}, tamanho={self.tamanho}, cor={self.cor}), quantidade={self.quantidade}'
Base.metadata.create_all(engine)

class Entradas(Base):
    __tablename__='entradas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataEntrada = Column(DATE)
    horaEntrada = Column(Time)
    tamanho = Column(String(6))
    cor = Column(String(30))
    qtde_entrada = Column(BigInteger, default=0)
    quantidade_id = relationship("Quantidades", backref='entradas', lazy=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'))

    def __repr__(self):
        return f'Entrada (id={self.id}, tamanho={self.tamanho}, cor={self.cor}, qtde_entrada={self.qtde_entrada}'
Base.metadata.create_all(engine)

class Saidas(Base):
    __tablename__='saidas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataSaida = Column(DATE)
    horaSaida = Column(Time)
    tamanho = Column(String(6))
    cor = Column(String(30))
    qtde_saida = Column(BigInteger, default=0)
    quantidade_id = relationship("Quantidades", backref='saidas', lazy=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'))


    def __repr__(self):
        return f'Entrada (id={self.id}, data={self.data}, quantidade={self.quantidade}'
Base.metadata.create_all(engine)

class Quantidades(Base):
    __tablename__='quantidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tamanho = Column(String(6))
    cor = Column(String(30))
    quantidade = Column(BigInteger, default=0)
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    entrada_id = Column(Integer, ForeignKey('entradas.id'), nullable=True)
    saida_id = Column(Integer, ForeignKey('saidas.id'), nullable=True)
    

    def __repr__(self):
        return f'Quantidade (id={self.id}, tamanho={self.tamanho}, quantidade={self.quantidade}, produto_id={self.produto_id})'
Base.metadata.create_all(engine)