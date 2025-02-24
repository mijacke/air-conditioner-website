<template>
    <footer class="bg-gray-900 text-gray-300 py-8">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2025 AirCondPro. All rights reserved.</p>
        <p>Designed with passion and powered by modern technologies.</p>
        <div class="mt-4">
          <a href="mailto:info@aircondpro.com" class="hover:text-white mx-2">info@aircondpro.com</a>
          <span class="mx-2">|</span>
          <a href="tel:+18001234567" class="hover:text-white mx-2">+1 (800) 123-4567</a>
        </div>
      </div>
    </footer>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue'
  export default defineComponent({
    name: 'Footer'
  })
  </script>
  