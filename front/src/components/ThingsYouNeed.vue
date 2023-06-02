<template>
  <div style="background: #f7f8fc">
    <b-container class="things">
      <b-row>
        <h1 class="titulo">
          Things you need <span class="color-naranja"> to do </span>
        </h1>
      </b-row>
      <b-row>
        <p>
          We ensure that you’ll embark on a perfectly planned,<br />
          safe vacation at a price you can afford.
        </p>
      </b-row>
      <b-card-group id="things-cards">
        <b-card-text
          v-for="thing in data"
          :key="thing.title"
          class="things-card"
        >
          <b-card-body class="card-body thing-card-body">
            <!-- <img :src="thing.image" alt="img-thing" /> -->
            <img
              :src="require(`@/assets/${thing.image}.png`)"
              alt="image thing"
            />
            <b-card-title id="things-card-title">{{
              thing.title
            }}</b-card-title>
            <b-card-text style="text-align: initial">
              {{ thing.body }}
            </b-card-text>
          </b-card-body>
        </b-card-text>
      </b-card-group>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "ThingsYouNeed",
  props: {
    data: Array,
  },
  data() {
    return {
      things_data: [
        {
          image: require("../assets/thing-1.png"),
          title: "Sign Up",
          body: "Sign Up Completes all the work associated with planning and processing",
        },
        {
          image: require("../assets/thing-2.png"),
          title: "Worth of Money",
          body: "After successful access then book from exclusive deals & pricing",
        },
        {
          image: require("../assets/thing-3.png"),
          title: "Exciting Travel",
          body: "Start and explore a wide range of exciting travel experience.",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
.things {
  padding: 5%;
}
.titulo {
  font-family: "Volkhov";
  font-weight: 700;
  font-size: 48px;

  color: #222222;
}
#things-cards {
  justify-content: space-between;
}
.things-card {
  border: none;
  background: white;
  display: flex;
  align-items: first baseline;
  padding: 16px;
}

.thing-card-body {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: column;
  flex-wrap: wrap;
  width: 20rem;
  gap: 5px;
  /* margin-right: 20rem; */
}

#things-card-title {
  font-family: "Poppins";
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  color: #222222;
}
</style>
