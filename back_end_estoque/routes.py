from flask import Flask, jsonify, request
from flask_cors import CORS
from src.controll.produtoControll import ProdutoControll 
from src.controll.categoriaControll import CategoriaControll
from src.controll.entrada_saida import Entrada_Saida_Controll 



app = Flask(__name__)
cors = CORS(app)

@app.route('/produtos', methods=['POST'])
def inserirProdutos():
    produto = request.json
    temProduto = ProdutoControll.produtoPossuiCadastro(produto)
    if temProduto:
        return "Produto já possui cadastro"
    ProdutoControll.create(produto)
    return "produto inserido!"

@app.route('/produtos')
def buscarProdutos():
    produtos = ProdutoControll.findAll()
    return jsonify(produtos)

@app.route('/produtos/<int:id>')
def buscarProdutoPeloId(id):
    produto = ProdutoControll.findById(id)
    return jsonify(produto)

@app.route('/teste/<name>')
def buscarProdutoPeloNome(name):
    produto = ProdutoControll.findByName(name)
    if produto == []:
       return "Produto não cadastrado"
    return jsonify(produto) 

@app.route('/categorias')
def getCategoria():
    categoria = CategoriaControll.findAll()
    return jsonify(categoria)

@app.route('/categorias', methods=['POST'])
def inserirCategorias():
    categoria = request.json
    temCategoria = CategoriaControll.findByCategoriaName(categoria)
    if temCategoria == []:
        CategoriaControll.create(categoria)
        return "Categoria inserido com sucesso"
    return "Já existe cadastro para categoria infomado!"
@app.route('/entradas', methods=['POST'])
def entradaProduto():
    produto = request.json
    Entrada_Saida_Controll.entradaProduto(produto)
    return "Atualizado com sucesso!"

@app.route('/entradas/<int:id>')
def historicoEntradas(id):
    produto = Entrada_Saida_Controll.historicoEntrada(id)
    return jsonify(produto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)