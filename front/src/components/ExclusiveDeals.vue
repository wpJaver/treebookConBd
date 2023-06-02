<template>
  <div>
    <b-container>
      <!-- TITULO -->
      <b-row>
        <b-col>
          <h1 class="titulo">
            Exclusive <span class="color-naranja">deals & discounts</span>
          </h1>
        </b-col>
      </b-row>
      <!-- Cuerpo -->
      <b-row>
        <b-col>
          <p>
            Discover our fantastic early booking discounts<br />
            & start planning your journey.
          </p>
        </b-col>
      </b-row>
      <!-- CARROUSEL -->
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
                  <b-container class="b-container-deals">
                    <b-row>
                      <b-col class="deals-card-col-title">
                        <h5 class="deals-card-title">{{ item.city }}</h5>
                        <p class="deals-card-star">{{ item.rating }}</p>
                      </b-col>
                    </b-row>
                    <b-row class="deals-card-row-body">
                      <b-col>
                        <p class="deals-card-location">
                          {{ item.country }}
                        </p>
                      </b-col>
                      <b-col></b-col>
                      <b-col>
                        <p class="deals-card-old-price">
                          {{ item.old_price }}
                        </p>
                      </b-col>
                      <b-col>
                        <p class="deals-card-new-price">
                          {{ item.new_price }}
                        </p>
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
  name: "ExclusiveDeals",
  props: {
    data: Array,
  },
  data() {
    return {
      new_data: {},
      data_cards: [],
      deals_data: [
        {
          cards: [
            {
              city: "Madrid",
              rating: "4.8",
              country: "Spain",
              old_price: "950",
              new_price: "850",
              image: require("../assets/Madrid.png"),
            },
            {
              city: "Firenze",
              rating: "4.5",
              country: "Italy",
              old_price: "850",
              new_price: "750",
              image: require("../assets/Firense.png"),
            },
            {
              city: "Paris",
              rating: "4.4",
              country: "France",
              old_price: "699",
              new_price: "599",
              image: require("../assets/Paris.png"),
            },
            {
              city: "London",
              rating: "4.8",
              country: "UK",
              old_price: "850",
              new_price: "850",
              image: require("../assets/London.png"),
            },
          ],
        },

        {
          cards: [
            {
              city: "Paris",
              rating: "4.4",
              country: "France",
              old_price: "699",
              new_price: "599",
              image: require("../assets/Paris.png"),
            },
            {
              city: "Firenze",
              rating: "4.5",
              country: "Italy",
              old_price: "850",
              new_price: "750",
              image: require("../assets/Firense.png"),
            },
            {
              city: "London",
              rating: "4.8",
              country: "UK",
              old_price: "850",
              new_price: "850",
              image: require("../assets/London.png"),
            },
            {
              city: "Madrid",
              rating: "4.8",
              country: "Spain",
              old_price: "950",
              new_price: "850",
              image: require("../assets/Madrid.png"),
            },
          ],
        },
      ],
    };
  },
};
</script>
<style>
.card-body {
  padding: 0 !important;
}
.deals-card-col-title {
  display: flex;
  justify-content: space-between;
}
.b-container-deals {
  border: 2px solid rgba(102, 102, 102, 0.08);
  border-radius: 8px;
  border-top: none;
}
.deals-card-title {
  font-family: "Poppins";
  font-weight: 500;
  font-size: 24px;
  color: #222222;
}

.deals-card-star {
  font-family: "Poppins";
  font-weight: 400;
  font-size: 16px;
  color: #666666;
}

.deals-card-star::before {
  margin-right: 10%;
  content: url("../assets/star.png");
}

.deals-card-row-body {
  flex-wrap: nowrap;
}

.deals-card-location {
  font-family: "Poppins";
  font-weight: 400;
  font-size: 14px;
  color: #666666;
}
.deals-card-location::before {
  content: url("../assets/location.png");
}

.deals-card-old-price {
  font-family: "Poppins";
  font-weight: 500;
  font-size: 16px;
  color: #999999;
  text-decoration: line-through;
}

.deals-card-new-price {
  font-family: "Poppins";
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  color: #fa7436;
  background: #ffe7db;
  border-radius: 8px;
}

.carousel-control-prev,
.carousel-control-next {
  position: relative !important;
  display: inline !important;
}

.carousel-control-prev-icon {
  background: #fa7436;
  border: 1px solid rgba(153, 153, 153, 0.5);
  border-radius: 50%;
  width: 100%;
  margin-right: 1rem;
  margin-top: 2rem;
}

.carousel-control-next-icon {
  background: #fa7436;
  border: 1px solid rgba(153, 153, 153, 0.5);
  border-radius: 50%;
  width: 100%;
}
.sr-only {
  display: none;
}
</style>
