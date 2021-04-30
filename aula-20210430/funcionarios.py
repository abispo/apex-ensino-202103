from uuid import uuid4


class Funcionario:

    def __init__(self, nome):
        self._id = str(uuid4())
        self._nome = nome
        self._salario = 0

    def calcular_salario(self):
        pass

    def info(self):
        return f"""
        ID: {self._id}
        Nome: {self._nome}
        Salário: {self._salario}
        """


# Herdamos as características (atributos/métodos) da classe Pai/Base, que nesse caso
# é a classe Funcionario
class FuncionarioCLT(Funcionario):

    # O argumento id terá como valor padrão o id gerado automaticamente pela função
    # uuid4()
    def __init__(self, nome, salario):
        # O built-in super() serve para acessarmos métodos e atributos da classe base, que eventualmente tenha sido
        # sobrescrimos na classe filha
        super().__init__(nome)

        if not isinstance(salario, int) and not isinstance(salario, float):
            raise Exception("O argumento salario deve ser do tipo numérico (int ou float)")
        self._salario = salario


class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome, qtd_horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self._qtd_horas_trabalhadas = qtd_horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_salario(self):
        self._salario = self._qtd_horas_trabalhadas * self._valor_hora


# valor salario = valor_total_vendas * (porcentagem_comissao / 100)
class FuncionarioComissionado(Funcionario):

    def __init__(self, nome, valor_total_vendas, porcentagem_comissao):
        super().__init__(nome)
        self._valor_total_vendas = valor_total_vendas
        self._porcentagem_comissao = porcentagem_comissao

    def calcular_salario(self):
        self._salario = self._valor_total_vendas * (self._porcentagem_comissao / 100)


class FuncionarioSecreto(Funcionario):

    def info(self):
        return f"""
        As informações do funcionário {self._nome} são confidenciais.
        """
