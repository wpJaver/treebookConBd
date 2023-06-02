<template>
  <div class="app">
    <NavBar />
    <MainBanner :data="dataMainBanner.data" />
    <ThingsYourNeed :data="dataThing.data" />
    <ExclusiveDeals :data="dataExclusive.data" />
    <VacationPlan :data="dataVacationPlan.data" />
    <about-us />
    <GetUpdate :data="dataGetUpdate.data" />
    <SubscribeGet />
    <FooterPag />
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "./components/NavBar.vue";
import MainBanner from "./components/MainBanner.vue";
import ThingsYourNeed from "./components/ThingsYouNeed.vue";
import ExclusiveDeals from "./components/ExclusiveDeals.vue";
import FooterPag from "./components/FooterPag.vue";
import SubscribeGet from "./components/SubscribeGet.vue";
import VacationPlan from "./components/VacationPlan.vue";
import AboutUs from "./components/AboutUs.vue";
import GetUpdate from "./components/GetUpdate.vue";

export default {
  name: "App",

  components: {
    NavBar,
    MainBanner,
    ThingsYourNeed,
    ExclusiveDeals,
    FooterPag,
    SubscribeGet,
    VacationPlan,
    AboutUs,
    GetUpdate,
  },

  data() {
    return {
      dataThing: [],
      dataExclusive: [],
      dataGetUpdate: [],
      dataMainBanner: [],
      dataVacationPlan: [],
    };
  },

  mounted() {
    const urls = [
      "http://127.0.0.1:8000/thing",
      "http://127.0.0.1:8000/exclusive",
      "http://127.0.0.1:8000/getUpdate",
      "http://127.0.0.1:8000/mainBanner",
      "http://127.0.0.1:8000/vacationPlan",
    ];
    const requests = urls.map((url) => axios.get(url));

    axios
      .all(requests)
      .then(
        axios.spread((...responses) => {
          // Respuestas individuales de cada solicitud
          this.dataThing = responses[0];
          this.dataExclusive = responses[1];
          this.dataGetUpdate = responses[2];
          this.dataMainBanner = responses[3];
          this.dataVacationPlan = responses[4];
        })
      )
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
