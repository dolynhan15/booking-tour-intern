<template>
  <div class="booking-tour">
    <Navbar/>
    <TourCard/>
    <RequestForm/>
    <Footer/>
  </div>
</template>

<script>
import Navbar from "@/layout/Navbar.vue";
import TourCard from "@/components/BookingTour/TourCard.vue";
import RequestForm from "@/components/BookingTour/RequestForm.vue";
import Footer from "@/layout/Footer.vue";

export default {
  name: "BookingTour",
  components: {
    Navbar,
    TourCard,
    Footer,
    RequestForm,
  },
  data() {
    return {
      userProfile: {},
    }
  }
};
</script>

<style>

</style>
