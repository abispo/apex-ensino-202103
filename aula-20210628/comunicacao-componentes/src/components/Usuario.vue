<template>
  <div>
      <h2>Usuário</h2>
      <p>Nome: <strong>{{ nome }}</strong></p>
      <button @click="alterarNome()">Alterar nome</button>
      <hr>
      <InfoUsuario :nome="nome" />
  </div>
</template>

<script>
import InfoUsuario from './InfoUsuario.vue'

export default {
    components: { InfoUsuario },
    data() {
        return {
            nome: 'Maria'
        }
    },
    methods: {
        alterarNome() {
            this.nome = 'Rafaella'
        }
    }
}
</script>

<style>

</style>