import Vue from "vue";
import VueRouter from "vue-router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import Home from "../views/Home.vue";
import ImageCropper from "@/components/ImageCropper.vue";
// import DocumentEditor from "../views/DocumentEditor.vue";

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
    name: "image-cropper",
    component: ImageCropper
  },
  {
    path: "/document",
    name: "document-editor",
    component: ImageCropper
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
