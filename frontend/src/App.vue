<template>
  <div>
    <Navbar />
    <!-- The router-view will load the corresponding page (Home, Services, etc.) -->
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Navbar from './components/Navbar.vue';

export default defineComponent({
  name: 'App',
  components: { Navbar }
});
</script>
