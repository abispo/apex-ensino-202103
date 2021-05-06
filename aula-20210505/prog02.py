from database import cursor

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
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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

