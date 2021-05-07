
from datetime import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    # A propriedade __tablename__ serve pra definir o nome da tabela no banco de dados
    # que será mapeada para essa classe
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    login = Column(String(20), nullable=False)
    passwd = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

