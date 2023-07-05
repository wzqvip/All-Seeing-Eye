<script>
import theHeader from "@/components/theHeader";
import axios from "axios";
import {ElMessage} from "element-plus";

export default {
  name: "2",
  // eslint-disable-next-line vue/no-unused-components
  components: {theHeader},
  data() {
    return {

      handlePre:false,
      list:[],//
      pngVisible:false,//
      url:'',//
      dialogConsult :false,
      // url:"https://picsum.photos/200/300",
      total:100,
      search:"",
      tableData: [
        {
          patientName:"",
          uploadTime:"",
          patientSex:"",
          // patientAge:"",
          patientBirthTime:""
        }
      ],
      // form:{
      //   doctorName:''
      // },
      form1:
          {
            search:''
          },
      form2:
          {
            patientName:'',
            uploadTime:'',
            text:''
          },
    }
  },

  mounted() {
    this.fetchData();

  },
  methods: {

    // onClose() {
    //   this.imgModal = false
    // },
    // // 切换图片 index为图片下标值
    // onSwitch(index) {
    //   this.imgSrcIndex = index
    // },
    // // 点击空白部分关闭弹窗
    // expressImgPreview(e) {
    //   if (e.target.getAttribute('class') === 'el-image-viewer__mask') {
    //     this.previewImgModal = false
    //   }
    // },
    // closeImgViewer(){
    //   this.imgViewerVisible = false;
    //   // const m = (e) => { e.preventDefault() };
    //   // document.body.style.overflow = 'auto';
    //   // document.removeEventListener("touchmove", m, true);
    // },



    fetchData() {
      // const form={
      //   doctorName:global.user.name
      // };
      axios({
        method:"post",
        url:global.baseUrl+"/doctor/queryCaseAll",
        // headers:{
        //   'Authorization':"Bearer "+tokenUtils.getToken(),
        // },
        params:{
          doctorName:global.user.name
        }
      }).then(res => {
        this.tableData = res.data.data.obj;
        console.log(res.data.data.token)
        //tokenUtils.setToken(res.data.data.token)
      })},
    // fetchData() {
    //
    //   axios.post("http://10.133.145.136:10393/mock/47f0b42c-189f-4c61-b545-6f40295ac4d4/doctor",this.form)
    //       .then(res => {
    //         const Array=[res.data.thh,res.data.ttt]
    //          this.tableData = Array;
    //       })
    //       ;
    // },//成功

    // check(){
    //   request.post("http://10.132.5.46:10393/mock/47f0b42c-189f-4c61-b545-6f40295ac4d4/doctor",this.form1).then(res=>
    //   {
    //
    //     console.log(res)
    //   });
    //   this.form1={}
    // },


    Consult(row){
      row.dialogConsult  = false;
      this.form2.patientName = row.patientName;
      this.form2.uploadTime = row.uploadTime;
      axios({
        method:"post",
        url:global.baseUrl+"/doctor/doCase",
        headers:{
          //'Authorization':"Bearer "+tokenUtils.getToken(),
        },
        params:{
          patientName:this.form2.patientName,
          uploadTime:this.form2.uploadTime,
          text:this.form2.text
        }
      }).then(res => {
        //tokenUtils.setToken(res.data.data.token)
        console.log(res.data)
        this.form2={}
      });
      ElMessage("处理成功")
      // axios.post("http://10.133.145.136:10393/mock/47f0b42c-189f-4c61-b545-6f40295ac4d4/doctor",this.form2).then(res=>
      // {
      //
      //   console.log(res)
      // });
    },

    // handleDownload(row) {
    //   ElMessage("已完成下载")
    //   const form={uploadTime:row.uploadTime,patientName:row.patientName};
    //   axios({
    //     method:"post",
    //     url:global.baseUrl+"/doctor/downloadDicom",
    //     headers:{
    //       'Authorization':"Bearer "+tokenUtils.getToken(),
    //     },
    //     // params:{
    //     //   uploadTime:form.uploadTime,
    //     // }
    //   }).then(res => {
    //     tokenUtils.setToken(res.data.data.token)
    //     console.log(res.data);
    //   });
    // },
    // handlePreview(row) {
    //   ElMessage("已完成下载")
    //   const form={patientName:row.patientName,uploadTime:row.uploadTime};
    //
    //   axios({
    //     method:"post",
    //     url:global.baseUrl+"/doctor/downloadPng",
    //     headers:{
    //       'Authorization':"Bearer "+tokenUtils.getToken(),
    //     },
    //     // params:{
    //     //   uploadTime:form.uploadTime,
    //     // }
    //   }).then(res => {
    //     tokenUtils.setToken(res.data.data.token);
    //     console.log(res.data);
    //   });
    // },
    // handlePreviewed(row) {
    //   const form={patientName:row.patientName,uploadTime:row.uploadTime};
    //
    //   // axios({
    //   //   method:"post",
    //   //   url:global.baseUrl+"/doctor/file/previewedPng",
    //   //   headers:{
    //   //     Authorization:"Bearer "+tokenUtils.getToken(),
    //   //   },
    //   //   data:form
    //   // }).then(res => {
    //   //   tokenUtils.setToken(res.data.data.token);
    //   //   this.list=res.data.data.list;
    //   //   this.pngVisible=true;
    //   //   console.log(res.data);
    //   // });
    // },
    handleConsult(){
      this.dialogConsult = true
    }
    // handlePreview() {
    //
    // },
    // handleConsult() {
    //
    // }
  }
}
</script>

