<template>
  <div id="demo">
    <div>
      <button v-if="loginType == false" @click="showLoginBox(1)">登录</button>
      <button v-if="loginType == false" @click="showLoginBox(2)">注册</button>
      <button @click="tohome()" v-if="loginType == true">首页</button>
      <button @click="touserinfo()" v-if="loginType == true">个人中心</button>
      <button v-if="loginType == true" @click="showLoginBox(3)">修改</button>
      <div>
        <div class="header">
          <h1>{{ siteinfo.sitename }}</h1>
          <img :src="siteinfo.logo" />
        </div>
        <Test :testName='editName'></Test>
        <div class="content">
          <div class="menu">
            <div v-for="item in menulist" :key="item.id" class="item">
              <div
                v-if="item.id == choosed"
                style="background: #777; color: #fff"
                @click="chooseMenu(item.id)"
              >
                <a style="color: #fff">{{ item.text }}</a>
              </div>
              <div v-else @click="chooseMenu(item.id)">
                <a style="color: #000">{{ item.text }}</a>
              </div>
            </div>
          </div>
          <div class="userlist">
            <p>{{ choosed_text }}</p>
            <hr />
            <router-view @editName='editTestName' @hideBox="hideLoginBox" @changeUI="changeLoginType" />
          </div>
        </div>
      </div>
      <LoginBox
        v-if="boxtarget"
        :target="boxtarget"
        @hideBox="hideLoginBox"
      ></LoginBox>
      <div class="footer">wykuro</div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import LoginBox from "../src/components/LoginBox";
import Test from "../src/components/test";
export default {
  components: {
    LoginBox,
    Test,
  },
  data() {
    return {
      menulist: [],
      choosed: 5,
      choosed_text: "django",
      boxtarget: 0,
      siteinfo: {},
      loginType: false,
      editName:"",
    };
  },
  mounted() {
    try {
      if (window.localStorage.getItem("token").length > 0) {
        this.loginType = true;
      }
    } catch (error) {
      console.log(error);
    }
    this.getmenulist();
  },
  methods: {
    editTestName(newname){
      this.editName=newname
    },
    touserinfo() {
      this.$router.push({ path: "/userinfo" });
    },
    tohome() {
      this.$router.push({ path: "/" });
    },
    getmenulist() {
      axios({
        url: "http://127.0.0.1:9000/get-menu-list/",
        type: "json",
        method: "get",
      }).then((res) => {
        console.log(res.data);
        this.menulist = res.data.menu_data;
        this.siteinfo = res.data.siteinfo;
      });
    },
    chooseMenu(id) {
      if (this.choosed == id) {
        return;
      }
      this.choosed = id;
      for (let i = 0; i < this.menulist.length; i++) {
        if (id == this.menulist[i].id) {
          this.choosed_text = this.menulist[i].text;
        }
      }
      this.$router.push({ path: "/", query: { menuId: id } });
    },
    showLoginBox(value) {
      this.boxtarget = value;
    },
    hideLoginBox() {
      this.boxtarget = 0;
    },
    changeLoginType(bool) {
      this.loginType = bool;
    },
  },
};
</script>
<style>
</style>
