from http import HTTPStatus
import uuid
from flask import Flask, jsonify, request


class Account:
    def __init__(self, name, value=0):
        self._id = str(uuid.uuid4())
        self._name = name
        self._value = value

    # O método serialize é responsável por serializar o nosso objeto Python, ou seja,
    # retornar uma representação desse objeto em um formato que seja entendido pela função
    # jsonify (objeto response)
    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'value': self._value
        }

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
#

accounts_list = [
    Account(name="Conta Padrão"),
    Account(name="Conta Corrente ViaCredi"),
    Account(name="Conta Poupança Caixa", value=200)
]


class Transaction:
    def __init__(self, debit_account, credit_account, value):
        self._id = str(uuid.uuid4())
        self._debit_account = debit_account
        self._credit_account = credit_account
        self._value = value


app = Flask(__name__)


# ===== ROTAS =====
@app.route('/accounts', methods=['GET'])
def list_all_accounts():
    return jsonify([account.serialize() for account in accounts_list]), HTTPStatus.OK


@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json

    name = data.get('name')
    value = data.get('value', 0)

    account = Account(name=name, value=value)
    accounts_list.append(account)

    return jsonify(account.serialize()), HTTPStatus.CREATED


@app.route('/accounts/<id>', methods=['GET'])
def get_account_by_id(id):

    for account in accounts_list:
        if id == account.id:
            return jsonify(account.serialize()), HTTPStatus.OK

    return jsonify(message="Conta não encontrada"), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True)
