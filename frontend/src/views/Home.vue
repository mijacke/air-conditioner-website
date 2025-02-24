<template>
  <div>
    <!-- Hero Section -->
    <section class="relative bg-cover bg-center h-screen" style="background-image: url('https://via.placeholder.com/1920x1080');">
      <div class="absolute inset-0 bg-black opacity-50"></div>
      <div class="container mx-auto px-4 relative z-10 flex flex-col justify-center h-full">
        <h1 class="text-white text-5xl md:text-6xl font-bold mb-4">Experience Ultimate Comfort</h1>
        <p class="text-white text-xl mb-8">Premium Air Conditioning Sales, Repair, and Assembly Services</p>
        <a href="#services" class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-8 rounded-full text-xl transition duration-300">
          Discover Our Services
        </a>
      </div>
    </section>

    <!-- Services Section -->
    <section class="container mx-auto px-4 py-16" id="services">
      <h2 class="text-4xl font-semibold text-center mb-12">Our Services</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
          <h3 class="text-2xl font-bold mb-2">Sales</h3>
          <p>Explore our range of high-quality air conditioning units designed for efficiency and comfort.</p>
        </div>
        <div class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
          <h3 class="text-2xl font-bold mb-2">Repair</h3>
          <p>Expert repair services to ensure your systems run smoothly and reliably at all times.</p>
        </div>
        <div class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
          <h3 class="text-2xl font-bold mb-2">Assembly</h3>
          <p>Professional assembly and installation services for optimal performance and safety.</p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-300 py-8">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2025 AirCondPro. All rights reserved.</p>
        <p>Designed with passion and powered by modern technologies.</p>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'Home'
});
</script>
