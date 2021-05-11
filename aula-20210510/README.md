# ORM
## Object Relational Mapper
Mapeia classes no nosso código para tabelas no banco de dados. Dessa maneira, não precisamos escrever código SQL para fazer operações no banco de dados, mas somente código da própria linguagem. Exemplos:

* Python: SQLAlchemy, ORM Django, Peewee
* PHP: Doctrine
* C#: Entity Framework

# Exercícios
* Criar a model `Comment`, que representará os comentários em um Post.
* O nome da tabela será `tb_comments`
* Os campos devem ser os seguintes:
    * id, inteiro, chave primária, auto incremento
    * user_id, inteiro, chave estrangeira para a tab
    * text, string de tamanho 255, não pode ser nulo
    * created_at, datetime timestamp, não pode ser nulo
* `Comment` terá uma ligação 1:1 para `User`
* `User` terá uma ligação 1:N para `Comment`
* `Comment` terá uma ligação 1:1 para `Post`
* `Post` terá uma ligação 1:N para `Comment`
* Criar os campos tipo `relationship` para `User` e `Post`.