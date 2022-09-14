import { createApp } from 'vue'
import App from './App.vue'
import store from './vuex/store' 
import router from './router/router'
import 'material-design-icons-iconfont'
//import './assets/styles/styles.scss'

const app = createApp(App)
app.use(store).use(router)
app.mount('#app')

