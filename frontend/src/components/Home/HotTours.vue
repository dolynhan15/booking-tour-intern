<template>
  <div class="container">
    <h3 class="title">Hot Tours</h3>
    <div class="unit flex">
      <div class="unit-left">
        <a class="product-big-figure">
          <img src="@/assets/slider-2.jpg" width="600" height="366"
        /></a>
      </div>
      <div class="unit-body">
        <div class="product-big-body">
          <h5 class="product-big-title">
            <a href="#">Da Nang, Hoi An</a>
          </h5>
          <div class="group-sm group-middle justify-content-start">
            <el-rate
              v-model="value"
              disabled
              show-score
              text-color="#ff9900"
              score-template="{value} points"
            >
            </el-rate>
          </div>
          <p class="product-big-text">
            Benidorm is a buzzing resort with a big reputation for beach
            holidays. Situated in sunny Costa Blanca, the town is one of the
            original Spanish beach resorts...
          </p>
          <a class="btn btn-booking-tour" href="#">Book This Tour</a>
          <div class="product-big-price-wrap">
            <span class="product-big-price">$790</span>
          </div>
        </div>
      </div>
    </div>
    <div class="view-more">
     <a href="#">View More</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "HotTours",
  data() {
    return {
      value: 3.7,
    };
  },
};
</script>

<style >
h3.title {
  padding: 50px;
  font-size: 36px;
  line-height: 1.2;
  text-align: center;
}
.unit {
  position: relative;
  border: 1px solid #e1e1e1;
}
.unit .unit-left {
  flex-basis: 50%;
  margin: 0 0 -8px;
}
.unit-left a {
  width: 584px;
  height: 336px;
  overflow: hidden;
}
.unit .unit-body .product-big-body {
  padding-left: 12%;
  padding-right: 85px;
}
.product-big-title a {
  font-size: 21px;
}
.product-big-title a:hover {
  color: #01b3a7;
}
.product-big-text {
  margin-top: 15px;
  letter-spacing: 0.025em;
  color: #9b9b9b;
}
.product-big-body .btn-booking-tour {
  color: #151515;
  margin-top: 15px;
  box-sizing: border-box;
  padding: 11px;
  width: 170px;
  border: 2px solid #151515;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
.product-big-body .btn-booking-tour:hover {
  background-color: #01b3a7;
  border-color: #01b3a7;
}

.product-big-price-wrap {
  height: 58px;
  width: 70px;
  top: -1px;
  right: -1px;
  position: absolute;
  overflow: hidden;
  text-align: center;
  z-index: 1;
  padding: 18px 12px 2px;
}
.product-big-price-wrap::before {
  position: absolute;
  content: "";
  bottom: 0;
  left: 24px;
  width: 400%;
  height: 100%;
  background: #01b3a7;
  transform: skew(45deg);
  transform-origin: 50% 100%;
  will-change: transform;
  pointer-events: none;
  z-index: -1;
}
.product-big-price {
  font-weight: 600;
  font-size: 21px;
  letter-spacing: 0.025em;
  color: #ffffff;
}
.view-more {
  margin: 50px 0;
  text-align: center;
}
.view-more a {
  border-radius: 5px;
   color: #ffffff;
  background-color: #151515;
  box-sizing: border-box;
  padding:6px 12px;
  border: 2px solid #151515;
  font-weight: 600;
  text-align: center;
  transition: all 0.3s ease-in-out;
}
.view-more a:hover {
  opacity: 0.8;
}

</style>
