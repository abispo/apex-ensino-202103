
# 1. Escreva um programa que conte quantas linhas existem em um arquivo .txt (arquivo.txt)

if __name__ == '__main__':

    # read
    with open("funcionarios.csv", "r") as _file:
        _lines = _file.readlines()

    print(len(_lines))
