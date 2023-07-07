<template>
  <div class="container">
    <h1>人生预测助手</h1>
    <el-input
      type="textarea"
      :rows="2"
      :autosize="{ minRows: 2, maxRows: 10}"
      v-model="form.input"
      placeholder="Please input"
    ></el-input>
    <el-button @click="submitInput(1)">计算应聘成功率</el-button>
    <el-button @click="submitInput(2)">给出应聘建议</el-button>
    <el-button @click="submitInput(3)">预测未来</el-button>
    <h3>结果展示：</h3>
    <div  style="border:solid;border-radius: 10px;border-color:#51b6b6" v-if="response">{{ response }}</div>

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

<style scoped>
.container {
  background-image: linear-gradient(to right, #fbc2eb, #a6c1ee);

  font-family: Arial, sans-serif;
  padding: 20px;
  border-radius: 5px;
  max-width: 800px;
  margin: 0 auto;
}

.input-field {
  width: 100%;  /* This will make the input field take up the full width of its parent container */
  resize: both; /* This allows the user to resize both the width and the height of the input field */
  overflow: auto; /* Necessary for 'resize' to work */
}


h1 {
  color: #101010;
  text-align: center;
  padding-bottom: 10px;
}

h3 {
  color: #251f64;
  padding-top: 20px;
}

p {
  color: #000000;
  line-height: 1.6;
}

.el-input {
  margin-bottom: 20px;
}

.el-button {
  margin-right: 10px;
  margin-bottom: 20px;
}

.el-button:last-child {
  margin-right: 0;
}

</style>