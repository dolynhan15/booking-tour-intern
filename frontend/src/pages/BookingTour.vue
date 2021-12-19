<template>
  <div class="booking-tour">
    <Navbar/>
    <TourCard/>
    <RequestForm v-bind:userProfile="userProfile"/>
    <Footer/>
  </div>
</template>

<script>
import Navbar from "@/layout/Navbar.vue";
import TourCard from "@/components/BookingTour/TourCard.vue";
import RequestForm from "@/components/BookingTour/RequestForm.vue";
import Footer from "@/layout/Footer.vue";
import UserProfileService from "@/services/UserProfileService/UserProfileService";

export default {
  name: "BookingTour",
  components: {
    Navbar,
    TourCard,
    Footer,
    RequestForm,
  },
  async created() {
    this.userProfile = await UserProfileService.getUserProfileById(localStorage.getItem("user_profile_id"))
    console.log(this.userProfile)

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
