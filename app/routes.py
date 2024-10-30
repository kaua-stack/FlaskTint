from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintkaua-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Página inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html',titulo="Contatos")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html',titulo="Cadastar")

@app.route('/atualizar')
def atualizar():
    return render_template('atualizarCadastro.html',titulo="AtualizarCadastro")

@app.route('/consultar')
def consultar():
    return render_template('consultarCa.html',titulo="ConsultarCa")

@app.route('/excluir')
def excluir():
    return render_template('excluirCa.html',titulo="excluirCa")


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf        = request.form.get("cpf")
        nome       = request.form.get("nome")
        telefone   = request.form.get("telefone")
        endereco   = request.form.get("endereco")
        dados      = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro \n +{e}'

@app.route('/listar')
def Listartudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json') #solicitando o dados
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'algo deu errado \n {e}'


@app.route('/atualizarCadastro', methods=['POST'])
def atualizarCadastro():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf": cpf, "nome": nome, "telefone": telefone, "endereco": endereco}
        for codigo in dicionario:
             chave = dicionario[codigo]['cpf']
             if chave == cpf:

                requisicao = requests.patch(f'{link}/cadastro/{codigo}/.json', data=json.dumps(dados))
                return "Atualizado com sucesso!"

    except Exception as e:
              return f'Algo deu errado\n {e}'

@app.route('/excluirco', methods=['POST'])
def excluirco():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")

        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == codigo:
             requisicao = requests.delete(f'{link}/cadastro/{codigo}/.json')
        return "Excluido com sucesso!"

    except Exception as e:
             return f'algo deu errado \n {e}'


@app.route('/consultarCo', methods=['POST'])
def consultarCo():
    try:
        resposta = ""
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")

        for codigo in dicionario:
             chave = dicionario[codigo]['cpf']
             telefone = dicionario[codigo]['telefone']
             nome = dicionario[codigo]['nome']
             endereco = dicionario[codigo]['endereco']
             if chave == cpf:
                resposta = f'cpf:{cpf} \n\n Telefone:{telefone} \n\n Nome:{nome}\n\n endereço:{endereco}\n'
                return resposta
             else:
                resposta = "CPF não encontrado!"
        return resposta
    except Exception as e:
              return f'algo deu errado \n {e}'

