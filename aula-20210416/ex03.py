# Escreva um programa que leia um arquivo CSV e imprima o nome das colunas, depois todos os
# registros (pedidos.csv)
import csv

if __name__ == '__main__':

    with open("pedidos.csv", "r") as _file:
        csv_reader = csv.DictReader(_file, delimiter=';')

        headers = csv_reader.fieldnames

        print(headers)

        for line in csv_reader:

            for value in line.values():
                print(f"{value} ", end=" | ")
            print()
