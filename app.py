import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Ribeiro',
        'habilidades': ['Python', 'Django']}

]
# devolve um desenvolvedor pelo ID tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT' 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem':mensagem}
        return response
    elif request.method == 'PUT':
        dados = json.loads(request.body)
        desenvolvedores[id] = dados
        return dados
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

# lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def listar_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    elif request.method == 'GET':
        return desenvolvedores


if __name__ == '__main__':
    app.run(debug=True)