<template>
  <div>
      <h3>Info usuário</h3>
      <p>Nome: {{ nome }}</p>
  </div>
</template>

<script>
export default {
    // Utilizando props conseguimos receber algum tipo de informação enviada pelo componente pai
    // props: ['nome']
    props: {
        // Podemos validar as props antes do componente as receber
        nome: {
            type: String,       // Indicamos que o tipo da props nome deve ser String
            // required: true      // Indicamos que a prop nome deve ser passada obrigatoriamente
            default: 'Anônimo'  // Indicamos o valor padrão caso a prop não seja passada
        }
    }
}
</script>

<style>

</style>