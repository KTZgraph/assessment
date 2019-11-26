import Vue from "vue";
import VueRouter from "vue-router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import Home from "@/views/Home.vue";
import ImageCropper from "@/components/ImageCropper.vue";
import Document from "@/views/Document.vue";
import AnswerCreator from "@/views/AnswerCreator.vue"
import NewDocument from "@/views/NewDocument.vue"
import AnswerAssessment from "@/views/AnswerAssessment.vue"

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
    path: "/document/:document_id",
    name: "document",
    component: Document,
    props: true
  },
  {
    path: "/new-document",
    name: "new-document",
    component: NewDocument,
    props: false
  },
  {
    path: "/crop",
    name: "image-cropper",
    component: ImageCropper,
    props: true
  },
  {
    path: "/document",
    name: "document-editor",
    component: ImageCropper
  },
  {
    path: "/document/:document_id/answer-assessment/:answer_id",
    name: "answer-assessment",
    component: AnswerAssessment,
    props: true
  },
  {
    path: "/answer-creator/:document_id",
    name: "answer-creator",
    component: AnswerCreator,
    props: true
  }

];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
