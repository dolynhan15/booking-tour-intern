<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" -->
    <Navbar/>
    <SwiperSlide/>
    <CategoryList/>
    <HotTours/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/layout/Navbar.vue";
import SwiperSlide from "@/components/Home/SwiperSlide.vue";
import HotTours from "@/components/Home/HotTours.vue";
import Footer from "@/layout/Footer.vue";
import CategoryList from "@/components/Home/CategoryList.vue";


export default {
  name: "Home",
  components: {
    Navbar,
    SwiperSlide,
    HotTours,
    Footer,
    CategoryList
  }
};
</script>

<style >
.header,
.footer {
  display: flex;
  align-items: center;
  background-color: #162e44;
  padding: 0px;
  color: #ffffff;
  text-align: center;
  height: 60px;
}
.header {
  position: fixed;
  top:0;
  right: 0;
  left: 0;
  z-index: 5;
}

.container {
  width: 1140px;
  padding: 0;
  margin: 0 auto;
}

.flex {
  display: flex;
  align-items: center;
}
 .btn {
   color: #ffffff;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    padding: 4px 18px;
    margin: 0 4px;
    justify-content: center;
    font-weight: 500;
  }
  .btn:hover {
    opacity:0.8 ;
  }
</style>
