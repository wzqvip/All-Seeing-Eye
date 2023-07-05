<script>


export default {
  name: "PatPerson",
  components: {

  },
  data() {
    return {

      userData:global.user,
      form:{
        username:global.user.username,
        password:'',
        phone:'',
        email:'',
        pictureURL:''
      },
      tableData: [
        {
          username:'',
          password:'',
          phone:'',
          email:'',
          pictureURL:''

        }
      ],
    }
  },
  methods:{
    save(){
      this.dialogFormVisible=false;
      // axios({
      //   method:"post",
      //   url:global.baseUrl+"/user/update",
      //   headers:{
      //     'Authorization':"bearer "+tokenUtils.getToken()
      //   }
      // }).then((res)=>{
      //   tokenUtils.setToken(res.data.data.token)
      //   global.user.username=res.data.data.obj.username;
      //   global.user.password=res.data.data.obj.password;
      //   global.user.phone=res.data.data.obj.phone;
      //   global.user.email=res.data.data.obj.email;
      //   global.user.pictureURL=res.data.data.obj.pictureURL;
      //   location.reload(true)
      //   // console.log(res.data)
      //   // const Array=[res.data]
      //   // this.tableData = Array;
      // });
      // axios.post("http://10.132.28.181:10393/mock/1c09042f-aab9-4287-a99f-4c3c4f35d9d7/user/update",this.form).then(res=>
      // {
      //   global.user.username=res.data.username;
      //   global.user.password=res.data.password;
      //   global.user.phone=res.data.phone;
      //   global.user.email=res.data.email;
      //   global.user.pictureURL=res.data.pictureURL;
      //   // console.log(res.data)
      //   // const Array=[res.data]
      //   // this.tableData = Array;
      // });
    }
  }
}
</script>

<template>
  <div>
    <div style="display: flex">
      <div class="column side">
<!--        <img src="../assets/biden.jpeg" height="650" width="440"/>-->
      </div>
      <div class="column middle">
        <h1>个人中心</h1>
        <br><br><br>
        <br><br><br>
        <br><br>
        <p>用户名：{{userData.username}}</p>
        <br>
        <div class="order">
          <span style="white-space:pre">   </span><span class="line"></span>
        </div>
        <br>
        <p>身份：{{userData.role}}</p>
        <br>
        <div class="order">
          <span style="white-space:pre">   </span><span class="line"></span>
        </div>
        <br>
        <p>手机号：{{userData.phone}}</p>
        <br>
        <div class="order">
          <span style="white-space:pre">   </span><span class="line"></span>
        </div>
        <br>
        <p>邮箱：{{userData.email}}</p>
        <br>
        <div class="order">
          <span style="white-space:pre">   </span><span class="line"></span>
        </div>
        <div class="el-button2">
          <!--    <el-row class="mb-4" size="large">-->
          <el-button round style="color: #51b6b6" @click="dialogFormVisible=true">编辑</el-button>

        </div>
      </div>
    </div>

  </div>
</template>



<style >
img {
  border-radius: 8px;
}
.column {
  float: left;
  padding: 10px;
}
.column.side {
  width: 40%;
}
.column.middle {
  width: 60%;
}
.row:after {
  content: "";
  display: table;
  clear: both;
}
h1 {font-size:60px;}
p {font-size:40px;}

.order {
  height: 20px;
  line-height: 20px;
}
.order .line {
  display: inline-block;
  padding-top : 3px;
  width: 90%;
  border-top: 10px dotted #000000;

}
body
{
  /*background-color:white;*/
  /*background-image:url('../assets/bg.png');*/

}

.el-button2{
  /*width: 230px;*/
  /*height: 200px;*/
  position: absolute;
  top: 30%;
  left: 55%;
  transform: translate(-50%,-50%);
}
</style>