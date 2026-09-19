/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    extend: {
      colors: {
        sage: { 50: '#F4F7F5', 100: '#EAF0EC', 200: '#D2E0D7', 500: '#6B8E7B', 600: '#587766', 700: '#466052', 800: '#374B40' },
        beige: { 50: '#FDFBF7', 100: '#F7F3EB', 200: '#EFEAE1', 300: '#E3DACD' },
        charcoal: { 800: '#2C3531', 900: '#1C2320' }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        serif: ['Lora', 'serif']
      },
      screens: { xs: '400px' }
    }
  }
};
