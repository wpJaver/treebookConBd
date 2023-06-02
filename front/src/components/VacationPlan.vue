<template>
  <div>
    <b-container>
      <!-- TITULO -->
      <b-row>
        <b-col>
          <h1 id="titulo">
            Best <span class="color-naranja"> vacation plan</span>
          </h1>
        </b-col>
      </b-row>
      <!-- Cuerpo -->
      <b-row>
        <b-col>
          <p>
            Plan your perfect vacation with our travel agency. Choose <br />
            hundreds of all-inclusive offers!
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
                  <b-container
                    style="
                      border: 2px solid rgba(102, 102, 102, 0.08);
                      border-radius: 8px;
                      border-top: none;
                    "
                  >
                    <b-row>
                      <b-col class="deals-card-col-title">
                        <h5 id="deals-card-title">{{ item.city }}</h5>
                        <p id="vacation-card-star">{{ item.price }}</p>
                      </b-col>
                    </b-row>
                    <b-row class="deals-card-row-body">
                      <b-col>
                        <p id="vacation-card-location">
                          {{ item.quantity_days }}
                        </p>
                      </b-col>

                      <b-col>
                        <p id="deals-card-star">
                          {{ item.rating }}
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
  name: "VacationPlan",
  props: {
    data: Array,
  },
  data() {
    return {
      deals_data: [
        {
          cards: [
            {
              city: "Rome, Italy",
              price: "5.42K",
              quantity_days: "10 Days Trip",
              rating: "4.8",
              image: require("../assets/rome.jpg"),
            },
            {
              city: "London, UK",
              price: "2.42K",
              quantity_days: "07 Days Trip",
              rating: "4.7",
              image: require("../assets/london2.png"),
            },
            {
              city: "Osaka,Japan",
              price: "5.42K",
              quantity_days: "10 Days Trip",
              rating: "4.8",
              image: require("../assets/osaka.png"),
            },
          ],
        },

        {
          cards: [
            {
              city: "Rome, Italy",
              price: "$5.42K",
              quantity_days: "10 Days trip",
              rating: "4.8",
              image: require("../assets/rome.jpg"),
            },
            {
              city: "London, UK",
              price: "$2.42K",
              quantity_days: "07 Days trip",
              rating: "4.7",
              image: require("../assets/london2.png"),
            },
            {
              city: "Osaka,Japan",
              price: "$5.42K",
              quantity_days: "10 Days trip",
              rating: "4.8",
              image: require("../assets/osaka.png"),
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

#deals-card-title {
  font-family: "Poppins";
  font-weight: 500;
  font-size: 24px;
  color: #222222;
}

#deals-card-star {
  font-family: "Poppins";
  font-weight: 400;
  font-size: 16px;
  color: #666666;
}
#vacation-card-star {
  font-family: "Poppins";
  font-weight: 600;
  font-size: 24px;
  color: #fa7436;
}
#vacation-card-location {
  font-family: "Poppins";
  font-weight: 500;
  font-size: 16px;
  color: #666666;
}
#vacation-card-location::before {
  content: url("../assets/Navigation.png");
}
#deals-card-star::before {
  margin-right: 10%;
  content: url("../assets/star.png");
}

.deals-card-row-body {
  flex-wrap: nowrap;
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
