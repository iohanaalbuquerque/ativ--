from flask import *

from BD import listar_filme, remove_filme, novo_filme, detalha_filme, atualiza_filme


app = Flask(__name__)


@app.route('/')

def list_boardgames():

   filmes! = listar_filme()

    return render_template("filme.html", filmes!=filmes!)


@app.route("/remover/<int:chave>")

def apagar(chave):

    remove_filme(chave)

    return redirect('/')



@app.route("/novo", methods=['GET', 'POST'])

def cadastrar():

    if request.method == 'POST':

        dados = request.form.to_dict()

        novo_filme(dados.get('nome'), dados.get('genero'), dados.get(classificação indicativa'))

        return redirect('/')

    return render_template('form_filme.html', filme=None, title='Filme Novo')


@app.route("/editar/<int:chave>", methods=['GET', 'POST'])

def editar(chave):

    if request.method == 'POST':

        dados = request.form.to_dict()

        atualiza_filme(chave, dados.get('nome'), dados.get('genero'), dados.get(‘classificação indicativa'))

        return redirect('/')

   filme = detalha_filme(chave)

    return render_template('form_filme.html', filme=filme, title='Editar Filme')


if __name__ == '__main__':


    app.run()
