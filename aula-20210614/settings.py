import os

database = os.path.join(os.getcwd(), 'db.sqlite3')

SQLALCHEMY_DATABASE_URI = f'sqlite:///{database}'

