# Usamos o pacote csv sempre que quisermos trabalhar com arquivos .csv
# Comma separated values
import csv

if __name__ == '__main__':

    with open("funcionarios.csv", "r") as _file:
        # Utilizamos a função reader para ler um arquivo csv
        # Por padrão, o pacote csv considera a vírgula como delimitador dos campos
        # Nesse caso, temos que informar que o delimitador dos campos do nosso arquivo é ponto-e-vírgula
        csv_reader = csv.reader(_file, delimiter=';')

        for index, line in enumerate(csv_reader):
            if index == 0:
                continue
                # Aqui criaremos uma string usando f-strings
            texto = f"""
    ID      : {line[0]}
    Nome    : {line[1]}
    Salário : {line[2]}
    Setor   : {line[3]}
    Bônus   : {line[4]}
    """
            print(texto)
