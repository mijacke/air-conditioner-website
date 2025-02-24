<template>
  <section class="container mx-auto px-4 py-16">
    <h2 class="text-4xl font-semibold text-center mb-12">Our Products</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
      <div
        v-for="product in products"
        :key="product.id"
        class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300"
      >
        <img
          :src="product.image"
          alt="Product"
          class="w-full h-40 object-cover rounded mb-4"
        />
        <h3 class="text-2xl font-bold mb-2">{{ product.name }}</h3>
        <p>{{ product.description }}</p>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

interface Product {
  id: number;
  name: string;
  description: string;
  image: string;
}

export default defineComponent({
  name: 'Products',
  setup() {
    const products = ref<Product[]>([
      { id: 1, name: "AC Model A", description: "Efficient and quiet air conditioner.", image: "https://via.placeholder.com/400x300" },
      { id: 2, name: "AC Model B", description: "High performance for larger spaces.", image: "https://via.placeholder.com/400x300" },
      { id: 3, name: "AC Model C", description: "Economical and stylish design.", image: "https://via.placeholder.com/400x300" },
      { id: 4, name: "AC Model D", description: "Energy-saving with smart features.", image: "https://via.placeholder.com/400x300" },
      { id: 5, name: "AC Model E", description: "Compact and powerful air conditioner.", image: "https://via.placeholder.com/400x300" },
      { id: 6, name: "AC Model F", description: "Modern design with advanced cooling.", image: "https://via.placeholder.com/400x300" },
      { id: 7, name: "AC Model G", description: "Durable and efficient performance.", image: "https://via.placeholder.com/400x300" },
      { id: 8, name: "AC Model H", description: "Innovative technology and design.", image: "https://via.placeholder.com/400x300" }
    ])
    return { products }
  }
})
</script>
