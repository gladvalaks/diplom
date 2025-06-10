import { createRouter, createWebHistory } from 'vue-router'

import BasePage from '@/pages/BasePage.vue'
import ClientsPage from '@/pages/ClientsPage.vue'
import ConstructionsPage from '@/pages/ConstructionsPage.vue'
import ConstructionTypesPage from '@/pages/ConstructionTypesPage.vue'
import ContractorPage from '@/pages/ContractorPage.vue'

const routes = [
  {
    path: '/',
    component: BasePage,
    children: [
      {
        path: 'clients',
        name: 'clients',
        component: ClientsPage,
      },
      {
        path: 'constructions',
        name: 'constructions',
        component: ConstructionsPage,
      },
      {
        path: 'constructions-types-page',
        name: 'constructions-types-page',
        component: ConstructionTypesPage
      },
      {
        path: 'contractors-page',
        name: 'contractors-page',
        component: ContractorPage
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router