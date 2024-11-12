// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  router: {
    extendRoutes(routes) {
      routes.push({
        path: '/',
        redirect: '/home', 
      });
    },
  },
  css: [
    'bootstrap/dist/css/bootstrap.min.css'
  ]
})
