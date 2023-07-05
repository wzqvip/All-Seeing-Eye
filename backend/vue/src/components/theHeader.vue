<template >
  <div style="height:50px;line-height: 50px;border-bottom: 1px solid #ccc;display: flex">
    <router-link to="/1">
      <el-button>主页</el-button></router-link>

    <router-link to="/2">
      <el-button>记录</el-button></router-link>

    <div style="flex: 1"></div>

      <el-button>个人主页</el-button>
      <el-button>Loginout</el-button>

  </div>
</template>

<script>
export default {
  name: "theHeader"
}
</script>

<style scoped>

</style>