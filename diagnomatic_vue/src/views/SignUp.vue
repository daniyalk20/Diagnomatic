<template>
<div class="main-container">
  <div class="login-form">
    <form>
        <h2 class="text-center">Create an Account</h2>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="First Name" v-model="fname" required="required">
        </div>  
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Last Name" v-model="lname" required="required">
        </div>   
        <div class="form-group">
            <input type="email" class="form-control" placeholder="johndoe@example.com" v-model="email" required="required">
        </div>      
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Username" v-model="username" required="required">
        </div>
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Password" v-model="password" required="required">
        </div>
        <div class="form-group">
            <input type="password" class="form-control" placeholder="Repeat Password" v-model="rpassword" required="required">
        </div>
        <div class="clearfix">
            <label class="float-left form-check-label"><input type="checkbox"> Remember me</label>
        </div>  
        <div class="form-group">
            <button class="btn btn-block login-btn" @click="loginUser">Sign Up</button>
        </div>    
        <div class="text-center">
            <p>Already have an account? 
            <router-link href="#" to="Login">Login</router-link></p>
        </div>
        <p v-if='isWrong' class="danger">Alert Message!</p>
    </form>
</div>
</div>
</template>

<script>
export default {
  name: 'SignUp',
  components: {

  },
  data() {
    return {
      fname: '',
      lname: '',
      email: '',
    username: '',
    password:'',
    rpassword: '',
    isWrong: false
    };
  },
  methods: {
    loginUser: function() {
      this.$store.dispatch('signUp', {
        fname: this.fname,
        lname: this.lname,
        email: this.email,
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
