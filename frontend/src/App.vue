<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
body {
  box-sizing: border-box;
  margin: 0;
  font-family: "Montserrat", sans-serif, Arial, sans-serif;
  box-sizing: border-box;
  font-size: 16px;
  line-height: 1.71429;
  font-weight: 400;
  letter-spacing: normal;
  color: #151515;
  background-color: #ffffff;
  -webkit-text-size-adjust: none;
  -webkit-font-smoothing: subpixel-antialiased;
}
a {
  position: relative;
    display: inline-block;
    text-decoration: none;
    transition: all 0.3s ease-in-out;
    color: #151515;
}
ul, ol {
    list-style: none;
    padding: 0;
    margin: 0;
}

.row {
    display: flex;
    flex-wrap: wrap;
    margin-left: -4px;
    margin-right: -4px;
}
.header__navbar {
    display: flex;
    justify-content: space-between;
}

</style>
