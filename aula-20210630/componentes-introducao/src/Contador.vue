<template>
  <div>
      <button @click="contador++">+</button>
      <button @click="contador--">-</button>
    <p>Valor: <span class="spanContador">{{ contador }}</span></p>
  </div>
</template>

<script>
export default {
    // No caso de componentes, a propriedade data deve ser uma função que retorna um objeto, diferentemente da maneira que era feita
    // quando estávamos trabalhando apenas com uma página html
    data: function() {
        return {
            contador: 0
        }
    }
}
</script>

<style>
    .spanContador {
        background-color: coral;
}
</style>