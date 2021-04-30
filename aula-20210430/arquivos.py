import csv


class ArquivoCSV:

    def __init__(self, nome):
        self._nome = nome
        self._arquivo = None
        self._linhas = []

    def abrir(self):
        self._arquivo = open(self._nome, 'r')

    def fechar(self):
        self._arquivo.close()

    def ler(self):
        leitor_csv = csv.DictReader(self._arquivo, delimiter=';')
        for linha in leitor_csv:
            self._linhas.append(linha)

    @property
    def linhas(self):
        return self._linhas
