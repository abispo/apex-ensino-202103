from decorators import apenas_horario_comercial


def meu_decorator(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper


@apenas_horario_comercial
def grite():
    """
    Apenas grita.
    :return: None
    """
    print("AAAAAAAAAAhhhhhhhhhhh")


if __name__ == '__main__':

    gritando = meu_decorator(grite)
    gritando()
    print(gritando)
