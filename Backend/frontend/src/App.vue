<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';

import NavbarComponent from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
  },
  methods:{
    async setUserInfo(){
      let endpoint = `/api/user/`;
      axios.get(endpoint)
          .then(response => {
              if(response){
                  const requestUser = response.data.username;
                  window.localStorage.setItem("username", requestUser);
              }
      })
    }
  },
  created(){
    this.setUserInfo();
  }
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Playfair Display", serif;
}
.btn:focus {
  box-shadow: none !important;
}
</style>