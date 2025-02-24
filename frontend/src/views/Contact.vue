<template>
  <section class="container mx-auto px-4 py-16">
    <h2 class="text-4xl font-semibold mb-8 text-center">Contact Us</h2>
    <div class="flex flex-col md:flex-row justify-center items-start gap-8">
      <div class="md:w-1/2">
        <form class="bg-white p-8 rounded-lg shadow-md">
          <div class="mb-6">
            <label for="name" class="block text-lg font-medium mb-2">Name</label>
            <input type="text" id="name" class="w-full border border-gray-300 p-3 rounded focus:outline-none focus:border-blue-500" />
          </div>
          <div class="mb-6">
            <label for="email" class="block text-lg font-medium mb-2">Email</label>
            <input type="email" id="email" class="w-full border border-gray-300 p-3 rounded focus:outline-none focus:border-blue-500" />
          </div>
          <div class="mb-6">
            <label for="message" class="block text-lg font-medium mb-2">Message</label>
            <textarea id="message" rows="5" class="w-full border border-gray-300 p-3 rounded focus:outline-none focus:border-blue-500"></textarea>
          </div>
          <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-full transition duration-300 w-full">
            Send Message
          </button>
        </form>
      </div>
      <div class="md:w-1/2">
        <div class="bg-gray-100 p-8 rounded-lg shadow-md">
          <h3 class="text-2xl font-bold mb-4">Get in Touch</h3>
          <p class="mb-4">For inquiries or service requests, contact us:</p>
          <p class="mb-2"><strong>Email:</strong> info@aircondpro.com</p>
          <p class="mb-2"><strong>Phone:</strong> +1 (800) 123-4567</p>
          <p class="mb-2"><strong>Address:</strong> 123 Main St, City, Country</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'Contact'
})
</script>
