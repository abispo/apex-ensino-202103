# Flask

Flask é um microframework web. Ele é assim definido pois com ele não são fornecidas muitas ferramentas/bibliotecas, por exemplo:
* Não há uma camada de abstração do banco de dados (ORM do Django por exemplo)
* Nenhuma forma de validação de formulários.
* Nenhuma outra lib de tarefas comuns do desenvolvimento web

Apesar disso, Flask vem com 2 componentes:
* Wekzeug: É a lib responsável por criar os objetos de request e response.
* Jinja2: É a biblioteca de templates do Flask.

## Instalação
* Com pipenv:
`````python
pipenv install flask
`````

## Executando a aplicação
O flask vem com uma ferramenta de linha de comando para executar os projetos, chamada `flask`. Antes de usá-la, precisamos definir 2 variáveis de ambiente:
* FLASK_APP: Definimos qual será o `entrypoint` da nossa aplicação, ou seja, o primeiro módulo que será chamado na nossa aplicação.
* FLASK_ENV: Define o environment onde a nossa aplicação vai ser executada.

Para definir essas variáveis, fazemos da seguinte maneira:
* No Linux
    ````bash
    $ export FLASK_APP=main.py
    $ export FLASK_ENV=development
    $ flask run
    ````
* No windows
    ````
    set FLASK_APP=main.py
    set FLASK_ENV=development
    flask run
    ````

