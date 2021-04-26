
class Cadeira:
    # Atributos de classe
    cor = "Preto"
    altura = 50

    # self é uma referência do objeto a ele mesmo
    def ajustar_altura(self, nova_altura):
        self._altura = nova_altura

    def identidade(self):
        return self


if __name__ == '__main__':
    # Sempre que formos instânciar uma classe, devemos chamá-la, assim como fazemos com as funções.
    cadeira1 = Cadeira()
    cadeira2 = Cadeira()

    print(id(cadeira1), cadeira2)
    print(id(cadeira1.identidade()))
    print(cadeira2.identidade())

    # f-string
    print(f"Cor da cadeira: {cadeira1.cor}")
    print(f"Altura da cadeira: {cadeira1.altura}")

    cadeira1.ajustar_altura(20)
    print(f"Nova altura da cadeira: {cadeira1.altura}")
