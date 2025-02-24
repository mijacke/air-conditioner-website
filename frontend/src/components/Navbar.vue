<template>
    <header class="bg-white shadow-lg">
      <div class="container mx-auto px-4 py-4 flex items-center justify-between">
        <!-- Logo & Title -->
        <div class="flex items-center">
          <img src="https://via.placeholder.com/100x100" alt="Logo" class="w-12 h-12 mr-2 rounded-full border border-gray-200" />
          <span class="text-2xl font-bold text-gray-800">AirCondPro</span>
        </div>
        <!-- Hamburger Button (Mobile) -->
        <button @click="toggleMenu" class="md:hidden focus:outline-none">
          <svg class="w-6 h-6 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"></path>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
        <!-- Navigation Links -->
        <nav :class="{'block': isOpen, 'hidden': !isOpen}" class="w-full md:block md:w-auto">
          <ul class="flex flex-col md:flex-row md:space-x-8">
            <li>
              <router-link @click="closeMenu" to="/" class="block py-2 text-gray-700 hover:text-blue-600">
                Home
              </router-link>
            </li>
            <li>
              <router-link @click="closeMenu" to="/services" class="block py-2 text-gray-700 hover:text-blue-600">
                Services
              </router-link>
            </li>
            <li>
              <router-link @click="closeMenu" to="/about" class="block py-2 text-gray-700 hover:text-blue-600">
                About
              </router-link>
            </li>
            <li>
              <router-link @click="closeMenu" to="/contact" class="block py-2 text-gray-700 hover:text-blue-600">
                Contact
              </router-link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'Navbar',
    setup() {
      const isOpen = ref(false);
      const toggleMenu = () => { isOpen.value = !isOpen.value; };
      const closeMenu = () => { isOpen.value = false; };
      return { isOpen, toggleMenu, closeMenu };
    }
  });
  </script>
  