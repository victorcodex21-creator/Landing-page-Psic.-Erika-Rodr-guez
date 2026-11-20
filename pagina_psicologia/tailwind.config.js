/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    extend: {
      colors: {
        petroleo: '#365B58',
        arena: '#EDE4D8',
        blanco: '#FAF8F4',
        gris: '#77736E',
        carbon: '#303735',
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        serif: ['Lora', 'serif'],
      },
      screens: { xs: '400px' },
    },
  },
};
