from database import Base, engine
from models import *

if __name__ == '__main__':
    # Cria a base de dados e todas as models(tabelas) que estão associadas a
    # essa base
    Base.metadata.create_all(engine)
