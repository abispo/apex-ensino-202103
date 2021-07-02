<template>
  <div>
    <h1>Comunicação</h1>
    <hr>
    <Usuario />
  </div>
</template>

<script>
import Usuario from './components/Usuario.vue'

export default {
  components: { Usuario }
}
</script>

<style>
  h1 {
    text-align: center;
  }
</style>