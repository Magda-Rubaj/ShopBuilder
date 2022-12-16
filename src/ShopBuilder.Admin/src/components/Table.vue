<template>
  <div class="table">
    <div class="table__controls">
      <span v-html="filterIcon"/>
      <SearchBar/>
    </div>
    <div class="table__content">
      <table class="table__table">
        <thead class="table__head">
          <th>ID</th>
          <th>Image</th>
          <th>Name</th>
          <th>Category</th>
          <th>Price (Tax excl.)</th>
          <th>Price (Tax incl.)</th>
          <th>Quantity</th>
          <th>Description</th>
        </thead>
        <tbody class="table__body">
          <tr>
            <td>1</td>
            <td>img.jpg</td>
            <td>S1</td>
            <td>Biodegradable</td>
            <td>3.99 $</td>
            <td>5 $</td>
            <td>999</td>
            <td>Better send it back</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="table__pagination">Insert premade pagination component</div>
  </div>
</template>

<script lang="ts" setup>
import SearchBar from './SearchBar.vue';
import filterIcon from '/src/assets/filter.svg?raw';

</script>

<style lang="scss" scoped src="./Table.scss"/>