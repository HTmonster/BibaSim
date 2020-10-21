<template>
    <el-container>
        <el-header>
            <el-menu class="el-menu-demo" mode="horizontal" >
                <el-menu-item index='4' ><el-avatar>{{username}}</el-avatar><el-button type="danger" plain @click="userlogout">登出</el-button></el-menu-item>
                <el-menu-item index='2'>
                    <i class="el-icon-files"></i>
                    文件访问
                </el-menu-item>
                <el-menu-item index='3' disabled>用户访问</el-menu-item>
                
            </el-menu>
        </el-header>
        <el-main>
            <div class="main">
              <el-table
                :data="objects"
                border
                :row-class-name="tableRowClassName">
                <el-table-column
                prop="id"
                label="id"
                width="100"
                >
                </el-table-column>
                <el-table-column
                prop="name"
                label="名称"
                width="400">
                </el-table-column>
                <el-table-column
                prop="w"
                width="180"
                label="写权限">
                    <template slot-scope="scope">
                        <el-tag v-if="scope.row.w" size="medium">可写</el-tag>
                        <el-tag v-else size="medium" type="danger">不可写</el-tag>
                    </template>
                </el-table-column>
                <el-table-column
                prop="r"
                width="180"
                label="读权限">
                <template slot-scope="scope">
                    <el-tag v-if="scope.row.r" size="medium">可读</el-tag>
                    <el-tag v-else size="medium" type="danger">不可读</el-tag>
                </template>
                </el-table-column>
                <el-table-column
                fixed="right"
                label="操作"
                >
                <template slot-scope="scope">
                    <el-button v-if="scope.row.w" type="text" @click="dialogFormVisible = true;writeid=scope.row.id">写入</el-button>
                    <el-button v-else type="text" disabled>写入</el-button>

                    <el-button v-if="scope.row.r" type="text" @click="readObject(scope.row.id)">读取</el-button>
                    <el-button v-else type="text" disabled>读取</el-button>
                </template>
                </el-table-column>
            </el-table>
            </div>
             <el-button @click="getPbjects">刷新数据</el-button>

             <el-dialog
                title="文件内容"
                :visible.sync="dialogVisible"
                width="50%"
                :before-close="handleClose">
                <span>{{dialogContent}}</span>
                <span slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
                </span>
            </el-dialog>

            <el-dialog title="文件写入" :visible.sync="dialogFormVisible">
                <el-form >
                    <el-form-item label="写入文件内容" :label-width="formLabelWidth">
                    <el-input v-model="wcontent" type="textarea" rows=10></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="writeObject">确 定</el-button>
                </div>
            </el-dialog>

        </el-main>
    </el-container>
</template>

<style scoped>
    .logo{
        display:inline-block;
        font-size: 45px;
    }
    .main{
        
        margin:100px auto;
        display: flex;
        width: 80%;

    }
</style>

<script>
import { mapMutations } from 'vuex';
  export default {
    mounted:function(){
        this.getPbjects();
        this.username=localStorage.getItem('username')
    },
    methods: {
        getPbjects(){
            this.axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/api/objects',
            auth:{username: localStorage.getItem('Authorization')}
            }).then(res => {
                console.log(res.data);
                this.objects=res.data.data;
                console.log(this.objects);
            }).catch(error => {
                console.log(error);
                this.$message.error('抱歉 刷新失败');
            });
        },
        readObject(id){
            this.axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/api/objects/'+id,
            auth:{username: localStorage.getItem('Authorization')}
            }).then(res => {
                console.log(res.data);
                this.dialogContent=res.data.data;
                this.dialogVisible=true;
                // this.objects=res.data.data;
                // console.log(this.objects);
            }).catch(error => {
                this.$message.error('抱歉 请求失败');
            });
        },
        writeObject(){
            let _this=this
            this.axios({
            method: 'post',
            url: 'http://127.0.0.1:5000/api/objects/'+this.writeid,
            data: {data:_this.wcontent},
            auth:{username: localStorage.getItem('Authorization')}
            
            }).then(res => {
                console.log(res.data);
                if(res.data.status=="OK"){
                    this.$message({
                        message: '写入成功',
                        type: 'success'
                    });
                    this.dialogFormVisible=false;
                    this.wcontent=""
                }else{
                    this.$message.error('抱歉 写入失败');
                }

            }).catch(error => {
                this.$message.error('抱歉 写入失败');
            });
        },


        ...mapMutations(['logout']),
        userlogout (){
            this.logout()
            this.$router.push('/login');
        }
    },
    data () {
        return {
            dialogVisible:false,
            dialogFormVisible:false,
            writeid:-1,
            wcontent:"",
            dialogContent:"",
            objects:[]
    }
  }
  }
</script>