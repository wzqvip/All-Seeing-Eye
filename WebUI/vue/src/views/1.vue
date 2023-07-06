<template>
  <div>
    <h1>人生预测助手</h1>
    <el-input v-model="form.input" placeholder="Please input"></el-input>
    <el-button @click="submitInput(1)">计算应聘成功率</el-button>
    <el-button @click="submitInput(2)">给出应聘建议</el-button>
    <el-button @click="submitInput(3)">预测未来</el-button>
    <div v-if="response">{{ response }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "1",
  data() {
    return {
      form: {},
      response: null
    }
  },
  methods: {
    async submitInput(type) {
      const data = {
        type: type,
        content: this.form.input,
        is_audio_input: false,  // replace with actual value
        audio_input: null,  // replace with actual audio clip if any
        gen_img: false  // replace with actual value
      }
      const res = await axios.post('http://localhost:6666/api', data)  // replace 'http://localhost:6666/api' with actual API endpoint
      this.response = res.data.result
    }
  },
}
</script>

<style scoped>
</style>
