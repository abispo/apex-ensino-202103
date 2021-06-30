import Vue from 'vue'
import App from './App.vue'
import Contadores from './Contadores.vue'

Vue.config.productionTip = false
// Dessa maneira estamos registrando o componente Contadores de maneira global, ou seja, ele estará
// disponível em qualquer outro componente do nosso projeto a partir da tag <contadores />
Vue.component('contadores', Contadores)

new Vue({
  render: h => h(App),
}).$mount('#app')
