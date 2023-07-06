<template>
  <div>
    <h1>人生预测助手</h1>
    <el-input v-model="form.input" placeholder="Please input"></el-input>
    <el-button @click="submitInput(1)">计算应聘成功率</el-button>
    <el-button @click="submitInput(2)">给出应聘建议</el-button>
    <el-button @click="submitInput(3)">预测未来</el-button>
    <div v-if="response">{{ response }}</div>

    <h3>示例输入</h3>
    <p>预测应聘成功概率示例：</p>
    <p>I have a degree in Computer Science, 2 years of experience in software development, and I'm proficient in Python and Java. I want to apply for the position of Senior Software Engineer at Google.</p>
    <p>I have ten years of driving experience. I want to be a taxi driver to earn a living. Will I succeed?</p>
    <p>提供应聘指导建议示例：</p>
    <p>I'm an experienced programmer, software developer. I have been worked at Google, Microsoft. I want to apply for a job as senior software developer at Amazon.</p>
    <p>预测人生示例：</p>
    <p>I'm a 30-year-old software engineer living in San Francisco. I'm passionate about technology and love to travel. What does my future look like?</p>
    <p>I'm a CS graduated student, I have less money. I live in China, I'm longing for freedom in USA.</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "1",
  data() {
    return {
      form: {
        input: ''
      },
      response: null
    }
  },
  methods: {
    submitInput(type) {
      const payload = {
        type: type,
        content: this.form.input,
        is_audio_input: false,
        audio_input: "",
        gen_img: false
      }

      axios({
        method: 'post',
        url: 'http://cloud.tacoin.site:15000/api',
        data: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json' }
      })
        .then(res => {
          this.response = res.data.result
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>