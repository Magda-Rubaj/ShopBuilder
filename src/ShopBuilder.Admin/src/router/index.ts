import Products from '../views/Products.vue';

import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Products',
    component: Products
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
