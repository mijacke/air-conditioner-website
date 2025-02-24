<template>
    <section class="container mx-auto px-4 py-10">
      <h2 class="text-3xl font-semibold mb-4">Contact Us</h2>
      <p>Reach out for inquiries or to schedule a service.</p>
      <form class="max-w-lg mx-auto mt-6">
        <div class="mb-4">
          <label for="name" class="block mb-2">Name</label>
          <input type="text" id="name" class="w-full p-2 border rounded" />
        </div>
        <div class="mb-4">
          <label for="email" class="block mb-2">Email</label>
          <input type="email" id="email" class="w-full p-2 border rounded" />
        </div>
        <div class="mb-4">
          <label for="message" class="block mb-2">Message</label>
          <textarea id="message" rows="4" class="w-full p-2 border rounded"></textarea>
        </div>
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          Send
        </button>
      </form>
    </section>
  </template>
  