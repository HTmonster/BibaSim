/*
 * @Author: Theo_hui
 * @Date: 2020-10-20 20:40:16
 * @Descripttion: 
 */
import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
 
const store = new Vuex.Store({
 
  state: {
    // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : ''
  },
 
  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin (state, user) {
      console.log("xxxx")
      state.Authorization = user.Authorization;
      localStorage.setItem('Authorization', user.Authorization);
    }
  }
});
 
export default store;