import { createStore } from 'vuex'
import { axiosBase } from './axios-base'

export default createStore({
  state: {
    accessToken: localStorage.getItem('access_token') || null, // To hold the state of the user even if they reload the page
    refreshToken: localStorage.getItem('refresh_token') || null,
    APIData: '' // It hold the response data from the backend
  },
  getters: {
    loggedIn(state){
      return state.accessToken != null
    }
  },
  mutations: {
    updateLocalStorage(state, {access, refresh }){
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_toke', refresh)
      state.accessToken = access
      state.refreshToken = refresh
    },
    updateAccess (state, access) {
      state.accessToken = access
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
    }
  },
  actions: {
    refreshToken: function (context) {
      return new Promise((resolve, reject) => {
        axios.post('/api/token/refresh/', {
          refresh: context.state.refreshToken
        }) // sending the refresh token to the backend
        .then (response => {
          // If backend sent new Tokens then update the store
          console.log("New access toke successfuly generated.")
          context.commit('updateAccess', response.date.access)
          resolve(response.data.access)
        })
        .catch(err => {
          console.log("There occured an error in refreshing token")
          reject(err) // error generating the refresh token
        })
      })
    },
    registerUser: function (context, data) {
      return new Promise((resolve, reject) => {
        axiosBase.post('/register/', {
          fname: data.name,
          lname: data.lname,
          emial: data.email,
          username: data.username,
          password: data.password
        })
        .then (response => {
          resolve(response)
        })
        .catch (err => {
          reject(err)
        })
      })
    },
    logoutUser: function (context) {
      if (context.getters.loggedIn){
        return new Promise((resolve, reject) => {
          axiosBase.post('/api/token.logout/')
          .then (response => {
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            context.commit('destroyToken')
          })
          .catch(err => {
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            context.commit('destroyToken')
            resolve(err)
          })
        })
      }
    },
    loginUser: function (context, credentials) {
      return new Promise((resolve, reject) => {
        // sending credentials to the backend
        axiosBase.post('/api/token', {
          username: credentials.username,
          password: credentials.password
        })
        // If successful
        .then(response => {
          context.commit('updateLocalStorage', {access: response.data.access, refresh: response.data.refresh})
          resolve()
        })
        .catch(err => {
          reject(err)
        })
      })
    }
  },
  modules: {
  }
})
