from decorators import duplicar, titulo


@titulo(mostrar=False)
def diga_ola(nome):
    return f"Olá {nome}."


def diga_boa_noite(nome):
    return f"Boa noite, {nome}."


def diga_ola_para_maria(funcao_diga_ola):
    return funcao_diga_ola("Maria")


if __name__ == '__main__':

    print(diga_ola("João"))
    print(diga_ola_para_maria(diga_ola))
    print(diga_ola_para_maria(diga_boa_noite))

"""
SaaS

Software as a Service
"""