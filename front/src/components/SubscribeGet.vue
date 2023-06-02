<template>
  <div class="subscribe">
    <b-container>
      <b-row class="subscribe-row">
        <b-col>
          <h1 class="suscribete-titulo">
            Subscribe and get exclusive <br />
            deals & offer
          </h1>
        </b-col>
        <b-col align="center">
          <input-group id="suscribete-fondo-input">
            <img
              src="../assets/email-logo.png"
              alt=""
              style="width: 5%; height: 5%"
            />
            <b-input
              type="text"
              class="form-control"
              id="suscribete-input"
              placeholder="Enter your mail"
              aria-label="Recipient's username"
              aria-describedby="button-addon2"
            />
            <b-button class="btn" id="suscribete-boton">subscribe</b-button>
          </input-group>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<style>
.subscribe {
  background: url("../assets/bacground-suscribete.png");
  padding: 7rem;
  background-repeat: no-repeat;
  background-position: center;
}
.subscribe-row {
  flex-direction: column;
}
.suscribete-titulo {
  font-family: "Volkhov";
  font-weight: 700;
  font-size: 48px;
  text-align: center;
  color: #ffffff;
}
#suscribete-fondo-input {
  background: white;
  border-radius: 10px;
  padding: 1%;
  display: flex;
  align-items: center;
  width: 50%;
}
#suscribete-input {
  border: none;
  background: none;
  font-family: "Poppins";
  font-weight: 400;
  font-size: 16px;
  color: #999999;
  outline: none;
}
#suscribete-input:focus {
  outline: none;
}
#suscribete-boton {
  background: #fa7436;
  border-radius: 8px;
  font-family: "Poppins";
  font-weight: 400;
  font-size: 16px;
  color: #ffffff;
}
#suscribete-boton:hover {
  background: #ffffff;
  color: #fa7436;
  border: 1px solid #fa7436;
}
</style>
