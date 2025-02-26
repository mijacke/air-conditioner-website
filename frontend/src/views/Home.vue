<template>
  <div>
    <!-- Hero Section with Featured Product -->
    <section class="relative bg-cover bg-center h-screen" style="background-image: url('https://via.placeholder.com/1920x1080');">
      <div class="absolute inset-0 bg-black opacity-50"></div>
      <div class="container mx-auto px-4 relative z-10 flex flex-col justify-center h-full text-center">
        <h1 class="text-white text-5xl md:text-6xl font-bold mb-4">Featured Air Conditioner</h1>
        <p class="text-white text-xl mb-8">Experience ultimate comfort with our top-of-the-line product.</p>
        <button @click="$router.push('/products')" class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-8 rounded-full text-xl transition duration-300">
          Load More Products
        </button>
      </div>
    </section>

    <!-- Cascade of Products Section -->
    <section class="container mx-auto px-4 py-16">
      <h2 class="text-4xl font-semibold text-center mb-12">Our Products</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
        <div v-for="product in products.slice(0,6)" :key="product.id" class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
          <img :src="product.image" alt="Product" class="w-full h-40 object-cover rounded mb-4" />
          <h3 class="text-2xl font-bold mb-2">{{ product.name }}</h3>
          <p>{{ product.description }}</p>
        </div>
      </div>
      <div class="text-center mt-8">
        <button @click="$router.push('/products')" class="bg-green-600 hover:bg-green-700 text-white py-2 px-6 rounded-full transition duration-300">
          View More Products
        </button>
      </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="bg-gray-100 py-16">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-4xl font-semibold mb-8">Why Choose Us?</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">Quality Products</h3>
            <p>Our air conditioners are built with premium materials ensuring lasting performance.</p>
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">Expert Service</h3>
            <p>Professional installation and repair services from experienced technicians.</p>
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-bold mb-2">Customer Satisfaction</h3>
            <p>Your comfort is our priority. We deliver unmatched service quality.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Team Section -->
    <section class="container mx-auto px-4 py-16">
      <h2 class="text-4xl font-semibold text-center mb-12">Meet Our Team</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
        <div v-for="member in team" :key="member.id" class="bg-white rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
          <img :src="member.image" alt="Team Member" class="w-32 h-32 object-cover rounded-full mx-auto mb-4" />
          <h3 class="text-2xl font-bold mb-2">{{ member.name }}</h3>
          <p class="text-gray-600">{{ member.role }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

interface Product {
  id: number
  name: string
  description: string
  image: string
}

interface TeamMember {
  id: number
  name: string
  role: string
  image: string
}

export default defineComponent({
  name: 'Home',
  setup() {
    const products = ref<Product[]>([
      { id: 1, name: "AC Model A", description: "Efficient and quiet air conditioner.", image: "/placeholder-400x300.png" },
      { id: 2, name: "AC Model B", description: "High performance for larger spaces.", image: "/placeholder-400x300.png" },
      { id: 3, name: "AC Model C", description: "Economical and stylish design.", image: "/placeholder-400x300.png" },
      { id: 4, name: "AC Model D", description: "Energy-saving with smart features.", image: "/placeholder-400x300.png" },
      { id: 5, name: "AC Model E", description: "Compact and powerful air conditioner.", image: "/placeholder-400x300.png" },
      { id: 6, name: "AC Model F", description: "Modern design with advanced cooling.", image: "/placeholder-400x300.png" }
    ])    
    const team = ref<TeamMember[]>([
      { id: 1, name: "Marcel Vasko", role: "CEO", image: "/placeholder_image.jpg" },
      { id: 2, name: "Mario Lassu", role: "CTO/Lead Engineer", image: "/placeholder_image.jpg" }, 
      { id: 3, name: "Placeholder Kijac", role: "", image: "/placeholder_image.jpg" }
    ])

    return { products, team }
  }
})
</script>
