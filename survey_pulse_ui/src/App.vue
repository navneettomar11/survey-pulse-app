<script setup lang="ts">
  import {Header, Footer} from './components';
  import { RouterView } from 'vue-router';
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <Header/>
    <main class="flex-grow p-4">
      <!--content-->
      <RouterView/>
    </main>
    <Footer/>
  </div>
</template>