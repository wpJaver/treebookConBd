<template>
  <div style="background-color: #fefbfb; padding: 2rem 0">
    <!-- TEXTO CON IMAGEN -->
    <b-container>
      <b-row>
        <!-- Texto banner -->
        <b-col class="banner">
          <h1 class="banner-titulo">
            Get started your exciting
            <span class="color-naranja">journey</span> with us.
          </h1>
          <p>
            A Team of experienced tourism professionals will provide you with
            the best advice and tips for your desire place.
          </p>
          <button class="btn" id="banner-boton">Discovery Now</button>
        </b-col>
        <!-- Imagen banner -->
        <b-col>
          <img src="../assets/img banner 2.png" alt="Banner principal" />
        </b-col>
      </b-row>
    </b-container>

    <!-- MENU -->
    <b-container id="menu">
      <b-row id="menu-row">
        <b-col v-for="(option, index) in data" :key="index" class="menu-col">
          <!-- <template> -->
          <b-form-input
            list="my-list-id"
            :placeholder="option.name"
            id="menu-text"
          ></b-form-input>
          <datalist id="my-list-id">
            <option v-for="(item, index2) in option.options_list" :key="index2">
              {{ item }}
            </option>
          </datalist>
          <span>{{ option.text }}</span>
          <!-- </template> -->
        </b-col>
        <b-col>
          <b-button class="btn" id="boton-header">Explore Now</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
export default {
  name: "MainBanner",
  props: {
    data: Array,
  },
  data() {
    return {
      data_options: [
        {
          name: "Location",
          text: "Where are you doing",
          options_list: ["op1", "op2", "op3"],
        },
        {
          name: "Date",
          text: "Where are you doing2",
          options_list: ["op4", "op5", "op6"],
        },
        {
          name: "Guest",
          text: "Where are you doing3",
          options_list: ["op7", "op8", "op9"],
        },
      ],
    };
  },
};
</script>
<style>
.banner {
  margin-top: 5rem;
  display: flex;
  flex-direction: column;
}
.banner-titulo {
  font-family: "Volkhov", serif;
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 70px;
}

.color-naranja {
  color: #fa7436;
}

#banner-boton {
  box-sizing: border-box;
  background: #ffffff;
  color: #fa7436;
  border: 1px solid #fa7436;
  border-radius: 5px;
  width: 35%;
}

#banner-boton:hover {
  color: white;
  background: #fa7436;
}
#menu {
  margin-top: 3rem;
  width: 60%;
  background: white;
  border-radius: 1rem;
}
#menu.row {
  align-items: center;
}

.menu-col {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  align-items: center;
}

#menu-text {
  border: none;
  width: 50%;
}

#menu-text::placeholder {
  color: black;
  font-weight: bold;
}
</style>
