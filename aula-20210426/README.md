
# Programação Orientada a Objetos (POO, OOP)

Programação orientada a objetos é um dos paradigmas de programação mais utilizados. Um paradigma seria uma estrutura de organização e as regras de desenvolvimento. Existem 3 principais paradigmas de programaçao:
* Procedural/Estruturado: Definimos a organização do nosso código como um conjunto de funções
* Orientado a Objetos: Paradigma onde o conceito central é o objeto, sendo o objeto uma representação de uma entidade do mundo real.
* Funcional: Paradigma onde tudo são funções.

Terminologia básica da programação orientada a objetos
* Objeto: A instância de uma classe, ou uma entidade criada a partir de uma classe.
* Classe: É o modelo a partir do qual criamos/instanciamos os nossos objetos. Aqui definimos as características da classe e o comportamento dos objetos instanciados a partir dessa classe.
* Atributo: São características da entidade representada por uma determinada classe.
* Métodos: São as ações que um objeto pode tomar. Além disso, os métodos podem alterar o estado do próprio objeto.

Existem alguns pilares que definem o que é Orientação a Objetos. Que são eles:

* Abstração: É o processo onde selecionamos apenas os detalhes relevantes de uma entidade e ignoramos quaisquer detalhes internos de implementação.
* Encapsulamento: É o processo onde cada objeto mantém um estado interno que só pode ser acessado e/ou modificado pelo próprio objeto. Nesse processo definimos uma série de métodos públicos, onde a partir destes alteramos o estado.
* Herança: É a capacidade de uma classe herdar características(atributos/métodos) de uma outra classe.
* Polimorfismo: É a capacidade de uma classe filha definir as próprias características/ações e mesmo assim compartilhar as funcionalidades da classe pai/base

## 1 Exercício
* Definir uma classe que representará uma máquina de café. Regras
    * Para usarmos a máquina, ela deve estar ligada.
    * Para fazer o café, precisamos de água e pó de café.
    * Após isso, apertamos o botão "Fazer café".
    * Ao final de alguns segundos, o café estará pronto.