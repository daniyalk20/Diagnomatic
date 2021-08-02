<template>
<div class="main-body">
  <nav class="navbar navbar-expand-lg navbar-dark">
    <a class="navbar-brand" href="/">Diagnomatic</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link class="nav-link" :to="{ path: 'pneumonia' }">Pneumonia</router-link>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <router-link class="btn btn-outline-success my-2 my-sm-0" type="submit" to="/login">Login</router-link>
      </form>
    </div>
  </nav>
  <div class="main-container">
  <router-view/>
  </div>
  <footer class="footer">
      <div>
        <span class="text-muted">All Rights Reserved by <a href="">Diagnomatic</a></span>
      </div>
    </footer>
</div>
</template>

<style lang="scss">
@import '../node_modules/bootstrap';
.navbar{
  background-color: #25476a;
}
.footer{
  background-color: #25476a;
  text-align: center;
  color: whitesmoke;
}
.main-container{
  min-height: 89vh;
}
</style>
