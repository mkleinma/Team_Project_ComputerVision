<script setup>
import { ref, computed } from 'vue'
import Home from './index.html'
import VueRouter from 'vue-router'
import SmallDS from './index_small_ds.html'
Vue.use(VueRouter);

const routes = {
  '/': Home,
  '/smallds': SmallDS
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
const router = new VueRouter({
  routes // short for `routes: routes`
});

</script>


<template>
  <a href="#/">Home</a> |
  <a href="#/smallds">SmallDS</a> |
  <component :is="currentView" /> 
</template>
</script>

<style>

.btn-cta {
  background-color: #d0d0d5;
  border-width: 3px;
  border-color: #1b1b32;
  border-radius: 0;
  border-style: solid;
  color: #1b1b32;
  display: block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 18px;
  line-height: 1.42857143;
}

.btn-cta:active:hover, .btn-cta:focus, .btn-cta:hover {
  background-color: #1b1b32;
  border-width: 3px;
  border-color: #000;
  background-image: none;
  color: #f5f6f7;
}

</style>