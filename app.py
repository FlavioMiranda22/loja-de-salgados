from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

produtos = [
    {'id': 1, 'nome': 'Coxinha', 'preco': 5.0, 'descricao': 'Coxinha crocante recheada com frango', 'imagem': 'https://via.placeholder.com/150'},
    {'id': 2, 'nome': 'Empada', 'preco': 4.5, 'descricao': 'Empada de frango com catupiry', 'imagem': 'https://via.placeholder.com/150'},
    {'id': 3, 'nome': 'Enroladinho', 'preco': 6.0, 'descricao': 'Enroladinho de presunto e queijo', 'imagem': 'https://via.placeholder.com/150'}
]

carrinho = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_carrinho', methods=['POST'])
def adicionar_carrinho():
    produto_id = int(request.form['produto_id'])
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto:
        carrinho.append(produto)
        return jsonify({'status': 'Produto adicionado ao carrinho'})
    return jsonify({'status': 'Erro ao adicionar produto ao carrinho'}), 400

@app.route('/carrinho')
def get_carrinho():
    return jsonify(carrinho)

@app.route('/compra_certa')
def compra_certa():
       return jsonify({'status': 'sua compra deu certo!'})

@app.route('/compra_errada')
def compra_errada():
       return jsonify({'status': 'ops credenciais errada'})

if __name__ == '__main__':
    app.run(debug=True)
