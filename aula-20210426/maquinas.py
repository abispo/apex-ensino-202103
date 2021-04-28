"""
* Definir uma classe que representará uma máquina de café. Regras
    * Para usarmos a máquina, ela deve estar ligada.
    * Para fazer o café, precisamos de água e pó de café.
    * Após isso, apertamos o botão "Fazer café".
    * Ao final de alguns segundos, o café estará pronto.
"""


class MaquinaDeCafe:

    def __init__(self):
        self._ligado = False
        self._qtd_agua = 0
        self._qtd_cafe = 0

    # Uma property faz um método de uma classe se comportar como um atributo
    # Nesse cenário, nossas properties servirão como getters e setters dos atributos da classe
    @property
    def ligado(self):
        return f"A máquina está {'Ligada' if self._ligado else 'Desligada'}."

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print("Máquina ligada.")
        else:
            print("A máquina já está ligada.")

    def desligar(self):
        if not self._ligado:
            print("A máquina já está desligada.")
        else:
            self._ligado = False
            print("Máquina desligada.")

    def colocar_agua(self, qtd):
        self._qtd_agua += qtd

    def colocar_cafe(self, qtd):
        self._qtd_cafe += qtd

    @property
    def nivel_agua(self):
        return self._qtd_agua

    @property
    def nivel_cafe(self):
        return self._qtd_cafe


if __name__ == '__main__':
    maquina = MaquinaDeCafe()
    print(maquina.ligado)
    maquina.ligar()

    # Colocar água e café
    maquina.colocar_agua(1)
    maquina.colocar_cafe(1)

    print(maquina.nivel_agua)
    print(maquina.nivel_cafe)

    print(maquina.nivel_cafe)
