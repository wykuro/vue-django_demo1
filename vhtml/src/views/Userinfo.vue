<template>
    <div class="userinfo">
        <h1>我的信息</h1>
        <img :src="'http://127.0.0.1:9000/upload/'+userinfo.headimg">
        <div>{{ userinfo.nickname }}</div>
        <div>身份:管理员</div>
        <input v-model="changeNickName" type="text" name="" >
        <button @click="changeAllNickName">修改</button>
    </div>
</template>

<script>
import {eventBus} from '../main.js';
export default {
    data(){
        return{
            userinfo:{},
            changeNickName:"",
        }
    },
    mounted(){
        this.getuserinfo()
        this.changePageUI()
    },
    methods:{
        changeAllNickName(){
            var NickName=this.changeNickName
            this.userinfo.nickname=NickName
            // this.$emit('editName',NickName)
            eventBus.$emit('changeTestName',NickName)
        },
        getuserinfo(){
            this.userinfo=this.$store.state.userinfo
            console.log(this.userinfo.headimg);
        },
        changePageUI(){
            this.$emit('changeUI',true)
            this.$emit('hideBox')
        }
    }   
};
</script>

<style scoped>

</style>