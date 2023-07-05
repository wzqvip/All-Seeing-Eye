<template>

  <div>

  <div>请帮我预测就职Web前端成功率</div>
  <el-input v-model="form.input" placeholder="Please input" ></el-input>
  <el-button>确定</el-button>
  </div>


</template>

<script>
import theHeader from "@/components/theHeader";
export default {
  name: "1",
  // eslint-disable-next-line vue/no-unused-components
  components: {theHeader},
  data() {
    return {
      form:{},
    }
  },
  methods: {

  },
}
</script>

<style scoped>

</style>