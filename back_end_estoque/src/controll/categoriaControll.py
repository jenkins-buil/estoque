from src.configs.db import engine
from src.model.produtoModel import Categorias
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

class CategoriaControll:

    def findAll():
            result = []
            data = session.query(Categorias).all()
            for categoria in data:
                result.append({
                    "id": categoria.id,
                    "categoria": categoria.categoria
                })
            return result
    
    def create(categoria):
        categoria_name = categoria['categoria'].upper()
        data_insert = Categorias(categoria=categoria_name)
        session.add(data_insert)
        session.commit()

    def findByCategoriaName(categoria):
         result = []
         categoria_name = categoria['categoria'].upper()
         data = session.query(Categorias).filter(Categorias.categoria == categoria_name)
         for produto in data:
              result.append({
                   "id": produto.id,
                   "categoria": produto.categoria
              })
         return result
         