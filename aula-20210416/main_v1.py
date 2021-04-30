
if __name__ == '__main__':

    # Abrimos um arquivo com o built-in open()
    _file = open("funcionarios.csv", "r")

    # O método read() ele retorna o conteúdo do arquivo como uma string.
    # O cursor do arquivo vai parar no final
    file_content = _file.read()
    print(file_content)

    # O método tell() indica a posição atual do cursor dentro do arquivo
    print(_file.tell())

    # O método seek() permite que reposicionemos o cursor em qualquer posição que desejarmos
    # Nesse caso, vamos reposicionar o cursor no início do arquivo
    _file.seek(0)

    # read() aceita um argumento n, que é o número de caracteres que desejamos retornar
    file_content = _file.read()
    print(file_content)

    _file.seek(0)
    print("*"*40)

    # readline() lê uma linha inteira do arquivo
    print(_file.readline())

    # readline() aceita um argumento numérico que indica a quantidade de caracteres que vamos ler dessa linha.
    print(_file.readline(10))

    _file.seek(0)

    # Um objeto do tipo file é iterável, ou seja, podemos usar o for para acessar o seu conteúdo.
    # Quando iteramos sobre um arquivo, cada linha é considerada um item
    # Nesse exemplo, mostramos apenas a quinta linha do arquivo.
    for contador, line in enumerate(_file):
        if contador >= 5:
            break


    # readlines() retorna o conteúdo do arquivo como uma lista de strings (cada item da lista correspondendo)
    # a uma linha

    _file.seek(0)
    file_content = _file.readlines()
    print(file_content)

    # readlines() recebe um argumento numérico que representa a quantidade de linhas que se deseja retornar
    _file.seek(0)
    file_content = _file.readlines(28)
    print(file_content)

    # O atributo closed nos informa se o arquivo foi ou não fechado.
    print(_file.closed)

    # O método close() fecha a conexão com o arquivo.
    _file.close()

    print(_file.closed)


    # O comando with é usado pelo gerenciador de contexto para criar um novo contexto de execução
    # Essa é a maneira ideal de se trabalhar com arquivos, pois ao final da execução do contexto, o arquivo
    # é fechado de forma automática
    with open("funcionarios.csv", "r") as _file:
        print(_file.readlines())
        # print(_file.closed)

    _file.close()

    print(_file.closed)
