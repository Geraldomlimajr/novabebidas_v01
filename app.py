from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "MINHA-PALAVRA"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'

db = SQLAlchemy(app)

class Produtos(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    produto = db.Column (db.String, nullable = False)
    categoria = db.Column (db.String, nullable = False)
    quantidade= db.Column (db.Integer, nullable = False)
    custo_un = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    preco_venda = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastrar')
def form_cadastrar():
    return render_template('cadastrar.html')

@app.route('/estoque')
def ver_estoque():
        estoque = Produtos.query.all()
        return render_template("/ver_estoque.html", estoque = estoque)


@app.route('/atualizar', methods = ['POST'])
def atualizar():
     id_produto = request.form.get('codigo')
     n_produto = request.form.get('produto')
     n_categoria = request.form.get('categoria')
     n_quantidade = request.form.get('quantidade')
     n_custo = request.form.get('custo')
     n_venda = request.form.get('venda')

     produtos = Produtos.query.get(id_produto)    

     produtos.produto = n_produto
     produtos.categoria = n_categoria
     produtos.quantidade = n_quantidade
     produtos.custo_un = n_custo
     produtos.preco_venda= n_venda

     db.session.commit()

    

     return redirect("/estoque")   

    

@app.route("/cadastrar_produto" , methods = ['POST'])
def cadastrar_produto():
    produto = request.form['product']
    categoria = request.form['category']
    quantidade = request.form['amount']
    custo_un = request.form['cost-price']
    preco_venda = request.form['sale-price']

    produto_estoque = Produtos(
        produto = produto,
        categoria = categoria,
        quantidade = quantidade,
        custo_un= custo_un,
        preco_venda = preco_venda
    )

    db.session.add(produto_estoque)
    db.session.commit()
    
    return redirect('/estoque')

@app.route('/delete/<int:id>' , methods = ['POST'])
def deletar(id):
     produto = Produtos.query.get(id)

     db.session.delete(produto)
     db.session.commit() 

     return redirect(url_for('ver_estoque'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
