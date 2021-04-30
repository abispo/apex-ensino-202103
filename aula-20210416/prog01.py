if __name__ == "__main__":
    print("Curso Python")

    nome_funcionario = "Joana"
    print(nome_funcionario)

    nome = 'José'
    frase = "Olá mundo"
    texto = """
        Primeira sentença
        Segunda sentença
        nome_funcionario
    """
    print(texto)

    # O comando abaixo gera uma lista de inteiros de 1 a 10
    lista_numeros = [numero for numero in range(1, 11)]
    print(lista_numeros)

    itens = [
        'Espada', 'Escudo', 'Mapa', 'Cantil', 'Poção de cura'
    ]

    calculo = 4 + 5 * \
              (4 ** 3) - \
              (10 / 2) - \
              (3 + 2)
    print(calculo)

    usuario = "Maria"

    if usuario == "Maria":
        print("Maria logada")
        print("ok")

    elif usuario == "Lorena":
        print("ok")
