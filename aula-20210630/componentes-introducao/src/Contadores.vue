<template>
  <div>
      <h1>Contadores</h1>
      <hr>
      <!-- <app-contador v-for="n in 3" :key="n" /> -->
      <Contador v-for="n in 3" :key="n" />
  </div>
</template>

<script>
// Estamos registrando o componente Contador de maneira local no componente Contadores. Ou seja, ele só
// será acessado dentro desse componente, ficando indisponível nos outros componentes que não o importam.
import Contador from './Contador.vue'
export default {
//   components: { 'app-contador': Contador }
  components: { Contador }
}
</script>

<style>

</style>