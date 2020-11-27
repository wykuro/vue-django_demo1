<template>
  <div id="userlist">
    <div v-for="item in imglist" :key="item.pk" class="user">
      <img :src="apiurl + 'upload/' + item.headimg" />
      <p>{{ item.nickname }}</p>
      <button @click="deleteuser(item.id)">删除</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  data() {
    return {
      apiurl: "http://127.0.0.1:9000/",
      imglist: [],
      menuId: 5,
    };
  },
  mounted() {
    this.getUserlist(this.menuId);
  },
  watch: {
    $route(to) {
      this.menuId = to.query.menuId;
      this.getUserlist(this.menuId);
    },
  },
  methods: {
    getUserlist(id) {
      axios({
        url: "http://127.0.0.1:9000/get-user-list/",
        type: "json",
        params: {
          id,
        },
        method: "get",
      }).then((res) => {
        this.imglist = res.data;
      });
    },
    deleteuser(id) {
      axios({
        url: "http://127.0.0.1:9000/get-user-list/",
        type: "json",
        data: Qs.stringify({
          id,
        }),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        method: "delete",
      }).then((res) => {
        if(res.data=='ok'){
          this.getUserlist(this.menuId)
        }
      });
    },
  },
};
</script>

<style scoped>
</style>