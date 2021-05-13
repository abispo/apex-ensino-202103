# Migrations

É um histórico de alterações das tabelas do banco de dados. Elas evitam que para manter as models e as tabelas a elas associadas existam diferenças.
Utilizamos as migrations sempre que o estado das models se altera.
Alteração do estado das models pode ser:
* Criação de uma nova model.
* Alteração dos atributos de uma model (inserção, exclusão, etc)
* Remoção de uma model

Então, o fluxo seria o seguinte:
* Alteração do estado das models
* Geração de uma migration (arquivo de migração)
* Aplicação das alterações nesse arquivo no banco

---

# Exercício
### Modelar as entidades e relacionamentos de um sistema de agenda

* Criar o pacote `users`:
    * Criar o arquivo `models.py` e criar as seguintes classes:
        * `User`
            * id (inteiro, chave primária, auto incremento)
            * email (string, tamanho 255, não nulo)
            * passwd (string, tamanho 255, não nulo)
            * level (inteiro, valor padrão = 0)
            * __tablename__ = 'tb_users'
            
        * `UserProfile`
            * id(inteiro, chave primária)
            * first_name (string, tamanho 50, não nulo)
            * last_name (string, tamanho 100, não nulo)
            * birth_date (datetime, não nulo)  
            * __tablename__ = 'tb_users_profiles'
          
        * As models `User` e `UserProfile` terão um relacionamento 1:1 pelo campo ID.
* Criar o pacote `addresses`
    * Criar o arquivo `models.py` e criar as seguintes classes:
        * `Address` (representa o endereço). com os campos:
            * __tablename__ = 'tb_addresses'
            * id(inteiro, chave primária, auto incremento)
            * profile_id(inteiro, chave estrangeira para a model UserProfile)
            * address (string, tamanho 255, não nulo)
            * number (string, tamanho 10, não nulo)
            * city (string, tamanho(255), não nulo)
            * state (string, tamanho(255), não nulo)