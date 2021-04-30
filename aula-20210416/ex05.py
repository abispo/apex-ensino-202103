"""
Escreva um programa que leia um arquivo csv de registro de pedidos. Ao final, o programa mostrará a quantidade
total de pedidos, o valor total e a data/hora do último pedido (pedidos.csv)
"""
import csv
from datetime import datetime

if __name__ == '__main__':

    orders = []
    total_value = 0

    with open("pedidos.csv", "r") as _file:
        csv_reader = csv.DictReader(_file, delimiter=';')

        for line in csv_reader:
            orders.append(line)
            order_value = float(line['valor'].replace(',', '.'))
            total_value = total_value + order_value

    last_order = orders[-1]
    last_order_datetime = datetime.strptime(
        last_order['data'], "%Y%m%d"
    )

    print(f"Total de pedidos: {len(orders)}")
    print(f"Valor total dos pedidos: {total_value:.2f}")
    print(f"Data do último pedido: {last_order_datetime.strftime('%d-%m-%Y')}")
