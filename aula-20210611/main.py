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







if __name__ == '__main__':
    app.run()
