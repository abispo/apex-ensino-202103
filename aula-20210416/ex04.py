# Escreva um programa que receba via terminal os registros de uma compra (codigo, nome e valor).
# E salve esses registros em um arquivo .csv.
import csv

if __name__ == '__main__':

    products = []
    headers = ["code", "name", "cost"]

    for _ in range(3):

        code = input("Digite o código do produto: ")
        name = input("Digite o nome do produto: ")
        cost = input("Digite o valor do produto")

        products.append(
            {'code': code, 'name': name, 'cost': cost}
        )

    with open("ex04.csv", "w", newline='') as _file:
        csv_writer = csv.DictWriter(_file, delimiter=";", fieldnames=headers)

        # writeheader() salva os cabeçalhos no arquivo
        csv_writer.writeheader()

        csv_writer.writerows(products)
