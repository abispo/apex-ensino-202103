
from http import HTTPStatus
from flask import Blueprint, request, jsonify
from .models import Account
from .controllers import create_transaction

accounts_app = Blueprint('accounts_app', __name__)

"""
Criar a rota /transactions
Essa rota deve aceitar o método POST
Vamos precisar dos seguintes dados:
    - user_id               - ID do usuário que está realizando essa transação
    - debit_account_id      - ID da conta do usuário que vai ser debitada
    - credit_account_id     - ID da conta do usuário que vai ser creditado
    - value                 - valor da operação
    
Depois de ser salvo, a rota deve retornar o objeto Transaction

A rota /transactions deve aceitar o método GET.
O retorno deve ser do tipo:
    id: Id da transação
    user: o e-mail do usuário
    debit_account: Nome da conta debitada
    credit_account: Nome da conta creditada
    observation: Observações da transação
    value: Valor
    
    [
        {
            'id': 1,
            'user': 'maria@email.com',
            'debit_account': 'Conta Corrente ViaCredi',
            'credit_account': 'Conta de Luz Celesc',
            'observation': 'Muito caro',
            'value': 250.00
        }
    ]

"""


@accounts_app.route('/transactions', methods=['POST'])
def post_transaction():
    data = request.get_json()

    transaction = create_transaction(data)

    return jsonify(transaction.serialize()), HTTPStatus.CREATED
