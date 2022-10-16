<template>
  <nav class="navbar">
    <div class="navbar__head">
      <div @click="toggleBurger" class="navbar__burger">
        <svg  width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 16H28" stroke="#F3F3F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M4 8H28" stroke="#F3F3F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M4 24H28" stroke="#F3F3F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <div></div>
    </div>
    <div v-if="active" class="navbar__options">
      <div class="navbar-option">
        <div class="navbar-option__head">
          <div class="navbar-option__label">
            <svg width="32" height="23" viewBox="0 0 32 23" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.8 23V14.8824H19.2V23H27.2V12.1765H32L16 0L0 12.1765H4.8V23H12.8Z" fill="#F3F3F3"/>
          </svg>
            <h5>Home</h5>
          </div>
          <svg class="navbar-option__arrow" width="17" height="27" viewBox="0 0 17 27" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 23.8275L10.5074 13.5L0 3.1725L3.23482 0L17 13.5L3.23482 27L0 23.8275Z" fill="#F3F3F3"/>
          </svg>
        </div>
      </div>
      <div class="navbar-option">
        <div class="navbar-option__head">
          <div class="navbar-option__label">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M23.5782 11.7682L17.2073 0.708114C16.9309 0.236038 16.4655 0 16 0C15.5345 0 15.0691 0.236038 14.7927 0.724974L8.42182 11.7682H1.45455C0.654545 11.7682 0 12.5269 0 13.4542C0 13.6059 0.0145454 13.7576 0.0581818 13.9094L3.75273 29.5385C4.08727 30.9547 5.20727 32 6.54545 32H25.4545C26.7927 32 27.9127 30.9547 28.2618 29.5385L31.9564 13.9094L32 13.4542C32 12.5269 31.3455 11.7682 30.5455 11.7682H23.5782ZM11.6364 11.7682L16 4.34984L20.3636 11.7682H11.6364ZM16 25.2561C14.4 25.2561 13.0909 23.7387 13.0909 21.8841C13.0909 20.0295 14.4 18.5121 16 18.5121C17.6 18.5121 18.9091 20.0295 18.9091 21.8841C18.9091 23.7387 17.6 25.2561 16 25.2561Z" fill="#F3F3F3"/>
            </svg>
            <h5>Orders</h5>
          </div>
          <svg class="navbar-option__arrow" width="17" height="27" viewBox="0 0 17 27" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 23.8275L10.5074 13.5L0 3.1725L3.23482 0L17 13.5L3.23482 27L0 23.8275Z" fill="#F3F3F3"/>
          </svg>
        </div>
      </div>
      <div class="navbar-option">
        <div class="navbar-option__head">
          <div class="navbar-option__label">
            <svg width="32" height="25" viewBox="0 0 32 25" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M29.0909 0.735294C27.4764 0.220588 25.7018 0 24 0C21.1636 0 18.1091 0.588235 16 2.20588C13.8909 0.588235 10.8364 0 8 0C5.16364 0 2.10909 0.588235 0 2.20588V23.75C0 24.1176 0.363636 24.4853 0.727273 24.4853C0.872727 24.4853 0.945455 24.4118 1.09091 24.4118C3.05455 23.4559 5.89091 22.7941 8 22.7941C10.8364 22.7941 13.8909 23.3824 16 25C17.9636 23.75 21.5273 22.7941 24 22.7941C26.4 22.7941 28.8727 23.2353 30.9091 24.3382C31.0545 24.4118 31.1273 24.4118 31.2727 24.4118C31.6364 24.4118 32 24.0441 32 23.6765V2.20588C31.1273 1.54412 30.1818 1.10294 29.0909 0.735294ZM29.0909 20.5882C27.4909 20.0735 25.7455 19.8529 24 19.8529C21.5273 19.8529 17.9636 20.8088 16 22.0588V5.14706C17.9636 3.89706 21.5273 2.94118 24 2.94118C25.7455 2.94118 27.4909 3.16176 29.0909 3.67647V20.5882Z" fill="#F3F3F3"/>
            </svg>
            <h5>Catalog</h5>
          </div>
          <svg @click="toggleCatalog" class="navbar-option__arrow" :class="{ 'navbar-option__arrow--unfolded': catalogActive }" width="17" height="27" viewBox="0 0 17 27" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 23.8275L10.5074 13.5L0 3.1725L3.23482 0L17 13.5L3.23482 27L0 23.8275Z" fill="#F3F3F3"/>
          </svg>
        </div>
        <ul class="navbar-option__content" :class="{ 'navbar-option__content--unfolded': catalogActive }">
          <li class="navbar-option__suboption">Products</li>
          <li class="navbar-option__suboption">Categories</li>
          <li class="navbar-option__suboption">Discounts</li>
        </ul>
      </div>
      <div class="navbar-option">
        <div class="navbar-option__head">
          <div class="navbar-option__label">
            <svg width="32" height="23" viewBox="0 0 32 23" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M28.8 0H3.2C1.424 0 0.016 1.27937 0.016 2.875L0 20.125C0 21.7206 1.424 23 3.2 23H28.8C30.576 23 32 21.7206 32 20.125V2.875C32 1.27937 30.576 0 28.8 0ZM28.8 20.125H3.2V11.5H28.8V20.125ZM28.8 5.75H3.2V2.875H28.8V5.75Z" fill="#F3F3F3"/>
            </svg>
            <h5>Payments</h5>
          </div>
          <svg class="navbar-option__arrow" width="17" height="27" viewBox="0 0 17 27" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 23.8275L10.5074 13.5L0 3.1725L3.23482 0L17 13.5L3.23482 27L0 23.8275Z" fill="#F3F3F3"/>
          </svg>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const active = ref(false);

const toggleBurger = () => active.value = !active.value;

const catalogActive = ref(false);
const toggleCatalog = () => catalogActive.value = !catalogActive.value;

</script>

<style lang="scss" scoped src="./Navbar.scss"/>
