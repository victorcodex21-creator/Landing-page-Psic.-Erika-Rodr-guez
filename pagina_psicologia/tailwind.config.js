/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    extend: {
      colors: {
        sage: { 50: '#FAF8F4', 100: '#EDE4D8', 200: '#dcd0c0', 500: '#365B58', 600: '#2a4744', 700: '#203a37', 800: '#303735' },
        beige: { 50: '#FAF8F4', 100: '#F4EFE9', 200: '#EDE4D8', 300: '#dcd0c0' },
        charcoal: { 800: '#303735', 900: '#1C2320' }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        serif: ['Lora', 'serif']
      },
      screens: { xs: '400px' }
    }
  }
};
