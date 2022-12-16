<template>
  <div class="products">
    <header>
      <p class="products__breadcrumb">Catalog / Products</p>
      <BaseHeader>Products</BaseHeader>
    </header>
    <div class="products__table">
      <Table/>
    </div>

  </div>
</template>

<style lang="scss" src="./Products.scss" scoped/>

<script lang="ts" setup>
import BaseHeader from '../components/BaseHeader.vue';
import Table from '../components/Table.vue';

</script>
