
from funcionarios import (
    FuncionarioCLT, FuncionarioTerceirizado, FuncionarioComissionado
)


class FolhaDePagamento:

    def __init__(self, arquivo_csv):
        self._arquivo_csv = arquivo_csv
        self._lista_de_funcionarios = []

    def processar(self):
        for linha in self._arquivo_csv.linhas:

            funcionario = None
            tipo_funcionario = int(linha.get('tipo_funcionario'))

            if tipo_funcionario == 1:
                funcionario = FuncionarioCLT(
                    linha.get('nome'), float(linha.get('salario'))
                )
            elif tipo_funcionario == 2:
                funcionario = FuncionarioTerceirizado(
                    linha.get('nome'),
                    float(linha.get('qtd_horas_trabalhadas')),
                    float(linha.get('valor_hora'))
                )
            elif tipo_funcionario == 3:
                funcionario = FuncionarioComissionado(
                    linha.get('nome'),
                    float(linha.get('valor_total_vendas')),
                    float(linha.get('porcentagem_comissao'))
                )
            else:
                raise Exception("Tipo de funcionário incorreto.")

            funcionario.calcular_salario()
            self._lista_de_funcionarios.append(funcionario)

    def exibir_folha(self):
        print("*** FOLHA DE PAGAMENTO ***")
        for funcionario in self._lista_de_funcionarios:
            print(funcionario.info())
        print("*** FIM DA FOLHA DE PAGAMENTO ***")