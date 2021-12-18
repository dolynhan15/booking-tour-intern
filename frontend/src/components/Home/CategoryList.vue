<template>
  <div class="category-list">
    <div class="container">
      <ul class="categories">
        <li>
          <a href="#"><img src="https://livedemo00.template-help.com/wt_51647/images/cta-1-368x420.jpg" alt="" /></a>
          <h3 class="box-categories-title">North Trips</h3>
        </li>
        <li>
          <a href="#"><img src="https://livedemo00.template-help.com/wt_51647/images/cta-2-368x420.jpg" alt="" /></a>
          <h3 class="box-categories-title">Mountain Trips</h3>
        </li>
        <li>
          <a href="#"><img src="https://livedemo00.template-help.com/wt_51647/images/cta-3-368x420.jpg" alt="" /></a>
          <h3 class="box-categories-title">Beach Trips</h3>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "CategoryList",
  };
</script>

<style scoped>
  .categories {
    margin-top: 100px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .categories li {
    height: 420px;
    border: 0.5px solid #999;
    width: 368px;
    display: flex;
    justify-content: center;
    position: relative;
    transition: all 0.3s ease-in-out;
    overflow: hidden;
  }

  .categories li img {
    transition: transform 1s;
  }

  .categories li:hover img {
    opacity: 0.9;
    -ms-transform: scale(1.2);
    -webkit-transform: scale(1.2);
    transform: scale(1.2);
  }

  .categories li h3 {
    font-size: 24px;
    color: #fff;
    position: absolute;
    bottom: 48px;
    font-weight: bold;
  }
</style>