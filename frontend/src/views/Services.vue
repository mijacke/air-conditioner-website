<template>
  <section class="container mx-auto px-4 py-16">
    <h2 class="text-4xl font-semibold mb-12 text-center">Our Services</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white p-8 rounded-lg shadow-lg transform hover:scale-105 transition duration-300">
        <h3 class="text-2xl font-bold mb-4">Sales</h3>
        <p>We offer a wide range of high-quality air conditioning units tailored to your needs.</p>
      </div>
      <div class="bg-white p-8 rounded-lg shadow-lg transform hover:scale-105 transition duration-300">
        <h3 class="text-2xl font-bold mb-4">Repair</h3>
        <p>Our expert technicians provide fast and reliable repair services to ensure optimal performance.</p>
      </div>
      <div class="bg-white p-8 rounded-lg shadow-lg transform hover:scale-105 transition duration-300">
        <h3 class="text-2xl font-bold mb-4">Assembly</h3>
        <p>Professional installation services to guarantee safe and efficient setup of your system.</p>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'Services'
})
</script>
