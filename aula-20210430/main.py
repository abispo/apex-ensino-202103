
# from funcionarios import FuncionarioCLT, FuncionarioTerceirizado, FuncionarioComissionado

from folha import FolhaDePagamento
from arquivos import ArquivoCSV

if __name__ == '__main__':
    arquivo_csv = ArquivoCSV('funcionarios.csv')

    arquivo_csv.abrir()
    arquivo_csv.ler()

    folha = FolhaDePagamento(arquivo_csv)
    folha.processar()

    folha.exibir_folha()

    arquivo_csv.fechar()
