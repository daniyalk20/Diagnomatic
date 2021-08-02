
module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
      ? '/Diagnomatic/'
      : '/',
      // https://cli.vuejs.org/config/#devserver-proxy
  devServer: {
    port: 3000,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        ws: true,
        changeOrigin: true,
      },
    },
  },
  
  lintOnSave: false
  }