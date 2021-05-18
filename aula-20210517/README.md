# Projeto

Montar um cadastro de usuário utilizando uma chamada a API de cep (https://api.postmon.com.br/v1/cep/)
Pelo terminal, o usuário vai digitar o nome, o sobrenome e o CEP. 

## Informações a serem salvas (model User)
* Nome
* Sobrenome
* Logradouro (API)
* Bairro (API)
* Cidade (API)
* UF (API)
* CEP

## Decorator de Log
Além de salvar os dados na tabela de usuários, vamos registrar cada chamada a API. Para isso, vamos
utilizar um decorator que vai pegar o horário de início e de fim da requisição, e os dados que
foram trazidos

````python
@log        # decorator
def buscar_dados(data):
    ...
````

Os dados de log, vão ser salvos em uma tabela de logs, que vai precisar ter os seguintes campos:
* id
* timestamp de início da requisição
* timestamp de fim da requisição
* os dados que foram trazidos