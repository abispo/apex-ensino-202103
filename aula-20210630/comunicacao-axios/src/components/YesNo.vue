<template>
  <div>
      <h3>YesNo</h3>
      <p><button @click="pegarResposta()">Sim ou Não?</button></p>
      <p><button @click="limpar()">Limpar</button></p>
      <p>Resposta: <strong>{{ yesnoapi.answer }}</strong></p>
      <img :src="yesnoapi.image" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            yesnoapi: {
                answer: '',
                forced: '',
                image: ''
            }
        }
    },
    methods: {
        pegarResposta() {
            axios.get('https://yesno.wtf/api').then(response => {
                this.yesnoapi = response.data
            })
        },
        limpar() {
            this.yesnoapi = {}
        }
    },
    created() {
        // Fazemos uma requisição GET a api
        // Usamos o método then para capturar a resposta dessa requisição, e passamos essa
        // resposta para uma arrow function
        axios.get('https://yesno.wtf/api').then(response => {
            console.log(response)
        })

        this.$http.get('89036150').then(response => {
            console.log(response.data)
        })
    }

}
</script>

<style>

</style>