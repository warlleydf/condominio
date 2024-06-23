from flask import Flask, render_template, request, redirect, url_for, flash
from models import Encomenda

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        unidade = request.form['unidade']
        descricao = request.form['descricao']
        porteiro = request.form['porteiro']
        data_recebimento = request.form['data_recebimento']
        Encomenda.registrar_encomenda(unidade, descricao, porteiro, data_recebimento)
        flash('Encomenda registrada com sucesso!')
        return redirect(url_for('index'))
    return render_template('registrar.html')

@app.route('/listar')
def listar():
    encomendas = Encomenda.listar_encomendas()
    return render_template('listar.html', encomendas=encomendas)

@app.route('/dar_baixa', methods=['GET', 'POST'])
def dar_baixa():
    if request.method == 'GET':
        encomendas = Encomenda.listar_encomendas()
        return render_template('dar_baixa.html', encomendas=encomendas)
    if request.method == 'POST':
        id_encomenda = int(request.form['id_encomenda'])
        if Encomenda.encomenda_existe(id_encomenda):
            if Encomenda.encomenda_existe(id_encomenda):
                 if Encomenda.encomenda_existe_entrega(id_encomenda):
                    flash("Encomenda não disponivel para baixa.")            
                 else: 
                    Encomenda.dar_baixa_encomenda(id_encomenda)
                    flash(f"Encomenda {id_encomenda} marcada como entregue.")              
        else:
            flash("Encomenda não encontrada.")
        return redirect(url_for('index'))
    return render_template('dar_baixa.html')

@app.route('/listar_baixadas')
def listar_baixadas():
    encomendas_baixadas = Encomenda.listar_encomendas_entregues()
    return render_template('listar_baixadas.html', encomendas=encomendas_baixadas)

@app.route('/listar_disponiveis')
def listar_disponiveis():
    encomendas = Encomenda.listar_encomendas()
    return render_template('listar_disponiveis.html', encomendas=encomendas)

if __name__ == '__main__':
    app.run(debug=True)
