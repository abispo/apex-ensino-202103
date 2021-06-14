from flask import Flask

from database import db, migrate
from app.users.views import users_app
from app.accounts.views import accounts_app


def create_app():

    app = Flask(__name__)

    # Carrega as configurações do arquivo settings.py
    app.config.from_object('settings')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(users_app)
    app.register_blueprint(accounts_app)

    return app
