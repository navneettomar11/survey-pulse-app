import { createMemoryHistory, createRouter } from "vue-router"
import {Survey, HomeView} from "./components"


const routes = [
  { path: '/', component: HomeView },
  { path: '/create-survey', component: Survey },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
  linkActiveClass: 'bg-gray-900 text-white',
})

export default router;