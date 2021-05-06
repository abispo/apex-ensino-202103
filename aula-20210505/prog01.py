from database import cursor

if __name__ == '__main__':

    # O método execute() executa um comando SQL
    # Quem está usando sqlite é esse comando
    cursor.execute('PRAGMA table_list')

    # Quem está usando MySQL é esse comando
    cursor.execute('SHOW DATABASES')

    # O método fetchall() retorna todas as linhas geradas pelo comando executado
    # anteriormente
    response = cursor.fetchall()
    print(response)

    response = cursor.fetchone()

    # A linha abaixo retornará None, pois a posição do cursor no resultado está no final,
    # ou seja, precisamos "rebobinar" o cursor até a posição inicial. Fazemos isso
    # executando um novo comando SQL
    print(response)

    cursor.execute('SHOW DATABASES;')
    # fetchone() retorna apenas o primeiro resultado da consulta. Avança o cursor do resultado
    # 1 posição
    response = cursor.fetchone()
    print(response)

    response = cursor.fetchone()
    print(response)

    # fetchmany() traz a quantidade de resultados que for especificada como argumento. Avança
    # o cursor no resultado o número de vezes informado no argumento.
    response = cursor.fetchmany(2)
    print(response)
