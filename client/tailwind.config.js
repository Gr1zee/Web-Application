/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#1890ff', // Цвет Ant Design primary
      },
    },
  },
  plugins: [],
  corePlugins:{
    preflight: false
  },
}