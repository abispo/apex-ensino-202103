<template>
  <div>
      <h3>Info usuário</h3>
      <p>Nome: {{ nome }}</p>
      <p>Idade: {{ idade }}</p>
      <button @click="reiniciarNome()">Reiniciar nome</button>
      <!-- Quando o botão abaixo for clicado, chamamos a função que foi passada pelo componente pai -->
      <button @click="trocarFn()">Trocar nome</button>
  </div>
</template>

<script>
import barramento from '@/barramento'
export default {
    // Utilizando props conseguimos receber algum tipo de informação enviada pelo componente pai
    // props: ['nome']
    props: {
        // Podemos validar as props antes do componente as receber
        nome: {
            type: String,       // Indicamos que o tipo da props nome deve ser String
            // required: true      // Indicamos que a prop nome deve ser passada obrigatoriamente
            default: 'Anônimo'  // Indicamos o valor padrão caso a prop não seja passada
        },
        idade: {
            type: Number
        },
        trocarFn: Function
    },
    methods: {
        reiniciarNome() {
            // Com o $emit emitimos um evento personalizado
            // onClick, onMouseOver, onMouseDown
            this.$emit('nomeReiniciou', {
                novo: 'Maria', antigo: this.nome
            })
        }
    },
    // Método de ciclo de vida chamado automaticamente quando o componente é criado
    created() {
        // Atribuímos ao componente um listener para o evento 'idadeMudou'. Ou seja, o componente ficará 'escutando'
        // esse evento e irá executar o código dentros das chaves sempre que esse evento for disparado
        barramento.$on('idadeMudou', idade => { this.idade = idade})
    }
}
</script>

<style>

</style>