<template>
  <div>
    <div style="display: flex">

      <div style="flex: 1">
        <div style="padding: 10px">
          <div style="margin: 0 10px">
            <el-input v-model="form1.search" placeholder="搜索" style="width: 20%;"/>
            <el-button style="margin-left: 5px" @click="check">搜索</el-button>
          </div>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="patientName" label="患者姓名" width="120"></el-table-column>
            <el-table-column prop="uploadTime" label="上传时间" width="180"></el-table-column>
            <el-table-column label="DICOM图片">
              <template #default="scope">
                <el-button size="small" type="text" @click="handleDownload(scope.$index, scope.row)">下载</el-button>
              </template>
            </el-table-column>
            <el-table-column label="处理图片组">
              <template #default="scope">
                <el-button size="small" type="text" @click="handlePreview (scope.$index, scope.row)">下载</el-button>
                <!--          <el-button size="small" type="text" @click="handlePreviewed(scope.$index, scope.row)">预览</el-button>-->
                <el-dialog
                    :visible.sync="pngVisible"
                    width="80%"
                >
                  <div style="height:500px;text-align: center">


                  </div>
                </el-dialog>

                <!--          <el-dialog v-model="handlePreview" title="处理图片">-->
                <!--            <img :src="url"/>-->
                <!--            <el-form :model="form">-->
                <!--              <el-form-item label="用户名" style="width: 180px;margin-left: 50px">-->
                <!--                <el-input v-model="form.username" autocomplete="off"/>-->
                <!--              </el-form-item>-->
                <!--              <el-form-item label="密码" style="width: 226px;margin-left: 64px">-->
                <!--                <el-input v-model="form.password" autocomplete="off"/>-->
                <!--              </el-form-item>-->
                <!--              <el-form-item label="手机号" style="width: 360px;margin-left: 50px">-->
                <!--                <el-input v-model="form.phoneNum" autocomplete="off"/>-->
                <!--              </el-form-item>-->
                <!--              <el-form-item label="邮箱" style="width: 346px;margin-left: 64px">-->
                <!--                <el-input v-model="form.email" autocomplete="off"/>-->
                <!--              </el-form-item>-->
                <!--            </el-form>-->
                <!--            <template #footer>-->
                <!--                    <span class="dialog-footer">-->
                <!--                      <el-button @click="handlePreview = false">取消</el-button>-->
                <!--                      <el-button type="primary" @click="handlePreview = false">-->
                <!--                        确认-->
                <!--                      </el-button>-->
                <!--                    </span>-->
                <!--            </template>-->
                <!--          </el-dialog>-->

              </template>
            </el-table-column>
            <el-table-column label="患者病历">
              <template #default="scope">
                <el-button size="small" type="text" @click="scope.row.dialogConsult=true">诊断</el-button>
                <el-dialog v-model="scope.row.dialogConsult" title="患者病历" class="dialog">
                  <el-form :model="form">
                    <el-form-item label="性别：" style="width: 180px;margin-left: 50px">
                      <div>{{scope.row.patientSex}}</div>
                      <!--                              <el-input v-model="form.username" autocomplete="off"/>-->
                    </el-form-item>
                    <!--                            <el-form-item label="年龄：" style="width: 180px;margin-left: 50px">-->
                    <!--                              <div>{{scope.row.patientAge}}</div>-->
                    <!--&lt;!&ndash;                              <el-input v-model="form.password" autocomplete="off"/>&ndash;&gt;-->
                    <!--                            </el-form-item>-->
                    <el-form-item label="生日：" style="width: 180px;margin-left: 50px">
                      <div>{{scope.row.patientBirthTime}}</div>
                      <!--                              <el-input v-model="form.phoneNum" autocomplete="off"/>-->
                    </el-form-item>
                    <el-form-item label="医师诊断" style="width: 600px;margin-left: 64px">
                      <el-input v-model="form2.text" autocomplete="off"/>
                    </el-form-item>
                  </el-form>
                  <template #footer>
                                  <span class="dialog-footer">
                                    <el-button @click="scope.row.dialogConsult  = false">取消</el-button>
                                    <el-button type="primary" @click="Consult(scope.row)">
                                      确认
                                    </el-button>
                                  </span>
                  </template>
                </el-dialog>
              </template>
            </el-table-column>
          </el-table>
          <div style="margin: 0 10px">
            <el-pagination layout="prev, pager, next" :total="total" />
          </div>
        </div>
      </div>
    </div>

    <!--    <el-image-viewer-->
    <!--        class="image-shenmai-close"-->
    <!--        v-if="imgViewerVisible"-->
    <!--        :on-close="closeImgViewer"-->
    <!--        :on-switch="onSwitch"-->
    <!--        :close-on-press-escape=true-->
    <!--        :url-list="previewList"-->
    <!--        :initial-index="imgSrcIndex"-->
    <!--        @click.native="expressImgPreview"-->
    <!--    />-->
    <!--    <el-button @click.prevent="this.imgViewerVisible=true">anniu</el-button>-->

    <!-- 预览组件 -->



    <!-- 预览按钮 -->



  </div>
</template>

<style>


.dialog {
  z-index: 9999;
}
</style>