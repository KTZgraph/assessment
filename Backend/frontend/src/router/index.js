import Vue from "vue";
import VueRouter from "vue-router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import Home from "../views/Home.vue";
import CropImage from "../views/CropImage.vue";


Vue.use(VueRouter);
Vue.use(BootstrapVue);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/crop",
    name: "cropImage",
    component: CropImage
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
