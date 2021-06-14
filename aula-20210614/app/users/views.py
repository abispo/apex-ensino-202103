from flask import jsonify, request, Blueprint
from http import HTTPStatus

from .controllers import (
    get_all_users, create_user, get_user_by_id, delete_user,
    update_user_profile
)

from app.accounts.controllers import create_account


users_app = Blueprint('users_app', __name__)


# Routes
# http://127.0.0.1:5000/users
@users_app.route('/users', methods=['GET'])
def get():
    all_users = [user.serialize() for user in get_all_users()]
    return jsonify(all_users), HTTPStatus.OK


@users_app.route('/users', methods=['POST'])
def post():
    # Capturamos os dados enviados pelo cliente
    data = request.get_json()

    user = create_user(data)

    # Retornamos o objeto que foi salvo
    return jsonify(user.serialize()), HTTPStatus.CREATED


@users_app.route('/users/<int:id>', methods=['GET'])
def get_by_id(id):
    user = get_user_by_id(id)
    return jsonify(user.serialize(full=True)), HTTPStatus.OK


@users_app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    delete_user(id)

    return jsonify(), HTTPStatus.NO_CONTENT


# Criar a rota /profiles/<id_do_perfil>
# Essa rota deverá aceitar o método PATCH
# Essa rota servirá para atualizar os dados do perfil do usuário
# first_name, last_name
@users_app.route('/profiles/<int:id>', methods=['PATCH'])
def update_profile(id):
    data = request.get_json()
    profile = update_user_profile(id, data)

    return jsonify(profile.serialize()), HTTPStatus.OK


@users_app.route('/users/<int:id>/accounts', methods=['POST'])
def post_account(id):
    data = request.get_json()
    """
    data = {
            "name": "Conta Corrente Viacredi"
        }
    """
    account = create_account(id, data)

    return jsonify(account.serialize()), HTTPStatus.CREATED

