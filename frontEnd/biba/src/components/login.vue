<!--
 * @Author: Theo_hui
 * @Date: 2020-10-20 19:57:51
 * @Descripttion: 
-->
<template>
  <el-main>
    <el-card class="box-card">
      <h>登录</h>
      <el-input class="elinput" v-model="loginForm.username" placeholder="用户名"></el-input>
      <el-input class="elinput" v-model="loginForm.password" placeholder="密码" type="password"></el-input>
      <el-button class="sbtn" type="primary" @click="login">登录</el-button>
    </el-card>
  </el-main>
</template>
<style scoped>
  .box-card{
    margin: 200px auto;
    width: 400px;
  }
  .elinput{
    margin-top: 20px;
  }
  .sbtn{
    margin-top: 20px;
    width: 100%;
  }
</style>
 
<script>
import { mapMutations } from 'vuex';
export default {
    name: 'login',
    data () {
        return {
        loginForm: {
            username: '',
            password: ''
        }
    };
  },
 
  methods: {
    ...mapMutations(['changeLogin']),
    login () {
      let _this = this;
      if (this.loginForm.username === '' || this.loginForm.password === '') {
        alert('账号或密码不能为空');
      } else {
        this.axios({
          method: 'post',
          url: 'http://127.0.0.1:5000/api/login',
          data: _this.loginForm
        }).then(res => {
          console.log(res.data);
          _this.userToken =res.data.token;
          console.log(_this.userToken);
          // 将用户token保存到vuex中
          _this.changeLogin({ Authorization: _this.userToken });
          // _this.$router.push('/home');
          alert('登陆成功');
        }).catch(error => {
          console.log(error)
          alert('账号或密码错误');
          console.log(error);
        });
      }
    }
  }

};
</script>