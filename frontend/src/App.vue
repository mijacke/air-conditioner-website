<script>
export default {
  data() {
    return {
      message: 'Loading...'
    };
  },
  async created() {
    try {
      console.log("Fetching from Flask API...");
      const response = await fetch('http://127.0.0.1:5000/api/hello');
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      this.message = data.message;
      console.log("Flask response:", data);
    } catch (error) {
      console.error('Error fetching data:', error);
      this.message = 'Error loading data';
    }
  }
}
</script>

<template>
  <div>
    <h1>Test Vue.js Frontend</h1>
    <h2>Mario Lassu</h2>
    <p>Flask API says: "{{ message }}"</p>
  </div>
</template>
