<template>
<div class="main-container">
  <div class="login-form">
    <form>
        <h2 class="text-center">Forgot Password</h2>       
        <div class="form-group">
            <input type="email" class="form-control" placeholder="Email" v-model="username" required="required">
        </div>
        <div class="form-group">
            <button class="btn btn-block login-btn" @click="loginUser">Send Password</button>
        </div>
        <div class="text-center">
            <router-link to="Login">Login</router-link> | <router-link to="SignUp">Sign Up</router-link>
        </div>      
        <p v-if='isWrong'>Email not registered!</p>
    </form>
</div>
</div>
</template>

<script>
export default {
  name: 'ForgotPassword',
  components: {

  },
  data() {
    return {
    email: '',
    isWrong: false
    };
  },
  methods: {
    loginUser: function() {
      this.$store.dispatch('forgotpassword', {
        username: this.username,
        password: this.password
      })
      .then(() => {
        this.isWrong = false
        this.$router.push({ name: 'Login' })
      })
      .catch(err => {
        console.log(err)
        this.isWrong = true
      })
    }
  }
}
</script>



<style scoped>
.main-container{
  background: url('~@/assets/img/login-bg.jpg') no-repeat center center fixed;
  
}
.login-btn{
  background-color: #25476a;
  color: whitesmoke;
}
.login-form {
  
    width: 340px;
    margin: auto;
  	font-size: 15px;
    min-height: 100%;
}
.login-form form {
    margin-bottom: 15px;
    background: #f7f7f7;
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    padding: 30px;
}
.login-form h2 {
    margin: 0 0 15px;
}
.form-control, .btn {
    min-height: 38px;
    border-radius: 2px;
}
.btn {        
    font-size: 15px;
    font-weight: bold;
}

.main-body{
  background: url('~@/assets/img/login-bg.jpg') no-repeat center center fixed;
}
</style>
