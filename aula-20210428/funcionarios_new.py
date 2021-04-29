from uuid import uuid4




class FuncionarioCLT:

    # O argumento id terá como valor padrão o id gerado automaticamente pela função
    # uuid4()
    def __init__(self, nome, salario):
        self._id = str(uuid4())
        self._nome = nome
        if not isinstance(salario, int) and not isinstance(salario, float):
            raise Exception("O argumento salario deve ser do tipo numérico (int ou float)")
        self._salario = salario

    def info(self):
        text_info = f"""
        ID: {self._id}
        Nome: {self._nome}
        Salário: {self._salario}
        """
        return text_info


class FuncionarioTerceirizado:

    def __init__(self, nome, qtd_horas_trabalhadas, valor_hora):
        self._id = str(uuid4())
        self._nome = nome
        self._qtd_horas_trabalhadas = qtd_horas_trabalhadas
        self._valor_hora = valor_hora
        self._salario = 0

    def calcular_salario(self):
        self._salario = self._qtd_horas_trabalhadas * self._valor_hora

    def info(self):
        text_info = f"""
        ID: {self._id}
        Nome: {self._nome}
        Salário: {self._salario}
        """
        return text_info


# valor salario = valor_total_vendas * (porcentagem_comissao / 100)
class FuncionarioComissionado:

    def __init__(self, nome, valor_total_vendas, porcentagem_comissao):
        self._id = str(uuid4())
        self._nome = nome
        self._valor_total_vendas = valor_total_vendas
        self._porcentagem_comissao = porcentagem_comissao
        self._salario = 0

    def calcular_salario(self):
        self._salario = self._valor_total_vendas * (self._porcentagem_comissao / 100)

    def info(self):
        text_info = f"""
        ID: {self._id}
        Nome: {self._nome}
        Salário: {self._salario}
        """
        return text_info









