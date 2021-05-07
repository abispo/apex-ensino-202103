from database import cursor, db

if __name__ == '__main__':

    # Criar uma nova base de dados
    # Só para quem está usando MySQL
    comando = "CREATE DATABASE IF NOT EXISTS aula_20210505"
    cursor.execute(comando)

    # Definir a base de dados como padrão
    # Só para quem está usando MySQL
    comando = "USE aula_20210505"
    cursor.execute(comando)

    # Criar a tabela tb_users
    # No SQLite, definimos um campo como auto incremento usando AUTOINCREMENT
    comando_sqlite = """
        CREATE TABLE IF NOT EXISTS tb_users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            birth_date DATETIME
        )
    """
    comando = """
        CREATE TABLE IF NOT EXISTS tb_users(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(30) NOT NULL,
            email VARCHAR(50) NOT NULL,
            birth_date DATETIME
        )
    """
    cursor.execute(comando)

    # 1 -> Selecionar | 2 -> Inserir | 3 -> Apagar
    opcao = None

    opcao = int(input("Digite a opção(1 -> Selecionar | 2 -> Inserir | 3 -> Apagar): "))

    if opcao == 1:
        comando = "SELECT * FROM tb_users"
        cursor.execute(comando)
        response = cursor.fetchall()

        for user in response:
            print(user)

    elif opcao == 2:
        print("Insira dos dados do usuário a seguir")
        username = input("Informe o username: ")
        email = input("Informe o email: ")
        birth_date = input("Informe a data de nascimento no formato correto (YYYY-MM-DD): ")

        comando = f"""
            INSERT INTO tb_users(username, email, birth_date) VALUES(
                '{username}', '{email}', '{birth_date}'
            )
        """

        cursor.execute(comando)
        db.commit()

        print(f"{cursor.rowcount} linha(s) afetada(s).")

    # Implementar a opção 3 (Delete de usuário)
    # Deve-se informar via linha de comando o id do usuário a ser apagado
    elif opcao == 3:
        id_usuario = int(input("Informe o ID do usuário a ser apagado: "))

        comando = f"DELETE FROM tb_users WHERE id = {id_usuario}"

        cursor.execute(comando)
        db.commit()

        print(f"{cursor.rowcount} linha(s) afetada(s)")

