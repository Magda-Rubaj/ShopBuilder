<template>
  <div>
    <Navbar/>
    <main>
      Content
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from './components/Navbar.vue';
</script>

<style>
  main {
    padding-top: calc(4em + 36px);
  }

  @media screen and (min-width: 768px) {
    main {
      padding-top: 0;
      padding-left: 300px;
    }
  }
</style>
