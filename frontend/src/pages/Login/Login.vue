<template>
  <div>
    <el-form ref="form"
             class="login-form"
             label-width="120px"
             method="POST"
             @submit.native.prevent="login"
             @keyup.enter="login">
      <div v-if="error !== ''" class="text-danger">
        {{ error }}
      </div>
      <br/>
      <el-form-item label-width="0px" prop="email">
        <el-input v-model="loginFormData.email"
                  aria-describedby="emailHelp"
                  class="form-control form-control-user"
                  placeholder="Email Address"
                  type="email"></el-input>
      </el-form-item>
      <el-form-item label-width="0px" prop="password">
        <el-input v-model="loginFormData.password"
                  class="form-control form-control-user"
                  placeholder="Password"
                  type="password"
        >
        </el-input>
      </el-form-item>
      <el-form-item label-width="0px">
        <div class="text-center">
          <el-button :loading="loading"
                     block
                     class="login-button mt-0 mb-0"
                     native-type="submit"
                     type="primary"
          >Login
          </el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>


import LoginService from "@/services/LoginService/LoginService";

export default {
  name: "Login",
  data() {
    return {
      error: "",
      loginFormData: {
        email: "",
        password: "",
      },
      success: false,
      loading: false
    };
  },
  methods: {
    login: async function () {
      if (await this.validation() === true) {
        const data = await LoginService.login(this.loginFormData)
        if (data) {
          localStorage.setItem("access_token", data["access_token"])
        //   const user = await GetUserService.getCurrentUser(token.sub)
        //   if (user) {
        //     const {id, email, profile, admin} = user.data;
        //
        //     const userData = {
        //       user: id,
        //       email: email,
        //       name: profile.name,
        //       profile_id: profile.id,
        //       is_admin: admin
        //     }
        //     localStorage.setItem("email", email);
        //     localStorage.setItem("user_id", id);
        //     localStorage.setItem("profile_id", profile.id);
        //     localStorage.setItem("is_admin", admin);
        //     localStorage.setItem("imageUrl", profile.image);
        //     localStorage.setItem("name", profile.name);
        //     if (this.$router.currentRoute.name === "Login") {
        //       await this.$router.push("/");
        //       this.$router.go(0);
        //     }
        //   } else {
        //     this.error = "Wrong Password or Email";
        //     this.loginFormData.email = "";
        //     this.loginFormData.password = "";
        //   }
        // } else
        //   this.error = 'Invalid Password'
      }}
    },
    validation: async function () {
      this.error = "";
      if (!this.loginFormData.email) {
        this.error = "Missing Email";
        return false;
      } else if (!this.validEmail(this.loginFormData.email)) {
        this.error = "Email wrong type";
        return false;
      } else if (!this.loginFormData.password || this.loginFormData.password.length < 6) {
        this.error = "Password has at least 6 params";
        return false;
      }
      return true;
    },
    validEmail: function (email) {
      const re = /^(([^<>()\]\\.,;:\s@"]+(\.[^<>()\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  }
};
</script>

<style>

</style>
