<template>
  <div class="header">
    <div class="container">
      <div class="navbar flex">
        <a class="navbar-brand" href="/"><img src="../assets/logo-traveling.png" alt="" /></a>

        <ul class="navbar-menu flex">
          <li class="navbar-nav-item active">
            <a class="navbar-nav-link" href="/">Home</a>
          </li>
          <li class="navbar-nav-item">
            <a class="navbar-nav-link" href="/detail">Category</a>
          </li>
          <li class="navbar-nav-item">
            <a class="navbar-nav-link" href="/about">About</a>
          </li>
        </ul>

        <div class="search">
          <el-input placeholder="Country, city, tourist destination..." v-model="search" class="">
            <el-button type="primary" slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </div>

        <div class="account">
          <a class="btn">Register</a>
          <a class="btn btn-signin"><strong>Sign in</strong> </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Navbar",
    data() {
      return {
        search: "",
      };
    },
  };
</script>

<style scoped>
  .navbar-nav-item {
    border-top: 3px solid transparent;
  }

  .navbar-nav-link {
    position: relative;
    text-decoration: none;
    letter-spacing: 0.05em;
    color: rgb(255, 255, 255);
    z-index: 1;
    padding: 18px 15px 20px;
    line-height: 1.2;
    font-weight: 500;
  }

  .navbar-brand {
    height: 60px;
    overflow: hidden;
  }

  .navbar-brand img {
    height: 72px;
    margin: 0 20px;
  }

  .navbar-nav-item.active {
    background: rgba(255, 255, 255, 0.11);
    border-top: 3px solid #01b3a7;
  }

  .navbar-nav-item:hover {
    background: rgba(255, 255, 255, 0.11);
    border-top: 3px solid #01b3a7;
  }

  .search {
    flex: 1;
    margin: 0 20px;
  }

  .btn-signin {
    border: 2px solid #01b3a7;
    color: #01b3a7;
  }

  .btn-signin:hover {
    background-color: #01b3a7;
    border: 2px solid #01b3a7;
    color: #ffffff;
    opacity: 1;
  }
</style>