# Sistema de Folha de Pagamento

No nosso sistema de folha de pagamento, existem 3 tipos de funcionários:
* Funcionário CLT: Recebe um valor fixo de salário.
* Funcionário Terceirizado: Tem seu salário definido como a quantidade de horas trabalhadas x o valor da hora.
* Funcionário Comissionado: Tem seu salário definido como uma porcentagem do valor total de vendas que ele realizou.

O Sistema de folha de pagamento deve calcular o salário de cada funcionário seguindo as regras acima descritas.

Todo funcionário possui um nome e um código identificador (id).

* Criar um método chamado salvar_folha na classe FolhaDePagamento
* Esse método vai salvar a folha de pagamento calculada em um novo arquivo csv chamado salarios.csv
* Esse arquivo terá a seguinte estrutura:
````csv
id;nome;salario
7058a2d0-3ba6-4bff-af6a-f64e63a253cb;Helena;2349.13
````
* Deve-se criar um método na classe ArquivoCSV chamado salvar
* Esse método vai receber a lista de registros que devem ser salvos (incluindo o cabeçalho do arquivo)