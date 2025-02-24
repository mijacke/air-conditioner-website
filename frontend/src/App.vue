<template>
  <div>
    <Navbar />
    <Home />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Navbar from './components/Navbar.vue'
import Home from './components/Home.vue'

export default defineComponent({
  name: 'App',
  components: { Navbar, Home }
})
</script>
