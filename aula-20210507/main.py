from database import Base, engine, session
from models import *
from sqlalchemy import func

if __name__ == '__main__':
    # Cria a base de dados e todas as models(tabelas) que estão associadas a
    # essa base
    Base.metadata.create_all(engine)

    # Selecionar todos os dados da tb_users
    # O método all() retorna todos os registros da tabela mapeada a classe
    # SELECT * FROM tb_users
    response = session.query(User).all()

    # 1 - Instanciar o objeto a ser persistido(salvo) na tabela
    # maria = User(
    #     login='mariazinha', email='maria@gmail.com', passwd='dkf93u9sf'
    # )

    # 2 - Adicionar esse objeto a sessão do banco
    # session.add(maria)

    # 3 - Commitar as alterações no banco de dados
    # session.commit()

    print("LISTA DE USUÁRIOS")
    for user in response:
        info = f'''
        ID: {user.id}
        Login: {user.login}
        Email: {user.email}
        '''

        print(info)

        # O método get seleciona um registro usando o valor informado e comparando
        # com a chave primária da tabela
        # SELECT * FROM tb_users WHERE id = 1
        # maria = session.query(User).get(1)
        #
        # session.delete(maria)
        # session.commit()


        