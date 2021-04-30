
# from funcionarios import FuncionarioCLT, FuncionarioTerceirizado, FuncionarioComissionado
from funcionarios_new import (
    FuncionarioCLT,
    FuncionarioTerceirizado,
    FuncionarioComissionado,
    FuncionarioSecreto
)
from folha import FolhaDePagamento

if __name__ == '__main__':

    maria = FuncionarioCLT("Maria", 2000)
    carla = FuncionarioCLT("Carla", 1800)

    fabio = FuncionarioTerceirizado("Fabio", 190, 45)

    vanessa = FuncionarioComissionado("Vanessa", 10000, 25)
    bruno = FuncionarioComissionado("Bruno", 12000, 10)

    valdir = FuncionarioSecreto("Valdir")
    denis = FuncionarioSecreto("Denis")

    folha_de_pagamento = FolhaDePagamento([maria, carla])
    folha_de_pagamento.adicionar_funcionario(fabio)
    folha_de_pagamento.adicionar_funcionario(vanessa)
    folha_de_pagamento.adicionar_funcionario(bruno)
    folha_de_pagamento.adicionar_funcionario(valdir)
    folha_de_pagamento.adicionar_funcionario(denis)

    folha_de_pagamento.processar()
    folha_de_pagamento.exibir_folha()