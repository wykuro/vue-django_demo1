<template>
  <div id="login-userinfo">
    <img src="../assets/1.jpg" />
    <div>{{ nickname }}</div>
  </div>
</template>
<script>
import {eventBus} from '../main.js';
export default {
    mounted(){
        eventBus.$on('changeTestName',(data)=>{
            console.log(data)
            this.nickname=data
        })
    },
    props:['testName'],
    data(){
        return{
            nickname:''
        }
    },
}
</script>

<style scoped>

</style>