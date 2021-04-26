from datetime import date


class Pessoa:
    # Método construtor é o método chamado no momento em que o objeto é instanciado,
    # ou seja, é o método que define os valores iniciais dos atributos da nossa classe.
    def __init__(self, nome, data_de_nascimento):
        # No Python não existe o conceito de método/atributo privado. Nesse caso, por
        # convenção, indicamos que um método/atributo deve ser tratado como privado
        # colocando um underline na frente do seu nome
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento

    def get_nome(self):
        return self._nome


if __name__ == '__main__':

    maria = Pessoa("Maria", date(1990, 3, 20))
    lorena = Pessoa("Lorena", date(1989, 7, 8))

    print(maria._nome)

    print("fim")