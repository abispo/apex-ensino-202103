<template>
  <div>
      <h2>Usuário</h2>
      <p>Nome: <strong>{{ nome }}</strong></p>
      <button @click="alterarNome()">Alterar nome</button>
      <p>Idade: {{ idade }}</p>
      <hr>
      <!-- Usando @nomeReiniciou capturamos o evento emitido no componente filho -->
      <!-- Conseguimos acessar o valor desse evento a partir de $event -->
      <AppInfoUsuario :nome="nome" :idade="idade" @nomeReiniciou="nome = $event.novo" :trocarFn="trocarNome"/>
      <!-- <VerUsuario :idade="idade" @idadeMudou="idade = $event" /> -->
      <VerUsuario :idade="idade" />
      <!-- Também conseguimos usar da seguinte maneira -->
      <!-- <app-info-usuario :nome="nome" @nomeReiniciou="nome = $event"/> -->

  </div>
</template>

<script>
// import absoluto
import InfoUsuario from '@/components/InfoUsuario.vue'
// import relativo
import VerUsuario from './VerUsuario.vue'

export default {
    components: {
        AppInfoUsuario: InfoUsuario,
        VerUsuario 
    },
    data() {
        return {
            nome: 'Maria',
            nomes: ['Maria', 'João', 'José'],
            idade: 20
        }
    },
    methods: {
        alterarNome() {
            // Math.floor(Math.random()*items.length)];
            // this.nome = this.nomes[Math.floor(Math.random()*this.nomes.length)]
            this.nome = 'Rafaella'
        },
        trocarNome() {
            this.nome = 'Lorena'
        }
    }
}
</script>


<style scoped>
    /* scoped impede que o estilo definido no componente pai eventualmente seja aplicado nos componentes filhos  */
    h2 {
        background-color: darksalmon;
    }
</style>