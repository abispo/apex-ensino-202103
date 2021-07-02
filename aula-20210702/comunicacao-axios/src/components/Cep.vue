<template>
  <div>
      <p>
          <label for="txtCep">CEP: </label>
          <input type="text" id="txtCep" v-model="cep">
      </p>
      <p>
          <button @click="obterEndereco()">Consultar</button>
          <button @click="limparEndereco()">Limpar</button>
      </p>
      <hr>
      <div v-if="infoCep.cidade">
          <h3>Informações do Endereço</h3>
          <ul>
              <li>Logradouro: <strong>{{ infoCep.logradouro }}</strong>.</li>
              <li>Bairro: <strong>{{ infoCep.bairro }}</strong>.</li>
              <li>Cidade: <strong>{{ infoCep.cidade }}</strong>.</li>
              <li>Estado: <strong>{{ infoCep.estado }}</strong>.</li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            cep: '',
            infoCep: {}
        }
    },
    methods: {
        obterEndereco() {
            this.$http.get(this.cep).then(
                // arrow function / função anônima
                response => {
                    this.infoCep = response.data
                }
            )
        },
        limparEndereco() {
            this.cep = ''
            this.infoCep = {}
        }
    }
}
</script>

<style>

</style>