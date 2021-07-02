<template>
  <div>
    <h1>Comunicação HTTP com axios</h1>
    <hr>
    <!-- <YesNo /> -->
    <Cep />
  </div>
</template>

<script>
// import YesNo from './components/YesNo.vue'
import Cep from '@/components/Cep.vue'

export default {
  components: {
    // YesNo,
    Cep
  },
}
</script>

<style>
  h1 {
    text-align: center;
    font-family: sans-serif;
  }
  button {
    margin-left: 5px;
  }

</style>