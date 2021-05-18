
def descendente(num):

    def filho01():
        return "Sou a função filho01"

    def filho02():
        return "Sou a função filho02"

    if num == 1:
        return filho01

    elif num == 2:
        return filho02


if __name__ == '__main__':

    primeiro = descendente(1)
    segundo = descendente(2)

    print(primeiro)
    print(segundo)

    print(primeiro)
    print(segundo)
