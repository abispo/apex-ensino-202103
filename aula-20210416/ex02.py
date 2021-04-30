"""
Escreva um programa que vai receber nomes até o usuário digitar "sair". Então o programa vai pedir o diretório onde o
usuário deseja salvar o arquivo. O programa vai salvar esses nomes em um arquivo .txt dentro do diretório escolhido.
"""
import os

if __name__ == '__main__':

    value = ""
    values_list = []

    while value.upper() != "SAIR":
        # A função input() recebe valores digitados pelo terminal
        # input() sempre retorna o valor como string
        value = input("Digite algum nome: ")
        values_list.append(value)

    values_list.pop()

    dir_name = input("Informe o diretório onde deseja salvar o arquivo: ")

    # exists() verifica se um arquivo ou um diretório existem no sistema de arquivos.
    if not os.path.exists(dir_name):

        # a função mkdir() do pacote os cria um novo diretório, desde que ele não exista
        # Se ele existir, é gerado um FileExistsError
        os.mkdir(dir_name)

    # join() "concatena" os caminhos definidos
    full_path = os.path.join(
        # dirname() retorna o caminho completo até o diretório onde o arquivo atual está sendo executado.
        # __file__ é uma variável especial do Python que indica o caminho completo do arquivo atualmente executado.
        os.path.dirname(__file__), dir_name, 'names.txt'
    )

    # Abrimos o arquivo no modo escrita (w)
    with open(full_path, "w") as _file:
        for value in values_list:
            _file.write(f"{value}\n")
