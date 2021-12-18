<template>
  <div class="container">
    <div class="main">
      <div class="title">
        <el-breadcrumb
          class="bread-crumb"
          separator-class="el-icon-arrow-right"
        >
          <el-breadcrumb-item>Home page</el-breadcrumb-item>
          <el-breadcrumb-item>Booking Tour</el-breadcrumb-item>
        </el-breadcrumb>
      </div>

      <div class="unit">
        <div class="unit-left">
          <a class="product-big-figure">
            <img src="@/assets/slider-2.jpg" width="300" height="200"
          /></a>
        </div>
        <div class="unit-body">
          <div class="product-big-body">
            <h5 class="product-big-title">
              <a href="#">Da Nang, Hoi An</a>
            </h5>
            <div class="product-big-text">
              <el-row>
                <el-col :span="6"><div class="grid-content">Tour</div></el-col>
                <el-col :span="18"
                  ><div class="grid-content font-weight">1001</div></el-col
                >
              </el-row>
              <el-row>
                <el-col :span="6"
                  ><div class="grid-content">Duration</div></el-col
                >
                <el-col :span="18"
                  ><div class="grid-content font-weight">
                    2 days 3 nights
                  </div></el-col
                >
              </el-row>
              <el-row>
                <el-col :span="6"><div class="grid-content">Fare</div></el-col>
                <el-col :span="18"
                  ><div class="grid-content font-weight">
                    1.999.999đ
                  </div></el-col
                >
              </el-row>
              <el-row>
                <el-col :span="6"
                  ><div class="grid-content">Departure date</div></el-col
                >
                <el-col :span="18"
                  ><div class="grid-content font-weight">
                    16/12/2021
                  </div></el-col
                >
              </el-row>
            </div>
          </div>
        </div>
      </div>
      <div class="attention-text">
        <ul>
          <li>
            Expenses incurred (if any): surcharge for foreign guests; surcharge
            for single room; surcharge for tour price difference…
          </li>
          <li>
            Vietnam Tourism staff will call to advise you right after receiving
            the ticket booking confirmation. (In administrative hours)
          </li>
          <li>
            In the event that you do not agree with the arising amounts, Your
            booking confirmation will not be valid.
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TourCard",
  data() {
    return {
      value: 3.7,
    };
  },
};
</script>

<style scoped>
.main {
  margin-top: 60px;
  margin-bottom: 30px;
}
.bread-crumb {
  margin: 50px 50px;
  padding: 15px;
  background: #8db6d985;
}
.el-breadcrumb span {
  font-size: 16px;
  cursor: pointer;
  font-weight: bold;
  color: #283c64;
}
.title {
  padding-top: 20px;
}
.img {
  background-repeat: no-repeat;
  background-size: auto;
}
.attention-text {
  padding-left: 10%;
  justify-content: center;
  color: #ca0a0a;
}
.font-weight {
  font-weight: bold;
}
.unit {
  position: relative;
  border: 1px solid #e1e1e1;
  margin: 51px;
  display: flex;
  box-shadow: 0 1px 10px 0 rgb(0 0 0 / 12%), 0 0px 63px 0 rgb(0 0 0 / 14%);
}
.unit:hover {
  box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.24),
    0 10px 50px 0 rgba(0, 0, 0, 0.19);
}
.unit .unit-left::before {
  position: absolute;
  top: 0;
  left: -75%;
  z-index: 2;
  display: block;
  content: "";
  width: 50%;
  height: 100%;
  background: -webkit-linear-gradient(
    left,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 100%
  );
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 100%
  );
  -webkit-transform: skewX(-25deg);
  transform: skewX(-25deg);
}
@-webkit-keyframes shine {
  100% {
    left: 125%;
  }
}
@keyframes shine {
  100% {
    left: 125%;
  }
}
.unit:hover .unit-left::before {
  -webkit-animation: shine 2s;
  animation: shine 2s;
}
.unit:hover .product-big-body h5 {
  border-bottom: solid 1px #35fdb3c7;
}
.unit:hover .product-big-title a {
  color: #01b3a7;
}

.unit .unit-left {
  margin: 0 0 -8px;
}
.unit-left a {
  align-content: center;
  overflow: hidden;
  display: unset;
}
.unit .unit-body .product-big-body {
  padding-left: 5%;
  padding-right: 85px;
  color: red;
}
.unit-body {
  background: #f9f9f9;
}
.product-big-title a {
  font-size: 16px;
}
.product-big-title a:hover {
  color: #01b3a7;
}
.product-big-text {
  letter-spacing: 0.025em;
  width: 650px;
  color: #2d4271;
}
.product-big-body .btn-booking-tour {
  color: #151515;
  box-sizing: border-box;
  padding: 11px;
  width: 170px;
  border: 2px solid #151515;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
.product-big-body h5 {
  border-bottom: solid 1px rgba(0, 0, 0, 0.15);
  margin-top: 17px;
}
.product-big-body .btn-booking-tour:hover {
  background-color: #01b3a7;
  border-color: #01b3a7;
}

ul, ol {
    list-style: disc;
    padding: 0;
    margin: 0;
}
</style>
