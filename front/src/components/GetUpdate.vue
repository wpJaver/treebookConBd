<template>
  <div>
    <b-container style="padding: 5%">
      <!-- TITULO -->
      <b-row>
        <h1 class="titulo">
          Get update with <span class="color-naranja"> latest blog</span>
        </h1>
      </b-row>
      <!-- CARD -->
      <b-container>
        <b-carousel controls indicators>
          <b-carousel-slide>
            <template v-slot:img>
              <b-card-group>
                <b-card
                  v-for="(item, index_img) in data"
                  :key="index_img"
                  style="margin-right: 1rem; border: none"
                >
                  <b-card-img
                    :src="require(`@/assets/${item.image}.png`)"
                    alt="img-deals"
                    style="width: 100%"
                  />
                  <b-container
                    style="
                      border: 2px solid rgba(102, 102, 102, 0.08);
                      border-radius: 8px;
                      border-top: none;
                    "
                  >
                    <b-row>
                      <b-col class="getUp-card-col-title">
                        <h5 id="get-update-card-title">{{ item.text }}</h5>
                        <p id="get-update-card-body">{{ item.date }}</p>
                      </b-col>
                    </b-row>
                  </b-container>
                </b-card>
              </b-card-group>
            </template>
          </b-carousel-slide>
        </b-carousel>
      </b-container>
    </b-container>
  </div>
</template>
<script>
export default {
  name: "GetUpdate",
  props: {
    data: Array,
  },
  data() {
    return {
      deals_data: [
        {
          cards: [
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/amazing-diference-year.png"),
            },
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/travel-for-enough.png"),
            },
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/save-money-while.png"),
            },
          ],
        },

        {
          cards: [
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/amazing-diference-year.png"),
            },
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/travel-for-enough.png"),
            },
            {
              text: "The Amazing Difference a Year of Travelling .",
              date: "July 27, 2021",
              image: require("../assets/save-money-while.png"),
            },
          ],
        },
      ],
    };
  },
};
</script>
<style>
#get-update-card-title {
  font-family: "Poppins";
  font-weight: 500;
  font-size: 18px;
  color: #222222;
}
#get-update-card-body {
  font-family: "Inter";
  font-weight: 400;
  font-size: 16px;
  color: #999999;
}
</style>
