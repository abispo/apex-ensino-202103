import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

if os.getenv('DATABASE_TYPE') == 'mysql':
    db_host = os.getenv('DATABASE_HOST')
    db_user = os.getenv('DATABASE_USER')
    db_passwd = os.getenv('DATABASE_PASSWD')
    db_name = os.getenv('DATABASE_NAME')

    connection_string = f'mysql+pymysql://{db_user}:{db_passwd}@{db_host}/{db_name}'


elif os.getenv('DATABASE_TYPE') == 'sqlite':

    database_file = os.path.join(
        os.getcwd(), f"{os.getenv('DATABASE_NAME')}.sqlite3"
    )

    connection_string = f"sqlite:///{database_file}"

# create_engine retorna um objeto engine, que é o objeto responsável por estabelecer a conexão ao banco de dados.
# O argumento echo=True vai imprimir no terminal os comandos SQL que serão executados
engine = create_engine(connection_string, echo=True)

# declarative_base retorna a classe base onde todas as classes do nosso projeto vão herdar, pois dessa maneira
# elas serão mapeadas para as tabelas no banco.
Base = declarative_base()

# Criando o objeto se sessão. É por meio desse objeto que executamos as operações na base de dados
Session = sessionmaker(bind=engine)
session = Session()
