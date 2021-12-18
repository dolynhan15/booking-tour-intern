<template>
  <el-row type="flex" class="row-bg" justify="center">
    <el-col :span="12" class="request-form">
      <h2 class="form-title">Contact information form</h2>
      <el-form
        :model="ruleForm"
        :rules="rules"
        ref="ruleForm"
        label-width="120px"
        class="request-form-body"
      >
        <el-form-item label="Họ tên" prop="name">
          <el-input placeholder="Họ tên" v-model="ruleForm.name"></el-input>
        </el-form-item>
        <el-form-item label="Địa chỉ" prop="address">
          <el-input placeholder="Địa chỉ" v-model="ruleForm.address"></el-input>
        </el-form-item>
        <el-row>
          <el-col :span="14">
            <el-form-item label="Email" prop="email">
              <el-input
                type="email"
                placeholder="Email"
                v-model="ruleForm.email"
              ></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="10">
            <el-form-item label="Số điện thoại" prop="phone">
              <el-input
                placeholder="Số điện thoại"
                v-model="ruleForm.phone"
              ></el-input>
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item label="Số người">
          <el-input-number
            v-model="ruleForm.numPerson"
            :min="1"
            :max="10"
          ></el-input-number>
        </el-form-item>

        <el-form-item label="Khuyến mãi" prop="discount">
          <el-input placeholder="Khuyến mãi" v-model="ruleForm.discount"
            ><i slot="suffix"><span>%</span> </i></el-input
          >
        </el-form-item>
        <el-form-item>
          <el-button class="btn-create-booking" @click="submitForm('ruleForm')"
            >Create</el-button
          >
          <el-button class="btn-reset" @click="resetForm('ruleForm')"
            >Reset</el-button
          >
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>
<script>
import { required, minLength, between } from 'vuelidate/lib/validators'
export default {
  name: "RequestForm",
  data() {
    return {
      ruleForm: {
        name: "",
        address: "",
        email: "",
        phone: "",
        numPerson: 1,
        discount: 0,
      },
      rules: {
        name: [
          {
            required: true,
            message: "Please input your name",
            trigger: "blur",
          },
        ],
        address: [
          {
            required: true,
            message: "Please input your address",
            trigger: "blur",
          },
        ],
        email: [
          {
            required: true,
            message: "Please input your email",
            trigger: "blur",
          },
          {
            type: "email",
            message: "Please input correct email address",
            trigger: ["blur", "change"],
          },
        ],
        phone: [
          {
            required: true,
            message: "Please input your phone",
            trigger: "blur",
          },
          {
            type: "string",
            required: true,
            pattern: /^[0-9]+$/,
            message: "Please input correct phonenumber",
          },
          {
            min: 10,
            max: 10,
            message: "Phone number has 10 digit number",
            trigger: "blur",
          },
        ],
        discount: [
          {
            required: true,
            message: "Please input your discount",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("submit!");
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>
<style scoped>
.form-title {
  text-align: center;
  font-weight: 500;
  text-transform: uppercase;
}
.request-form {
  border: 1px solid #8fa4bd70;
  background: #f9f9f9;
  margin-bottom: 50px;
}
.request-form:hover {
  box-shadow: 0 1px 10px 0 rgb(0 0 0 / 5%), 0 0px 63px 0 rgb(0 0 0 / 5%);
}
.request-form-body {
  margin: 30px;
}
.btn-create-booking {
  border: 1px solid #198881b0;
  color: #202216;
  font-weight: 500;
}
.btn-create-booking:hover {
  background-color: #01b3a7;
  border: 1px solid #01b3a7;
  color: #ffffff;
  opacity: 1;
}
.btn-reset {
  border: 1px solid #2c4644b0;
  color: #202216;
  font-weight: 500;
}
.btn-reset:hover {
  background-color: #b5b3bba4;
  opacity: 1;
}
.error {
  color: red
}
</style>
