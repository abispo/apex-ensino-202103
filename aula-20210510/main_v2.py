from database import Base, engine, session
from models import User, Post, Profile, Tag, posts_tags

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    sair = False

    while not sair:

        mensagem = """
        ESCOLHA UMA OPÇÃO:

        0) SAIR
        1) Novo usuário
        2) Novo post
        3) Visualizar usuários
        4) Visualizar tags
        """

        print(mensagem)
        opcao = int(input("Opção: "))

        if opcao == 0:
            sair = True
            break

        elif opcao == 1:
            print("INFORME OS DADOS DO USUÁRIO: ")
            email = input("Informe o e-mail: ")
            login = input("Informe a login: ")
            senha = input("Informe a senha: ")

            user = User(
                email=email, login=login, passwd=senha
            )

            session.add(user)
            session.commit()

            print("Usuário criado. Informe os dados de perfil: ")
            first_name = input("Digite o nome: ")
            last_name = input("Digite o sobrenome: ")

            profile = Profile(
                id=user.id, first_name=first_name, last_name=last_name
            )

            session.add(profile)
            session.commit()

        elif opcao == 2:
            title = input("Título do post: ")
            body = input("Conteúdo (aperte ENTER para terminar): ")
            user_id = int(input("Informe o ID do autor do Post: "))

            post = Post(
                title=title, body=body, user_id=user_id
            )

            session.add(post)
            session.commit()

            print("Escolha as tags que serão associadas a esse Post: ")
            for tag in session.query(Tag).all():
                print(tag.name, end=', ')

            tags_list = input("Informe as tags (separadas por vírgula): ")

            for tag_name in tags_list.split(','):
                tag = session.query(Tag).filter(Tag.name==tag_name).first()

                if not tag:
                    tag = Tag(name=tag_name)
                    session.add(tag)
                    session.commit()


        elif opcao == 3:
            users_list = session.query(User.id, User.email, User.login).all()

            for user in users_list:
                message = f"""
                ID: {user.id}
                EMAIL: {user.email}
                LOGIN: {user.login}
                """

                print(message)

        elif opcao == 4:
            print("Lista de tags: ")
            for tag in session.query(Tag).all():
                print(tag.name, end=", ")
