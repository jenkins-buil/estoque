from src.model.produtoModel import Quantidades
from src.configs.db import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


class AtualizaEstoque:
    def cadastrarNovo(produto):
        produto_id = produto.produto_id
        tamanho = produto.tamanho
        cor = produto.cor
        quantidade = produto.qtde_entrada
        entrada_id = produto.id
        data_insert = Quantidades(produto_id=produto_id, tamanho=tamanho, cor=cor,
                               quantidade=quantidade, entrada_id=entrada_id)
        session.add(data_insert)
        session.commit()
        return
        
    def temCadastroTabelaQuantidade(data):
        tamanho = data.tamanho
        cor = data.cor
        produto_id = data.produto_id
        data = session.query(Quantidades).filter(Quantidades.produto_id==produto_id).all()
        
        
        for Quantidade in data:
            if Quantidade.tamanho == tamanho and Quantidade.cor == cor:
                return {
                    "id": Quantidade.id,
                    "tamanho": Quantidade.tamanho,
                    "cor": Quantidade.cor,
                    "quantidade": Quantidade.quantidade,
                    "produto_id": Quantidade.produto_id
                }
        return


        
        
