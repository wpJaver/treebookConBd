<template>
  <div class="NavBar" style="background-color: #fefbfb">
    <b-navbar toggleable="lg" type="dark">
      <b-navbar-brand href="#">
        <img alt="Vue logo" src="../assets/Logo.png" style="margin-left: 1%" />
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <div></div>
        <b-navbar-nav class="custom-nav">
          <b-nav-item href="#">Home</b-nav-item>
          <b-nav-item href="#">About</b-nav-item>
          <b-nav-item href="#">Destination</b-nav-item>
          <b-nav-item href="#">Tour</b-nav-item>
          <b-nav-item href="#">Blog</b-nav-item>
        </b-navbar-nav>
        <div>
          <b-button id="login-header"> Login </b-button>
          <b-button id="boton-header"> Sign up </b-button>
        </div>
      </b-collapse>
    </b-navbar>

    <router-view />
  </div>
</template>

<script></script>

<style>
nav.navbar {
  margin: 0 1%;
}
#nav-collapse {
  justify-content: space-between;
}

.custom-nav li a {
  color: black;
}
.nav-link:hover,
.nav-link:focus {
  font-weight: bold;
  color: black;
}
#login-header {
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  text-align: right;
  color: #fd8d3a;
  border: none;
  background: none;
  margin-right: 5rem;
}
#boton-header {
  background: #fa7436;
  color: white;
  box-shadow: 0px 8px 16px rgba(250, 116, 54, 0.24);
  border-radius: 5px;
  border: none;
  padding: 0.7rem 2rem;
}
#boton-header:hover {
  background: #ffffff;
  color: #fa7436;
  border: 1px solid #fa7436;
}
</style>
