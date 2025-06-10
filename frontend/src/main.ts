import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { VueQueryPlugin, QueryClient } from '@tanstack/vue-query';
import router from '@/router';

const queryClient = new QueryClient()

const app = createApp(App)

app.use(VueQueryPlugin, { queryClient }).use(router).mount('#app')
