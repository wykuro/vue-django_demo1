<template>
  <div id="login" @click.self="hideSelf">
    <div id="loginbox">
      <div class="form">
        <div v-if="target == 1 || target == 2" class="item">
          <div class="span">用户名:</div>
          <input v-model="username" type="text" placeholder="用户名" />
        </div>
        <div v-if="target == 1 || target == 2" class="item">
          <div class="span">密码:</div>
          <input v-model="password" type="text" placeholder="密码" />
        </div>
        <div v-if="target == 2" class="item">
          <div class="span">重复密码:</div>
          <input v-model="password2" type="text" placeholder="密码" />
        </div>
        <div v-if="target == 3" class="item">
          <div class="span">网站名称:</div>
          <input v-model="sitename" type="text" placeholder="网站名称" />
        </div>
        <div v-if="target == 3" class="item">
          <div class="span">图片上传:</div>
          <input
            id="uploadlogo"
            @change="uploadImg($event)"
            type="file"
            style="width: 175px"
          />
        </div>
        <div v-if="target == 3" class="item">
          <img :src="testlogo" />
        </div>
        <button v-if="target == 1" @click="tologin">登录</button>
        <button v-if="target == 2" @click="toregister">注册</button>
        <button v-if="target == 3" @click="toupload">确定</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "LoginBox",
  props: ["target"],
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      sitename: "",
      testlogo: "",
    };
  },
  methods: {
    tologin() {
      console.log(this.username, this.password);
      let username = this.username;
      let password = this.password;
      if (username.length > 0 && password.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/login/",
          data: Qs.stringify({
            username,
            password,
          }),
          method: "post",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }).then((res) => {
          switch (res.data) {
            case "none":
              alert("用户名不存在");
              break;
            case "err":
              alert("密码错误");
              break;
            default:
              alert("成功");
              window.localStorage.setItem("token", res.data.token);
              var userinfo = res.data.userinfo;
              this.$store.commit("editUserinfo", userinfo);
              if (this.$route.path != "/userinfo") {
                this.$router.push({ path: "/userinfo" });
              }
          }
        });
      } else {
        alert("用户名或密码不能为空");
      }
    },
    hideSelf() {
      this.$emit("hideBox");
    },
    toregister() {
      let username = this.username;
      let password = this.password;
      let password2 = this.password2;
      console.log(username, password, password2);
      if (username.length > 0 && password.length > 0 && password2.length > 0) {
        if (password != password2) {
          alert("密码两次不一样");
        } else {
          axios({
            url: "http://127.0.0.1:9000/register/",
            data: Qs.stringify({
              username,
              password,
              password2,
            }),
            method: "post",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
          }).then((res) => {
            console.log(res);
            switch (res.data) {
              case "same":
                alert("存在同名用户");
                break;
              default:
                break;
            }
          });
        }
      } else {
        alert("缺少必填项");
      }
    },
    toupload() {
      let sitename = this.sitename;
      let logo = this.testlogo;
      if (sitename.length > 0 && logo.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/upload-logo/",
          method: "put",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          data: Qs.stringify({
            sitename,
            logo,
          }),
        }).then((res) => {
          if (res.data == "ok") {
            window.location.reload();
          }
        });
      } else {
        alert("没有新的内容");
      }
    },
    uploadImg(e) {
      var logo = e.target.files[0];
      console.log(logo);
      var Img = new FormData();
      Img.append("logo", logo);
      axios({
        url: "http://127.0.0.1:9000/upload-logo/",
        method: "post",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        data: Img,
      }).then((res) => {
        console.log(res);
        if (res.data) {
          console.log(res.data);
          this.testlogo = "http://127.0.0.1:9000/upload/" + res.data.img;
        }
      });
    },
  },
};
</script>

<style>
#login {
  width: 500px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  position: absolute;
}
#loginbox {
  width: 300px;
  height: 300px;
  border: 1px solid black;
  background: #00000090;
  display: flex;
  justify-content: center;
  align-items: center;
}
#loginbox .form .item {
  color: #fff;
  font-weight: 700;
  margin: 10px auto;
}
.span {
  float: left;
  width: 80px;
}
</style>