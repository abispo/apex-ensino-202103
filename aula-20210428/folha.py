

class FolhaDePagamento:

    def __init__(self, lista_de_funcionarios=[]):
        self._lista_de_funcionarios = lista_de_funcionarios
        # maria, fabrio, carla, vanessa

    def adicionar_funcionario(self, funcionario):
        self._lista_de_funcionarios.append(funcionario)

    def processar(self):
        for funcionario in self._lista_de_funcionarios:
            funcionario.calcular_salario()

    def exibir_folha(self):
        print("*** FOLHA DE PAGAMENTO ***")
        for funcionario in self._lista_de_funcionarios:
            print(funcionario.info())
        print("*** FIM DA FOLHA DE PAGAMENTO ***")