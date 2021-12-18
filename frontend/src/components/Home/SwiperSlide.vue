<template>
    <div class="swiper-slide">
        <img src="@/assets/slider-1.jpg">
        <div class="swiper-slide-caption section-md">
            <div class="container">
                <div class="row">
                    <div class="col-md-10">
                        <h6>A team of professional Travel Experts</h6>
                        <h2>
                            <span>Trust</span>
                            <span class="font-weight-bold"> Our Experience</span>
                        </h2>
                        <a class="">Get in touch</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {
  name: "SwiperSlide"
};
</script>

<style scoped>
.swiper-slide {
  margin-top: 60px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  white-space: nowrap;
}
.swiper-slide img {
  width: 100%;
  min-height: 400px;
  background-size: cover;
  background-repeat: no-repeat;
}
.swiper-slide-caption {
  position: absolute;
  color: #ffffff;
  letter-spacing: 0.1em;
}
.swiper-slide-caption h6 {
  text-transform: uppercase;
  font-size: 16px;
  margin: 0;
  font-weight: 500;
}
.swiper-slide-caption h2 {
  font-weight: 500;
  letter-spacing: 0.05em;
  font-size: 64px;
  margin: 0 4px;
}
.swiper-slide-caption .font-weight-bold {
  font-weight: 700;
}
.swiper-slide-caption a {
  color: #ffffff;
  box-sizing: border-box;
  border: 2px solid #ffffff;
  padding: 12px 0;
  font-weight: 500;
  width: 160px;
  cursor: pointer;
  text-align: center;
}
.swiper-slide-caption a:hover {
  background-color: #50ba87;
  border: 2px solid #50ba87;
  transition: all 0.3s ease-in-out;

}
</style>
