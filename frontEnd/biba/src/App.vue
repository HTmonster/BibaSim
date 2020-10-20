<!--
 * @Author: Theo_hui
 * @Date: 2020-10-20 19:46:43
 * @Descripttion: 
-->
<template>
    <div id="app">
      <el-container>
          <router-view/>
      </el-container>
    </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
