<template>
    <nav class="bg-white shadow">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <div class="text-xl font-bold">AirCondPro</div>
        <div class="space-x-4">
          <router-link to="/" class="text-gray-600 hover:text-blue-600">Home</router-link>
          <router-link to="/services" class="text-gray-600 hover:text-blue-600">Services</router-link>
          <router-link to="/about" class="text-gray-600 hover:text-blue-600">About</router-link>
          <router-link to="/contact" class="text-gray-600 hover:text-blue-600">Contact</router-link>
        </div>
      </div>
    </nav>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue'
  export default defineComponent({ name: 'Navbar' })
  </script>
  