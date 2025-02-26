import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: process.env.NODE_ENV === "development"
      ? {
          "/api": {
            target: "http://127.0.0.1:10000",
            changeOrigin: true,
            secure: false,
          },
        }
      : undefined,
  },
  define: {
    __API_URL__: JSON.stringify(
      process.env.NODE_ENV === "production"
        ? "https://air-conditioner-website.onrender.com"
        : "http://127.0.0.1:10000"
    )
  }
})
