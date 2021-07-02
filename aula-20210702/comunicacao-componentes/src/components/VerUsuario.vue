<template>
  <div>
      <h2>Ver Usuário</h2>
      <p>Idade: {{ idadeLocal }}</p>
      <button @click="alterarIdade()">Alterar Idade</button>
  </div>
</template>

<script>
// Utilizando @, fazemos o import absoluto do componente/lib, ou seja, importamos um objeto a partir do diretório raiz
// da aplicação, ou seja, do diretório src
import barramento from '@/barramento'
export default {
    props: {
        idade: {
            type: Number
        }
    },
    data() {
        return {
            idadeLocal: this.idade
        }
    },
    methods: {
        alterarIdade() {
            this.idadeLocal = 40
            barramento.$emit('idadeMudou', this.idadeLocal)
        }
    }
}
</script>

<style>

</style>