from http import HTTPStatus

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# Usando a classe SQLAlchemy configuramos a ferramenta na nossa instância do Flask.
db = SQLAlchemy(app)

# Dessa maneira, configuramos o alembic no nosso projeto
# Antes de inicializar a estrutura do alembic, precisamos definir a variável de ambiente
# FLASK_APP como sendo o arquivo que será executado. Nesse caso: FLASK_APP=main.py
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'tb_users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    profile = db.relationship("Profile", uselist=False, back_populates="user")

    def serialize(self, full=False):

        dict_fields = {
            'id': self.id,
            'email': self.email
        }

        if full:
            dict_fields.update({
                # como profile é o objeto relacionado a User, temos acesso aos atributos
                # e métodos normalmente
                'profile': self.profile.serialize()
            })

        return dict_fields


class Profile(db.Model):
    __tablename__ = 'tb_profiles'

    id = db.Column(db.Integer(), db.ForeignKey('tb_users.id'), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    user = db.relationship("User", uselist=False, back_populates="profile")

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


@event.listens_for(User, 'after_insert')
def create_profile_after_user_save(mapper, connection, target):     # target = instancia de User
    profile = Profile()
    profile.user = target

    db.session.add(profile)

# Routes
# http://127.0.0.1:5000/users
@app.route('/users', methods=['GET'])
def list_all_users():
    all_users = [user.serialize() for user in User.query.all()]
    return jsonify(all_users), HTTPStatus.OK


@app.route('/users', methods=['POST'])
def create_user():
    # Capturamos os dados enviados pelo cliente
    data = request.get_json()

    # Instanciamos a classe User, passando como parâmetros os valores enviados
    user = User(email=data.get('email'), password=data.get('password'))

    # Adicionamos a instância de User à sessão
    db.session.add(user)

    # Persistimos(salvamos) os dados na tabela tb_users
    db.session.commit()

    # Retornamos o objeto que foi salvo
    return jsonify(user.serialize()), HTTPStatus.CREATED


@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return jsonify(message="Usuário não encontrado."), HTTPStatus.NOT_FOUND
    return jsonify(user.serialize(full=True)), HTTPStatus.OK


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    user = User.query.get(id)
    if user is None:
        return jsonify(message="Usuário não encontrado."), HTTPStatus.NOT_FOUND

    db.session.delete(user)
    db.session.commit()

    return jsonify(), HTTPStatus.NO_CONTENT


# Criar a rota /profiles/<id_do_perfil>
# Essa rota deverá aceitar o método PATCH
# Essa rota servirá para atualizar os dados do perfil do usuário
# first_name, last_name
@app.route('/profiles/<int:id>', methods=['PATCH'])
def update_profile(id):
    data = request.get_json()
    profile = Profile.query.get(id)

    profile.first_name = data.get('first_name')
    profile.last_name = data.get('last_name')

    db.session.add(profile)
    db.session.commit()

    return jsonify(profile.serialize()), HTTPStatus.OK


if __name__ == '__main__':
    app.run()
