<template>
  <div class="searchbar">
    <div class="searchbar__frame">
      <span class="searchbar__icon" v-html="lupeIcon"/>
      <input :value="modelValue" @input="handleUpdate($event)" class="searchbar__input"/>
    </div>
    <button class="searchbar__btn">Search</button>
  </div>
</template>

<script lang="ts" setup>
import lupeIcon from '/src/assets/lupe.svg?raw';
defineProps({
  modelValue: {
    type: String,
    required: false,
    default: ''
  }
});
const emit = defineEmits(['update:modelValue']);
const handleUpdate = (e: any) => emit('update:modelValue', e.target.value);
</script>

<style lang="scss" scoped src="./SearchBar.scss"/>