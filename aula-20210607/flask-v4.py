from datetime import datetime
# A classe HTTPStatus contém as constantes que representam os códigos de retorno HTTP
from http import HTTPStatus
# O objeto request do Flask é responsável por armazenar as requisições feitas a um endpoint
# A função jsonify retorna uma resposta em json formado pelos argumentos que lhe são passados.
from flask import Flask, request, jsonify

# Precisamos criar o objeto Flask que vai representar a nossa
# aplicação
app = Flask(__name__)


# Dessa maneira criamos as rotas na nossa aplicação, ou endpoints.
# Podemos atribuir mais de uma rota(endpoint) a uma função(view)
@app.route('/')
@app.route('/index')
def index():
    return "Olá! Estou aprendendo Flask."


# Quando queremos passar um argumento na rota, utilizamos a sintaxe
# <argumento>. Esse argumento deve ser passado também para a função.
@app.route('/hello/<username>')
def hello_username(username):
    return f"Hello {username}"


# Podemos fazer o 'cast' (conversão) do argumento passado para o
# tipo que desejarmos.
@app.route('/double/<int:num>')
def double_num(num):
    return f"{num * num}"


# O argumento methods indica quais os verbos HTTP são aceitos nessa
# rota (GET, POST, PATCH, etc...)
@app.route('/datenow', methods=['GET'])
def datenow():
    return datetime.now().strftime('%H:%M:%S %Y-%m-%d')


@app.route('/operation', methods=['POST'])
def operation():
    data = request.json

    operation = data['operation']
    number_1 = data['number_1']
    number_2 = data['number_2']

    if operation == '+':
        result = number_1 + number_2

    elif operation == '-':
        result = number_1 - number_2

    elif operation == '*':
        result = number_1 * number_2

    elif operation == '/':
        result = number_1 / number_2

    else:
        return jsonify(message="Operação desconhecida"), HTTPStatus.NOT_FOUND

    return jsonify({'result': result}), HTTPStatus.CREATED


if __name__ == '__main__':
    app.run()
