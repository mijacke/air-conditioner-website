<template>
    <section class="container mx-auto px-4 py-10">
      <h1 class="text-4xl font-bold mb-4">Professional Air Conditioning Services</h1>
      <p class="text-lg mb-6">
        We offer sales, repair, and assembly services for top-quality air conditioners.
      </p>
      <img src="https://via.placeholder.com/1200x600" alt="Air Conditioning" class="w-full rounded shadow" />
    </section>
  </template>
  <template>
    <div>
      <!-- Hero / Header Section -->
      <header class="relative bg-cover bg-center h-screen" style="background-image: url('https://via.placeholder.com/1920x1080');">
        <div class="absolute inset-0 bg-black opacity-60"></div>
        <div class="container mx-auto px-4 relative z-10 flex flex-col justify-center h-full">
          <!-- Top info bar -->
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <img src="https://via.placeholder.com/100x100" alt="Logo" class="w-16 h-16 mr-4 rounded-full border-2 border-white" />
              <div>
                <h1 class="text-white text-5xl font-bold">AirCondPro</h1>
                <p class="text-white text-xl mt-1">Your Partner in Comfort</p>
              </div>
            </div>
            <div class="hidden md:block">
              <p class="text-white">Call us: <span class="font-semibold">+1 (800) 123-4567</span></p>
            </div>
          </div>
          <!-- Navigation -->
          <nav class="mt-8">
            <ul class="flex flex-wrap justify-center space-x-8 text-white text-lg">
              <li><router-link to="/" class="hover:underline">Home</router-link></li>
              <li><router-link to="/services" class="hover:underline">Services</router-link></li>
              <li><router-link to="/about" class="hover:underline">About</router-link></li>
              <li><router-link to="/contact" class="hover:underline">Contact</router-link></li>
            </ul>
          </nav>
          <!-- Call-to-Action Button -->
          <div class="mt-12 text-center">
            <a href="#find-online" class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-8 rounded-full text-xl transition duration-300">
              Find Us Online
            </a>
          </div>
        </div>
      </header>
  
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
  
      <!-- Find Us Online Section -->
      <section class="bg-gray-100 py-16" id="find-online">
        <div class="container mx-auto px-4">
          <h2 class="text-4xl font-semibold text-center mb-8">Connect With Us</h2>
          <div class="flex flex-col md:flex-row justify-around items-center">
            <div class="mb-6 md:mb-0">
              <h3 class="text-2xl font-bold mb-2">Facebook</h3>
              <a href="#" class="text-blue-600 hover:underline">facebook.com/AirCondPro</a>
            </div>
            <div class="mb-6 md:mb-0">
              <h3 class="text-2xl font-bold mb-2">Twitter</h3>
              <a href="#" class="text-blue-400 hover:underline">@AirCondPro</a>
            </div>
            <div class="mb-6 md:mb-0">
              <h3 class="text-2xl font-bold mb-2">Instagram</h3>
              <a href="#" class="text-pink-600 hover:underline">@AirCondPro</a>
            </div>
            <div>
              <h3 class="text-2xl font-bold mb-2">LinkedIn</h3>
              <a href="#" class="text-blue-700 hover:underline">AirCondPro on LinkedIn</a>
            </div>
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
  import { defineComponent } from 'vue'
  export default defineComponent({
    name: 'Home'
  })
  </script>
  
  <style scoped>
  /* You can add additional custom CSS here if needed */
  </style>
  